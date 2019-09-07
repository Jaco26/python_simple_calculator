import sys
from models import CharList, PriorityQueue
from constants import *

operators = ['(', ')', '*', '**', '/', '+', '-']


test_strings = {
  's1': '8.33*(1/  2.1 )',
  's2': '8 + (9 - 3 / (9 + 3))',
  's3':'''this is the outside 
            (hello 
              (this is the 
                (most inner)
              )
              (what are you)
            )''',
  's4': '3 * 9 / 34 - 9',
}

def to_float(val):
  try:
    return float(val)
  except:
    return None

def get_priority(char):
  if char == LEFT_PAREN:
    return 1
  elif char == EXPONENT:
    return 2
  elif char == MULTIPLY:
    return 3
  elif char == DIVIDE:
    return 4
  elif char == ADD:
    return 5
  elif char == SUBTRACT:
    return 6


class ParenNode:
  def __init__(self):
    self.value = ''
    self.children = []


def chomp_str(some_str):
  queue = PriorityQueue()
  char_list = CharList(some_str)

  for (item, left, right) in char_list:
    if item.value in operators:
      if right.value != LEFT_PAREN:
        queue.enqueue(left, item, right)
        right.queued = True
        item.queued = True
        left.queued = True

  return queue



def main():
  arg = ''.join(sys.argv[1:])
  input_expr = test_strings[arg] if test_strings.get(arg) else arg
  print(input_expr)
  print('-----'*3)
  ops = chomp_str(input_expr)
  print(ops.values)

if __name__ == '__main__':
  main()