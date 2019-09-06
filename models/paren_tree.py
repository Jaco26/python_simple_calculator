from .priority_queue import NaivePriorityQueue

LEFT_PAREN = '('
RIGHT_PAREN = ')'
EXPONENT = '**'
MULTIPLY = '*'
DIVIDE = '/'
ADD = '+'
SUBTRACT = '-'

class CharList:
  def __init__(self, some_str):
    one_line = paren_str.replace('\n', '')
    single_spaces = ''.join([x for x in one_line.split('  ') if x])
    self.value = list(single_spaces)

  def __sizeof__(self):
    return len(self.value)

  def shift(self):
    if len(self.value):
      return self.value.pop(0)
    return None

def chomp_str(string):
  section = ''
  queue = NaivePriorityQueue()
  def inner(char_list: CharList):
    while len(char_list):
      char = char_list.shift()
      priority = get_priority(char)
      if priority:
        next_char = char_list.pop(0)
        if get_priority(next_char) == 1: # paren
          pass
        section += char
        queue.enqueue(section, priority)
        return queue


def get_priority(sign):
  if sign == LEFT_PAREN:
    return 1
  elif sign == EXPONENT:
    return 2
  elif sign == MULTIPLY:
    return 3
  elif sign == DIVIDE:
    return 4
  elif sign == ADD:
    return 5
  elif sign == SUBTRACT:
    return 6



class ParenTreeNode:
  def __init__(self):
    self.raw_expression = ''
    self.children = []
    self.operations = NaivePriorityQueue()

  def parse_raw_expression(self):
    '''Parse self.raw_expression into operations in the priority queue'''
    pass



class ParenTree:
  def __init__(self, paren_str):
    one_line = paren_str.replace('\n', '')
    single_spaces = ''.join([x for x in one_line.split('  ') if x])
    character_list = list(single_spaces)
    def parse_char_list(char_list: list):
      node = ParenTreeNode()
      while len(char_list):
        char = char_list.pop(0)
        if char == LEFT_PAREN:
          child_node = parse_char_list(char_list)
          node.operations.enqueue(child_node, 1)
        elif char == RIGHT_PAREN:
          node.parse_raw_expression()
          return node
        else:
          node.expression += char
      node.parse_raw_expression()
      return node

    self.root = parse_paren_str(paren_str)
