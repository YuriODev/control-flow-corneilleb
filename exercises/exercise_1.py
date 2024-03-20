# Your solution to Exercise 1

Alex = int(input())
Tatyana = int(input())

output = ""

if Alex > Tatyana:
  output = "Alex is the eldest"
elif Tatyana > Alex:
  output = "Tatyana is the eldest"
else:
  output = "Alex and Tatyana are of the same age."

print(output)