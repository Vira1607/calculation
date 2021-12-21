import math

def calculation(x):
  a = (math.sin(x)) ** 3 + x ** 4
  b = math.sqrt(x) - math.log(x)
  c = 4 * x - 5 * (x ** 3)
  h = a ** 3 + b ** 2 - 8 * c
  return h

enter = float(input('Введите x: '))
answer = calculation(enter)
print('h равняется', answer)

