from constants import *
from .operator_queue import OperatorQueue, OpQueueNode
from .evaluation_history import EvaluationHistory


class ParenNode:
  def __init__(self):
    self.items = []

  def __repr__(self):
    return f'ParNode {self.items}'


evaluation_node_count = 1

class EvaluationNode:
  def __init__(self, value, was_paren=False):
    global evaluation_node_count

    self.id = evaluation_node_count
    self.was_paren = was_paren

    try:
      self.value = float(value)
    except:
      self.value = value # this should only be the case when `value` is an operator
    finally:
      evaluation_node_count += 1

  def __repr__(self):
    is_from_paren = ' paren' if self.was_paren else ''
    return f'EvNode id={self.id} value={str(self.value) + is_from_paren}'



class ParenTree:
  def __init__(self):
    self.root = None

  def __repr__(self):
    return f'ParenTree: {self.root}'

  def parse_char_list(self, char_list: list):
    def traverse_list(lst: list):
      node = ParenNode()
      while len(lst):
        char = lst.pop(0)
        if char == LEFT_PAREN:
          paren_node_item = traverse_list(lst)
          node.items.append(paren_node_item)
        elif char == RIGHT_PAREN:
          return node
        else:
          node.items.append(char)
      return node
    
    self.root = traverse_list(char_list)
  
  def evaluate(self):
    if not self.root:
      return

    def create_evaluation_nodes(node: ParenNode):
      accum = []
      for x in node.items:
        if type(x) is ParenNode:
          evaluation_result = traverse(x)
          evaluation_node = EvaluationNode(evaluation_result, was_paren=True)
          accum.append(evaluation_node)
        else:
          evaluation_node = EvaluationNode(x)
          accum.append(evaluation_node)
      return accum

    def do_math(**kwargs):
      left = kwargs.get('left')
      right = kwargs.get('right')
      operator = kwargs.get('operator')
      if operator == EXPONENT:
        return left**right
      elif operator == MULTIPLY:
        return left * right
      elif operator == DIVIDE:
        return left / right if right != 0 else 0
      elif operator == ADD:
        return left + right
      elif operator == SUBTRACT:
        return left - right

    def traverse(node: ParenNode):
      queue = OperatorQueue()

      eval_history = EvaluationHistory()

      eval_node_list = create_evaluation_nodes(node)

      queue.enqueue_evaluation_nodes(eval_node_list)

      accum = 0
      while len(queue):
        x = queue.dequeue()
        i = x.operator_index
        ev_node = x.eval_node
        left = get_from(eval_node_list, i - 1)
        right = get_from(eval_node_list, i + 1)

        operation = {
          'operator': ev_node.value,
          'left': eval_history.most_recent(left),
          'right': eval_history.most_recent(right),
        }
        
        result = do_math(**operation)
        
        eval_history.add(left, right, result)
  
        accum = result
      
      return accum
    
    return traverse(self.root)