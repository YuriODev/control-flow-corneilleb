# Your solution to Exercise 2

age = int(input())

output = ""

if age <= 1:
  output = "Infant"
elif age < 13:
  output = "Child"
elif age < 20:
  output = "Teenager"
else:
  output = "Adult"

print(output)