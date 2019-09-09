from constants import *

class CharListNode:
  def __init__(self, value):
    self.value = value
    self.queued = False
  
  def __repr__(self):
    # return f'CharListNode {self.value + "(queued)" if self.queued else self.value}'
    return self.value

class CharList:
  def __init__(self, expression):
    cleaned = list(expression.replace('\n', '').replace('\t', '').replace(' ', ''))
    def parse(char_list, accum):
      section = ''
      while len(char_list):
        char = char_list.pop(0)
        if char in OPERATORS:
          if len(section):
            accum.append(CharListNode(section))
          accum.append(CharListNode(char))
          return parse(char_list, accum)
        else:
          section += char
      if len(section):
        accum.append(CharListNode(section))
      return accum

    self._items = parse(cleaned, [])
    self._idx = 0

  def __iter__(self):
    return self

  def __next__(self):
    try:
      item = self._items[self._idx]
    except:
      raise StopIteration
    self._idx += 1
    return item
  
  def __len__(self):
    return len(self._items)

  def get(self, index):
    if index < len(self) and index > -1:
      return self._items[index]
    return None

  def shift(self):
    if len(self):
      return self._items.pop(0)
    return None