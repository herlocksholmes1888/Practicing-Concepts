def checkIsDigit(i):
    if i.isdigit() == False:
        raise ValueError("You must write an interger number.")
    else:
        return int(i)

p = input("Write the first number: ")
p = checkIsDigit(p)

q = input("Write the second number: ")
q = checkIsDigit(q)