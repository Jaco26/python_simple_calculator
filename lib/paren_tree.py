from constants import *
from models.char_list import create_simple_char_list

class ParenNode:
  def __init__(self):
    self.text = []
    self.children = []
  
  def __repr__(self):
    return f'ParenNode - text: {self.text}'


class ParenTree:
  def __init__(self, some_str):
    char_list = create_simple_char_list(some_str)
    self.root = self.build_from(char_list)

  def __repr__(self):
    def traverse(node: ParenNode, accum, tab):
      accum += tab + node.__repr__() + '\n'
      if len(node.children):
        tab += '  '
        for child in node.children:
          accum += traverse(child, '', tab) 
      return accum
    return traverse(self.root, '', '')

  def build_from(self, char_list: list):
    node = ParenNode()
    while len(char_list):
      item = char_list.pop(0)
      if item == LEFT_PAREN:
        child_node = self.build_from(char_list)
        node.text.append(f'PAREN_{len(node.children)}')
        node.children.append(child_node)
      elif item == RIGHT_PAREN:
        return node
      else:
        node.text.append(item)
    return node

  