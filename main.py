from random import randint
score = 0

print('''
====================================
  Welcome to the hexadecimal quiz!
====================================
''')

print('[1] For integer to hexadecimal conversions')
print('[2] For hexadecimal to integer conversions')
while True:
    mode_of_game_decision = input('>>> ').strip().replace('[','').replace(']','')

    if mode_of_game_decision == '1':

        while True:
            random_integer = randint(0,255)
            hex_random_integer = hex(random_integer).replace('0x','').upper()
            try:
                user_guess = input(f'What is {random_integer} in hexadecimal?: ').strip().upper()
                if user_guess == hex_random_integer:
                    print()
                    print(' >>> Congrats!!! You got it! <<<')
                    score += 1
                    if score == 5:
                        break
                    print(f'<<< Your score is now {score}, you need more {5-score} right guesses. >>>')
                    print()
                else:
                    print()
                    print(f'>>> Well... good guess, but actually it was {hex_random_integer} :( <<<')
                    print()
            except:
                print('Please, try again with a valid value!')
        break

    elif mode_of_game_decision == '2':

        while True:
            random_integer = randint(0,255)
            hex_random_integer = hex(random_integer).replace('0x','').upper()
            try:
                user_guess = input(f'What is "{hex_random_integer}" in integer?: ').strip().upper()
                if user_guess == str(random_integer):
                    print()
                    print(' >>> Congrats!!! You got it! <<<')
                    score += 1
                    if score == 5:
                        break
                    print(f'<<< Your score is now {score}, you need more {5-score} right guesses >>>')
                    print()
                else:
                    print()
                    print(f'>>> Well... good guess, but actually it was {random_integer} :( <<<')
                    print()
            except:
                print('Please, try again with a valid value!')
        break

    else: 
        print('Try again, that is not an option!')

print('''
===================================
  The game is over, you won it!!!
===================================
''')
