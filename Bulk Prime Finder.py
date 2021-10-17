from tqdm import tqdm

a = int(input('Lower Range: '))
b = int(input('Upper Range: '))
y = 1
li = [2]
for num in tqdm(range(a, b + 1, 2)):
    for x in range(3, num):
        if num % x == 0:
            break


    else:
        li.append(num)


for item in li:
    max = li[0]
    if item > max:
        max = item

print('Prime Numbers: ' + str(li))
print('Max = ' + str(max))
quit()
