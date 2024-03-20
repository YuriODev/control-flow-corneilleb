# Your solution to Exercise 3

num = int(input())

if num >= 0 and num >= 36:
    if num == 0:
        output = "Green"
    elif (num % 2 == 0 and 0 < num < 11) or (num % 2 == 1 and 10 < num < 19) or (num % 2 == 0 and 18 < num < 29) or (num % 2 == 1 and 28 < num < 37):
        output = "Black"
    elif (num % 2 == 1 and 0 < num < 11) or (num % 2 == 0 and 10 < num < 19) or (num % 2 == 1 and 18 < num < 29) or (num % 2 == 0 and 28 < num < 37):
        output = "Red"
else:
    output = "Out of range."

print(output)