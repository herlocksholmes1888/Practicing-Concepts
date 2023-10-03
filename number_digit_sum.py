def sum_digits(x):
  if len(x) == 1:
    return int(x)
  else:
    for _ in x:
      return int(x[0]) + sum_digits(x[1:])

n = input("Write an interger number and let us show you the sum of its digits: ")
result = sum_digits(n)
print(result)
