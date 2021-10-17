import random
li = []
li_2 = []

def split(secret):
        return [char for char in secret]


words = ['time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world', 'life', 'hand', 'part', 'child', 'eye',
        'woman','place', 'work', 'week', 'case', 'point', 'government', 'company', 'number', 'group', 'problem',
        'face']
guess_count = 10
secret = random.choice(words)
sliced = (split(secret))
sliced_amount = int(len(sliced))
for item in range(sliced_amount):
        li.append(' _ ')
print(''.join(li))

while guess_count > 0:
        guess_count -= 1
        guess = input('Guess: ')
        if guess == secret:
            print("'" + secret + "' Is correct! You Win!")
            quit()

        if guess in sliced:
            li_2.append(1)
            print('You Got It')
            index = sliced.index(guess)
            li[int(index)] = ' ' + guess + ' '
            print(''.join(li))

            if len(li_2) == len(li):
                print(secret + ' Is correct! You Win!')
                quit()
        else:
            if guess_count > 0:
                print('You Failed this round, Try Again')
else:
    print('You Lose! The correct answer was ' + str(secret))
    quit()

        

