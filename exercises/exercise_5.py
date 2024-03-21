# Your solution to Exercise 5

a = int(input())
b = int(input())
c = int(input())

n_roots = 0

if (b**2 - 4ac) > 0:
  n_roots = 2
elif (b**2 - 4ac) == 0:
  n_roots = 1

