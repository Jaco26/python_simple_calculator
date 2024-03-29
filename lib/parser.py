from constants import *

class Parser:
  def parse_expression(self, exp: str):
    cleaned = list(exp.replace('\t', '').replace('\n', '').replace(' ', ''))
    def inner(char_list: list, accum: list):
      section = ''
      while len(char_list):
        char = char_list.pop(0)
        if char in OPERATORS:
          if len(section):
            accum.append(section)
          if char == MULTIPLY and len(char_list) and char_list[0] == MULTIPLY:
            char += char_list.pop(0) # and this is how we properly parse the EXPONENT operator...
          elif char == LEFT_PAREN: 
            if len(accum):
              if accum[-1] not in OPERATORS or accum[-1] == RIGHT_PAREN:
                # if the item to the left of a LEFT_PAREN is not an operator or it's a RIGHT_PAREN
                # assume the desired operation is MULTIPLY
                accum.append(MULTIPLY)
          accum.append(char)
          return inner(char_list, accum)
        else:
          section += char
      if len(section):
        accum.append(section)
      return accum
    return inner(cleaned, [])
