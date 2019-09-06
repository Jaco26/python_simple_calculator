
def split_str(string, accumulator):
  character_list = list(string.replace('\n', '').replace('\t', '').replace(' ', ''))
  no_bump_ups = ['(', ')', '*', '**', '/', '+', '-']
  def inner(char_list, accum):
    section = ''
    while len(char_list):
      char = char_list.pop(0)
      if char in no_bump_ups:
        if len(section):
          accum.append(section)
        accum.append(char)
        return inner(char_list, accum)
      else:
        section += char
    if len(section):
      accum.append(section)
    return accum
  return inner(character_list, accumulator)



class CharList:
  def __init__(self, char_str):
    self.value = split_str(char_str, [])

  def __len__(self):
    return len(self.value)
  
  def __repr__(self):
    return str(self.value)

  def shift(self):
    if len(self.value):
      return self.value.pop(0)
    return None

  def consume(self, callback):
    while len(self.value):
      char = self.shift()
      callback(self, char)