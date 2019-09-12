DEMO = True
RESULT_ROUND_TO = 8

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

def get_from(lst: list, index: int):
  try:
    return lst[index] if index > -1 else None
  except:
    return None

def parser_error(message):
  print()
  print('[PARSER ERROR] -', message)
  print()