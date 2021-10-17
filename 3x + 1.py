


x = float(input('Number: '))
list = []
while x >= 2:
  if x % 2 == 1:
     x = x * 3 + 1
     final = list.append(x)



  else:
      x = x / 2
      final = list.append(x)





else:
        max = (list[0])
        for item in list:
            if item > max:
                max = item
        min = (list[0])
        for it in list:
            if it < min and it > 4:
                min = it

        total = 0
        for number in list:
            total += 1

        print(list)
        print('Max = ' + str(max))
        print('Min = ' + str(min))
        print('Total = ' + str(total))

        quit()









