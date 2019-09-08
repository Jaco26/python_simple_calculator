import sys
# from models import CharList, PriorityQueue
# from build_paren_tree import OperationsTree
from constants import *
from lib import OperationsTree


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
  's4': '3 * 9 / 34 - 9 * (9 + 7 )',
}

def to_float(val):
  try:
    return float(val)
  except:
    return None

# def chomp_str(some_str):
#   queue = PriorityQueue()
#   char_list = CharList(some_str)
#   # demo('THIS IS WHAT I DID YESTERDAY', char_list)
#   for i, (item, left, right) in enumerate(char_list):
#     if item.value in operators:
#       # if right.value != LEFT_PAREN:
#       #   queue.enqueue(item=[left, item, right])
#       # if item.value == LEFT_PAREN:
#       #   chomp_str(''.join(char_list._items[i:]))
#       # else:
#       queue.enqueue(item=[left, item, right])

#   return queue



  
def main():
  arg = ''.join(sys.argv[1:])
  input_expr = test_strings[arg] if test_strings.get(arg) else arg
  op_tree = OperationsTree(input_expr)
  


if __name__ == '__main__':
  main()