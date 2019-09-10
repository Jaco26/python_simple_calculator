import sys
from constants import demo
from lib import ParenTree, Parser

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
  's6': '(9 * (3 + 9 / (23 - 9)) + 9) - 23',
  's7': '3 + 8 * (4 - 2)',
}
  
def main():
  arg = ''.join(sys.argv[1:])
  
  input_expr = test_strings[arg] if test_strings.get(arg) else arg
  
  parser = Parser()
  paren_tree = ParenTree()

  char_list = parser.parse_expression(input_expr)

  demo('This is the python list of items in the input expression', char_list)

  paren_tree.parse_char_list(char_list)

  demo('This is the paren_tree after ParenTree.parse_expression', paren_tree)

  result = paren_tree.evaluate()

  demo('The result of ParenTree.evaluate', result)



if __name__ == '__main__':
  main()