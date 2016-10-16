def fact(n):
  if n == 1:
    return 1
  a = n* fact(n-1)
  print(a)
  return n * a
 
f = fact(5)
print(f)
