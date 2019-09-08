
from constants import OPERATORS

class CharListNode:
  def __init__(self, value):
    self.queued = False
    self.value = value

  def __repr__(self):
    return f'{self.value}(queued)' if self.queued else self.value


def split_str(string, accumulator):
  character_list = list(string.replace('\n', '').replace('\t', '').replace(' ', ''))
  def inner(char_list, accum):
    section = ''
    while len(char_list):
      char = char_list.pop(0)
      if char in OPERATORS:
        if len(section):
          accum.append(CharListNode(section))
        accum.append(CharListNode(char))
        return inner(char_list, accum)
      else:
        section += char
    if len(section):
      accum.append(CharListNode(section))
    return accum
  return inner(character_list, accumulator)


def create_simple_char_list(some_str):
  return [x.value for x in split_str(some_str, [])]


class CharList:
  def __init__(self, char_str):
    self._items = split_str(char_str, [])
    self._idx = 0

  def __iter__(self):
    return self

  def __next__(self):
    left = self.get(self._idx - 1)
    right = self.get(self._idx + 1)
    try: # we only want to stop if `item` is out of range...`left` and `right` should be None sometimes
      item = self._items[self._idx]
    except IndexError:
      raise StopIteration
    self._idx += 1
    return item, left, right

  def __len__(self):
    return len(self._items)
  
  def __repr__(self):
    return str(self._items)

  def get(self, index):
    if index > len(self) - 1 or index < 0:
      return None
    item = self._items[index]
    return item
  
  def get_slice(self, start, end=None):
    if not end:
      end = len(self) - 1
    if end < len(self):
      items_slice = ''.join([item.value for item in self._items[start:end]])
      return CharList(items_slice)
    return None

  def splice(self, start, end=None):
    if not end:
      end = len(self) - 1
    if end < len(self):
      spliced_values = ''.join([x.value for x in self._items[start:end]])
      self._items = [*self._items[:start], *self._items[end:]]
      return CharList(spliced_values)
    return None

  def shift(self):
    if len(self):
      return self.pop(0)
    return None
  
