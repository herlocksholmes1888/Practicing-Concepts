def checkIsDigit(i):
    if i.isdigit() == False:
        raise ValueError("You must write an interger number.")
    else:
        return int(i)
    
def checkGreatestCommonDivisor(a, b):
    if b == 0:
        return a
    else:
        return checkGreatestCommonDivisor(b, (a % b))

p = input("Write the first number: ")
p = checkIsDigit(p)

q = input("Write the second number: ")
q = checkIsDigit(q)

r = checkGreatestCommonDivisor(p, q)

print("The GCD between {} and {} is: {}!".format(p, q, r))