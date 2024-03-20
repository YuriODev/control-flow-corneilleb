# Your solution to Exercise 9

# integer = int(input('Enter an integer: '))

# digit_1 = integer // 100
# digit_2 = (integer // 10) % 10
# digit_3 = integer % 10

# sum = digit_1 + digit_3

# if sum > digit_2:
#     print('>')
# elif sum < digit_2:
#     print('<')
# else:
#     print('=')

3_digit = int(input())

sum_of_last_first = 3_digit // 100 + 3_digit % 10

middle_value = 3_digit // 10 % 10

if sum_of_last_first == middle_value:
  comparison = '='
elif sum_of_last_first >= middle_value:
  comparison = '>'
else:
  comparison = '<'

print(comparison)
