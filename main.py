import sys
from constants import demo
from lib import ParenTree

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
  's5': '(9 + 8)/(8 * 2) + 9',
  's6': '(9 * (3 + 9 / (23 - 9)) + 9) - 23'
}
  
def main():
  arg = ''.join(sys.argv[1:])
  input_expr = test_strings[arg] if test_strings.get(arg) else arg
  demo('INPUT', input_expr)
  paren_tree = ParenTree(input_expr)
  demo('PAREN TREE RESULT', paren_tree)
  # op_tree = OperationsTree(input_expr)
  # for x in op_tree.root.values:
  #   print(x)


if __name__ == '__main__':
  main()