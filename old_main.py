#!/usr/local/bin/python3
import sys

LEFT_PAREN = '('
RIGHT_PAREN = ')'
EXPONENT = '**'
MULTIPLY = '*'
DIVIDE = '/'
ADD = '+'
SUBTRACT = '-'

def operate(sign, left, right):

  left = float(left)
  right = float(right)

  if sign == EXPONENT:
    return left**right
  elif sign == MULTIPLY:
    return left * right
  elif sign == DIVIDE:
    return left / right
  elif sign == ADD:
    return left + right
  elif sign == SUBTRACT:
    return left - right

test_strings = {
  's1': '8 * (1 / 2)',
  's2': '8 + (9 - 3 / (9 + 3))',
  's3':'''this is the outside 
            (hello 
              (this is the 
                (most inner)
              )
              (what are you)
            )'''
}

class Node:
  def __init__(self):
    self.expression = ''
    self.children = []

  def __repr__(self):
    return f'Node - {self.expression} - children: {len(self.children)}'


def parse_paren_string(paren_string: str):
  one_line = paren_string.replace('\n', '')
  single_spaces = ''.join([x for x in one_line.split('  ') if x])
  character_list = list(single_spaces)
  def parse_char_list(char_list: list):
    node = Node()
    while len(char_list):
      char = char_list.pop(0)
      if char == LEFT_PAREN:
        child_node = parse_char_list(char_list)
        node.children.append(child_node)
      elif char == RIGHT_PAREN:
        return node
      else:
        node.expression += char
    return node
  return parse_char_list(character_list)

class ParenTree:
  def __init__(self, paren_string: str):
    self.root = parse_paren_string(paren_string)

  def display(self):
    def traverse(node: Node, tab=''):
      print(tab, node)
      if len(node.children):
        tab += '  '
        for child in node.children:
          traverse(child, tab)
    traverse(self.root)

  def evaluate(self):

    def extract_lr(items: list, sign):
      index = items.index(sign)
      left = items.pop(index - 1)
      items.pop(index - 1)
      right = items.pop(index - 1)
      return left, right


    def traverse(node: Node):
      exp_items = [x for x in node.expression.split(' ') if x]

      evaluated_children = []
      print(node.expression)

      for child_node in node.children:

        res = {
          'operator': exp_items.pop(),
          'evaluated_child': traverse(child_node)
        }
        evaluated_children.append(res)

      value_accum = 0

      if EXPONENT in exp_items:
        item = exp_items.pop(exp_items.index(EXPONENT))
        items = [x for x in item.split(EXPONENT)]
        value_accum += exponent(*items[:2])
      if MULTIPLY in exp_items:
        left, right = extract_lr(exp_items, MULTIPLY)
        value_accum += operate(MULTIPLY, left, right)
      if DIVIDE in exp_items:
        left, right = extract_lr(exp_items, DIVIDE)
        value_accum += operate(DIVIDE, left, right)
      if ADD in exp_items:
        left, right = extract_lr(exp_items, ADD)
        value_accum += operate(ADD, left, right)
      if SUBTRACT in exp_items:
        left, right = extract_lr(exp_items, SUBTRACT)
        value_accum += operate(SUBTRACT, left, right)

      # if evaluated_children:
      #   for x in evaluated_children:
          # print(x)
        
      return value_accum
    return traverse(self.root)
      

def main():
  expr = ' '.join(sys.argv[1:])
  tree = ParenTree(test_strings[expr]) if test_strings.get(expr) else ParenTree(expr)
  # print(tree.root.expression)
  # print(tree.root.children)
  # tree.display()
  result = tree.evaluate()
  print(result)
  # print(tree.root.children[0].children)
  

if __name__ == '__main__':
  main()





