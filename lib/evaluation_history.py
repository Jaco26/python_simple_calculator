class EvaluationHistoryNode:
  def __init__(self, evaluation_id, left_id, right_id, result):
    self.evaluation_id = evaluation_id
    self.left_id = left_id
    self.right_id = right_id
    self.result = result

  def __repr__(self):
    return str(self.result)

    

class EvaluationHistory:
  def __init__(self):
    self.count = 0 # unique id for each evaluation
    self.evaluated = {} # adjacency list with EvaluationNode.id as key and list of EvaluationTrackerNodes as value

  def __repr__(self):
    return f'EvalHistory {self.evaluated}'

  def add(self, left, right, result):
    self.count += 1

    node = EvaluationHistoryNode(self.count, left.id, right.id, result)

    if left.id not in self.evaluated:
      self.evaluated[left.id] = []

    if right.id not in self.evaluated:
      self.evaluated[right.id] = []
    

    self.evaluated[left.id].append(node)
    self.evaluated[right.id].append(node)

    # update old history nodes that include either left.id or right.id with result
    for key in self.evaluated:
      for prev_node in self.evaluated[key]:
        new_node_ids = [left.id, right.id]
        if prev_node.left_id in new_node_ids or prev_node.right_id in new_node_ids:
          prev_node.result = result
  
  
  def most_recent(self, eval_node):
    if eval_node.id in self.evaluated:
      return self.evaluated[eval_node.id][-1].result
    return eval_node.value
    