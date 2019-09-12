import sys
import time
from constants import *
from lib import ParenTree, Parser

test_strings = {
  's1': '8.33*(1/  2.1 )',
  's2': '8 + (9 - 3 / (9 + 3))',
  's3': '12 + 3',
  's4': '3 * 9 / 34 - 9 * (9 + 7 )', # fail
  's5': '(9 + 8)/(8 * 2) + 9',
  's6': '(9 * (3 + 9 / (23 - 9)) + 9) - 23',
  's7': '3 + 8 * (4 - 2)',
  's8': '8**2',
  's9': '8 + 8 * 9 / (9 + (22 - 30) * (23 * 1.4))',
  's10': '4 + 5 * (3.44 / 5.22) * (9 / 3 * (8 + 3 - ((1.1 * 8) - 8)))',
  's11': '2 + 2 * (4 / 2) * (9 / 3 * (8 + 2 - ((2 * 8) - 6)))',
}

def test():
  successes = []
  failures = []
  for key in test_strings:
    parser = Parser()
    paren_tree = ParenTree()
    
    char_list = parser.parse_expression(test_strings[key])
    # print(char_list)

    # print(round(eval(''.join(char_list)), ))
    python_result = round(eval(''.join(char_list)), RESULT_ROUND_TO)
    print(python_result)

    paren_tree.parse_char_list(char_list)

    test_result = round(paren_tree.evaluate(), RESULT_ROUND_TO)

    if test_result == python_result:
      successes.append(test_strings[key] + ' = ' + str(test_result))
    else:
      failures.append({
        'key': key,
        'expression': test_strings[key],
        'test_result': test_result,
        'python_result': python_result
      })
  
  message = ''

  if len(failures):
    message += f'{len(failures)} FAILURES:\n\n'
    for fail in failures:
      print(fail)
      message += f"key:           {fail['key']}\n"
      message += f"expression:    {fail['expression']}\n"
      message += f"test result:   {fail['test_result']}\n"
      message += f"python result: {fail['python_result']}\n\n"
  
  if len(successes):
    message += f'{len(successes)} SUCCESSES:\n\n'
    for s in successes:
      message += s + '\n\n'

  return message


  
def main():
  parser = Parser()
  paren_tree = ParenTree()

  arg = ''.join(sys.argv[1:])

  if arg == 'test':
    result = test()
    demo('Test results:', result)
  else:
    input_expr = test_strings[arg] if test_strings.get(arg) else arg

    demo('RAW INPUT', input_expr)

    char_list = parser.parse_expression(input_expr)

    python_result = round(eval(''.join(char_list)), RESULT_ROUND_TO)

    # demo('PARSED INPUT', char_list)

    paren_tree.parse_char_list(char_list)

    # demo('PARSED PAREN TREE', paren_tree)

    result = round(paren_tree.evaluate(), RESULT_ROUND_TO)

    demo('RESULT', result)

    # demo('Result is valid', result == python_result)
    
    # demo('Python eval() result', python_result)



if __name__ == '__main__':
  main()

