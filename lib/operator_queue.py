from constants import *

class OpQueueNode:
  def __init__(self, eval_node, operator_index, priority):
    self.eval_node = eval_node
    self.operator_index = operator_index
    self.priority = priority
  
  def __repr__(self):
    return f'OpQNode {self.priority} {self.eval_node}'


class OperatorQueue:
  def __init__(self):
    self.exponents = []
    self.multiply_divide = []
    self.add_subtract = []

  def __repr__(self):
    return f'PriorityQueue:\nexponents: {self.exponents}\nmult_div: {self.multiply_divide}\nadd_sub: {self.add_subtract}'

  def __len__(self):
    return len(self.exponents) + len(self.multiply_divide) + len(self.add_subtract)

  def enqueue_evaluation_nodes(self, evaluation_node_list):
    for i, eval_node in enumerate(evaluation_node_list):
      priority = i
      if eval_node.value == MULTIPLY:
        # check if we're multiplying ParenNodes
        # if so, prioritize this item
        left = get_from(evaluation_node_list, i - 1)
        right = get_from(evaluation_node_list, i + 1)
        if left.was_paren and right.was_paren:
          priority = 0
      node = OpQueueNode(eval_node, i, priority)
      self.enqueue(node)

  def enqueue(self, node: OpQueueNode):
    op = node.eval_node.value
    if op == EXPONENT:
      self.exponents.append(node)
      self.exponents = sorted(self.exponents, key=lambda x: x.priority)
    elif op in [MULTIPLY, DIVIDE]:
      self.multiply_divide.append(node)
      self.multiply_divide = sorted(self.multiply_divide, key=lambda x: x.priority)
    elif op in [ADD, SUBTRACT]:
      self.add_subtract.append(node)
      self.add_subtract = sorted(self.add_subtract, key=lambda x: x.priority)

  def dequeue(self):
    if len(self.exponents):
      return self.exponents.pop(0)
    elif len(self.multiply_divide):
      return self.multiply_divide.pop(0)
    elif len(self.add_subtract):
      return self.add_subtract.pop(0)
    
    