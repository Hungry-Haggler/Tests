import random
secret = random.randint(1, 50)
guess_count = 0
guess_limit = 5
guess_limit_2 = [1]
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret:
        print('You won!')

        break
    if secret in range(guess - 3, guess + 3):
        if len(guess_limit_2) == 1:
            print('You are very close, you receive one extra guess')
            guess_limit_2.clear()
            guess_limit += 1
        else:
            print('You are very close but will not receive another guess')
    if secret % guess == 0:
        print('I am a multiple of thee')
    if guess % secret == 0:
        print('I am a factor of thee')
    if guess > secret:
        print('I am fewer than thee')
    if guess < secret:
        print('I am greater than thee')


else:
    print(str(secret) + ' Was the correct number. You Lose!')