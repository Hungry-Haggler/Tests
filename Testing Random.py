import random
x = int(input('Number: '))
y = int(input('Accuracy: '))
total = 0
mega_total = 0
li = []
for number in range(y):
    total = 0
    for item in range(x):
        random_1 = random.randint(1, x)
        random_2 = random.randint(1, x)
        if random_1 == random_2:
            total += 1
    if total > 0:
        mega_total += 1
z = y / 100
print("Coincidences: " + str(mega_total) + '/' + str(y))
print('Percentage: ' + str(mega_total / z) + '%')



