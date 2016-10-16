
def get_combos_wrapped():
    cache = {}
    def get_combos(numbers, idx, total, depth=0):
        # print(cache)
        # dstr = '\t' * depth
        # print("%scalled: idx=%s, total=%s" % (dstr, idx, total))
        if (idx, total) in cache:
          # print("cache hit: %s, %s" % (idx, total))
          to_return = cache[(idx, total)]
          del(cache[(idx, total)])
          return to_return
        depth += 1
        if idx >= len(numbers): 
          return 1 if total == 0 else 0
        the_sum =   get_combos(numbers, idx + 1, total, depth) \
                  + get_combos(numbers, idx + 1, total - numbers[idx], depth)
        # print("%sreturning %s" % (dstr, the_sum))
        cache[(idx, total)] = the_sum
        return the_sum
    return get_combos


def answer(n):
  get_combos = get_combos_wrapped()
  numbers = range(1,n)
  return get_combos(numbers, 0, n)


print(answer(200))
