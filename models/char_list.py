
operators = ['(', ')', '*', '**', '/', '+', '-']


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
      if char in operators:
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
  