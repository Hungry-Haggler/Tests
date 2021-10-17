# defining
y = int(input('Lower Input: ')) - 1
z = int(input('Upper Input: ')) + 1
if y + 1 > z - 1 or y < 5:
    print('Invalid input.')
    quit()
max1 = 0
mega_list = []
list = []
list2 = []
counter = 0
x = y
i = y
w = y - 1

# Double Loop for testing through each number in range, each number creates a list.
# The highest number in that list is calculated, and then that number is put into a "Mega List"


for num in range(y, z):
    w += 1

    while x >= 2:
      if x % 2 == 1:
         x = x * 3 + 1
         list.append(x)



      else:
          x = x / 2
          list.append(x)





    else:
        x = w
        i += 1
        total = len(list)
        mega_list.append(total)
        if total >= max1:
            max1 = total
            n = max1
        list.clear()


index = mega_list.index(n)
print('Longest Survivor in Range: ' + str(n) + ' At number: ' + str(index + y - 1))
quit()




