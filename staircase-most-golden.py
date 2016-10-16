any_in = lambda x, y: any(i in y for i in x)

def get_combos_wrapped():
  memo = {}
  def get_combos(results, total, numbers, partial=[], memo=memo):
    match = False
    # print("total: %s, partial: %s, numbers: %s" % (total, partial, numbers))
    sum_partial = sum(partial)
    remainder = total - sum_partial
    if remainder in memo:
      for lst in memo[remainder]:
        if not any_in(partial, lst):
          return lst + partial         

    s = sum(partial)

    if s == total: 
      print("match: %s" % partial)
      # memo[total].append(partial)
      match = True
      return match
    if s >= total:
      # memo[(len_partial, total)] = False
      return match
    for i in range(len(numbers)):
      n = numbers[i]
      remaining = numbers[i+1:]
      new_partial = partial + [n]
      match = get_combos(results, total, remaining, new_partial, memo) 
      if match:
        break
  return get_combos

get_combos = get_combos_wrapped()

class BrickStash:
  def __init__(self, num_bricks):
    self.num_bricks = num_bricks
    self.staircases = []
    self._get_combos = get_combos(self.staircases, self.num_bricks, range(1,self.num_bricks))

def answer(n):
  stash = BrickStash(n)
  return len(stash.staircases)

answer(17)
