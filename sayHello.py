def sayHello(n):
    if n == 0:
        print("Goodbye!")
    else:
        print("Hello!")
        n -= 1
        sayHello(n)

n = int(input("How many times do you want to be greeted? "))
sayHello(n)