# Your solution to Exercise 13

number = int(input("Enter a number: "))

digit_1 = number // 1000
digit_2 = (number // 100) % 10
digit_3 = (number // 10) % 10
digit_4 = number % 10

print(digit_1 != digit_2 and digit_1 != digit_3 and digit_1 != digit_4 and digit_2 != digit_3 and digit_2 != digit_4 and digit_3 != digit_4)