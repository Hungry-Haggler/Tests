# How many coincidences for each item in x.

# defining stage, having many different subsets.
import random
from tqdm import tqdm


x = int(input('Number: '))
y = int(input('Accuracy: '))
total = 0
mega_total = 0
mega_total1 = 0
mega_total2 = 0
mega_total3 = 0
mega_total4 = 0
mega_total5 = 0
mega_total6 = 0
mega_total7 = 0
mega_total8 = 0
mega_total9 = 0
more = 0
li = []

# begining of the nested loop. This will repeat the next loop Y amount of times for accuracy.
for number in tqdm(range(y)):
    total = 0

    # Main loop
    for item in range(x):
        random_1 = random.randint(1, x)
        random_2 = random.randint(1, x)
        if random_1 == random_2:
            total += 1
    if total > 9:
        more += 1
        mega_total += 1
        break
    if total == 9:
        mega_total9 += 1
        mega_total += 1

    if total == 8:
        mega_total8 += 1
        mega_total += 1

    if total == 7:
        mega_total7 += 1
        mega_total += 1

    if total == 6:
        mega_total6 += 1
        mega_total += 1

    if total == 5:
        mega_total5 += 1
        mega_total += 1

    if total == 4:
        mega_total4 += 1
        mega_total += 1

    if total == 3:
        mega_total3 += 1
        mega_total += 1

    if total == 2:
        mega_total2 += 1
        mega_total += 1

    if total == 1:
        mega_total1 += 1
        mega_total += 1

z = y / 100
print('Breakdowns:')
print('More than 9 coincidences: ' + str(more) + '/' + str(y) + ' or ' + str(more / z) + '%')
print('9 coincidences: ' + str(mega_total9) + '/' + str(y) + ' or ' + str(mega_total9 / z) + '%')
print('8 coincidences: ' + str(mega_total8) + '/' + str(y) + ' or ' + str(mega_total8 / z) + '%')
print('7 coincidences: ' + str(mega_total7) + '/' + str(y) + ' or ' + str(mega_total7 / z) + '%')
print('6 coincidences: ' + str(mega_total6) + '/' + str(y) + ' or ' + str(mega_total6 / z) + '%')
print('5 coincidences: ' + str(mega_total5) + '/' + str(y) + ' or ' + str(mega_total5 / z) + '%')
print('4 coincidences: ' + str(mega_total4) + '/' + str(y) + ' or ' + str(mega_total4 / z) + '%')
print('3 coincidences: ' + str(mega_total3) + '/' + str(y) + ' or ' + str(mega_total3 / z) + '%')
print('2 coincidences: ' + str(mega_total2) + '/' + str(y) + ' or ' + str(mega_total2 / z) + '%')
print('1 coincidence: ' + str(mega_total1) + '/' + str(y) + ' or ' + str(mega_total1 / z) + '%')

print("Coincidences: " + str(mega_total) + '/' + str(y))
print('Percentage of having at least 1 coincidence: ' + str(mega_total / z) + '%')

