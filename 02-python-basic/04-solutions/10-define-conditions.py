s = "Knb423Lo12"
x = -12
y = 15

condition_1 = s == "Knb423Lo12"
condition_2 = (x > 100 or x < 20) and x % 3 == 0
condition_3 = (10 <= y <= 20) and y % 7 != 0

print(f'Is s == "Knb423Lo12"? {condition_1} (s has the value {s})')
print(f'Is the value of x either greater than 100 or less than 20 and divisible by 3? '
      f'{condition_2} (x has the value {x})')
print(f'Is the value of y between 10 and 20 and must not be divisible by 7? '
      f'{condition_3} (y has the value {y})')
