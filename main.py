from models import CharList, PriorityQueue

LEFT_PAREN = '('
RIGHT_PAREN = ')'
EXPONENT = '**'
MULTIPLY = '*'
DIVIDE = '/'
ADD = '+'
SUBTRACT = '-'


test_strings = {
  's1': '8.33*(1/  2.1 )',
  's2': '8 + (9 - 3 / (9 + 3))',
  's3':'''this is the outside 
            (hello 
              (this is the 
                (most inner)
              )
              (what are you)
            )'''
}

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


def chomp_str():
  queue = PriorityQueue()
  char_list = CharList(test_strings['s1'])

  print(char_list)

  def consume_cb(lst: CharList, char):
    char_priority = get_priority(char)
    if char_priority == 2:
      

      queue.enqueue(paren_node, 1)
      # print(char, char_priority)
    
  char_list.consume(consume_cb)


chomp_str()

