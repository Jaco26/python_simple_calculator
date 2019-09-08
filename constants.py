DEMO = True

LEFT_PAREN = '('
RIGHT_PAREN = ')'
EXPONENT = '**'
MULTIPLY = '*'
DIVIDE = '/'
ADD = '+'
SUBTRACT = '-'

OPERATORS = ['(', ')', '*', '**', '/', '+', '-']


def demo(header, item):
  if DEMO:
    print()
    print(header)
    print('-' * len(header))
    print(item)
    print()

