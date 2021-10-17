x = int(input('Number: '))
y = 1
li = []
while x > y + 1:
    y += 1
    if x % y == 0:
        print(str(x) + ' is not a prime number')
        quit()
else:
    print(str(x) + ' is a prime number')
    quit()