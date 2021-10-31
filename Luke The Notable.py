import random
li = []
for item in range(100000):
    amount = 0
    for number in range(1, 15):
        event = random.randint(1, 40)
        if event == 1:
            amount += 1
        if amount > 2:
            li.append('1')
print(str(len(li)) + '/' + '10000')
print('Percentage: %' + str(len(li)/1000) + '/' + '100000')