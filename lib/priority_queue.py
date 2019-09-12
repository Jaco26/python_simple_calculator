from constants import *

def determine_priority(operator, operator_index): 
  # smaller operator_index values mean the operator is closer to the left. important for ADD or SUBTRACT
  # and MULTIPLY or DIVIDE
  if operator == EXPONENT:
    p = 1
  elif operator == MULTIPLY or operator == DIVIDE:
    p = 2
  elif operator == ADD or operator == SUBTRACT:
    p = 3
  else:
    p = None
  return p, operator_index


class OperationNode:
  def __init__(self, operator='', operator_index=None, left='', right=''):
    self.operator = operator
    self.operator_index = operator_index
    self.left = left
    self.right = right

  def __repr__(self):
    
    left = self.left.value if hasattr(self.left, 'value') else self.left
    right = self.right.value if hasattr(self.right, 'value') else self.right
    operator = self.operator.value if hasattr(self.operator, 'value') else self.operator
    return f'OpNode [{left} {operator} {right}]'


class OperationQueue:
  def __init__(self):
    self.exponents = []
    self.multiply_divide = []
    self.add_subtract = []
  
  def __repr__(self):
    return f'OpQueue:\nexponents: {self.exponents}\nmult_div: {self.multiply_divide}\nadd_sub: {self.add_subtract}'

  def __len__(self):
    return len(self.exponents) + len(self.multiply_divide) + len(self.add_subtract)

  def find_where(self, callback):
    for op in self.exponents:
      if callback(op):
        return op
    for op in self.multiply_divide:
      if callback(op):
        return op
    for op in self.add_subtract:
      if callback(op):
        return op
    return None
    

  def enqueue(self, x: OperationNode):
    op = x.operator.value
    if op == EXPONENT:
      self.exponents.append(x)
      self.exponents = sorted(self.exponents, key=lambda x: x.operator_index)
    elif op == MULTIPLY or op == DIVIDE:
      self.multiply_divide.append(x)
      self.multiply_divide = sorted(self.multiply_divide, key=lambda x: x.operator_index)
    elif op == ADD or op == SUBTRACT:
      self.add_subtract.append(x)
      self.add_subtract = sorted(self.add_subtract, key=lambda x: x.operator_index)
    
  def dequeue(self):
    if len(self.exponents):
      return self.exponents.pop(0)
    elif len(self.multiply_divide):
      return self.multiply_divide.pop(0)
    elif len(self.add_subtract):
      return self.add_subtract.pop(0)
    return None

  