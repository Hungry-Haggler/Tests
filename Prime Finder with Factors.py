x = int(input('Number: '))
y = 1
li = [str(x) + ' * ' + str(1)]
li_2 = []
while x > y + 1:
    y += 1
    if x % y == 0:
        z = x / y
        if int(y) in li_2:
            print(li)
            print('Number of Factors: ' + str(len(li) * 2))
            print(str(x) + ' is not a prime number')
            quit()
        y = int(y)
        z = int(z)
        li.append(str(z) + ' * ' + str(y))
        li_2.append(y and z)

else:
    print(li)
    print('Number of Factors: 2')
    print(str(x) + ' is a prime number')
    quit()
