DEMO = True

LEFT_PAREN = '('
RIGHT_PAREN = ')'
EXPONENT = '**'
MULTIPLY = '*'
DIVIDE = '/'
ADD = '+'
SUBTRACT = '-'

OPERATORS = [
  LEFT_PAREN,
  RIGHT_PAREN,
  EXPONENT,
  MULTIPLY,
  DIVIDE,
  ADD,
  SUBTRACT
]


def demo(header, item):
  if DEMO:
    print()
    print(header)
    print('-' * len(header))
    print(item)
    print()

def parser_error(message):
  print()
  print('[PARSER ERROR] -', message)
  print()