def fibonacci(n):
    if n == 0 or n == 1:
        return n 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def Fibonacci(n):
    num1, num2 = 0, 1
    result, i = 0, 0
    while i <= n:
        result = num1 + num2 
        print(result)
        num1 = num2
        num2 = result
        i += 1

print(Fibonacci(5)) # I don't know why it shows "None" as a final result
print(fibonacci(5))
    