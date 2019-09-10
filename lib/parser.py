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
          accum.append(char)
          return inner(char_list, accum)
        else:
          section += char
      if len(section):
        accum.append(section)
      return accum
    return inner(cleaned, [])
