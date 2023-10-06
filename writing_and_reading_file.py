file = open("numbers_test.txt", "w")
for i in range(1, 11):
    file.write("%d\n" % i)
file.close()

read_file = open("numbers_test.txt", "r")
for i in read_file.readlines():
    print(i)
read_file.close()
