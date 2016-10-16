any_in = lambda x, y: any(i in y for i in x)

def get_combos_wrapped():
  memo = {}
  def get_combos(total, numbers, partial=[], memo=memo):
    # print("total: %s, partial: %s, numbers: %s" % (total, partial, numbers))
    results = 0
    s = sum(partial)
    diff = total - s
    if s > total:
      # memo[(s, diff)] = False
      return results
    if (s, diff) in memo:
      # print("cache hit: %s, %s" % ((s, diff), memo[(s, diff)]))
      if memo[(s, diff)] == True:
        results += 1
      return results
    if s == total: 
      results += 1
      memo[(s, diff)] = True
      return results
    length = len(numbers)
    for i in range(length):
      n = numbers[i]
      remaining = numbers[i+1:]
      new_partial = partial + [n]
      results += get_combos(total, remaining, new_partial, memo)

    return results
  return get_combos

get_combos = get_combos_wrapped()

class BrickStash:
  def __init__(self, num_bricks):
    self.num_bricks = num_bricks
    self.staircases = 0
    self.staircases = get_combos(self.num_bricks, range(1,self.num_bricks))

def answer(n):
  stash = BrickStash(n)
  #return len(stash.staircases)
  return stash.staircases

for i in range(50):
  print("i: %d, answer: %s" % (i, answer(i)))
