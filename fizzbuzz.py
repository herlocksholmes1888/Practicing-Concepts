def fizz_buzz_game(n):
    numbers = []
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append("Fizz Buzz")
        elif i % 3 == 0:
            numbers.append("Fizz")
        elif i % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(i)
    return numbers
        
print(fizz_buzz_game(16))