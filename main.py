import random

words = ['UMBRELLA', 'COMPUTER', 'TECHNOLOGY', 'SMARTPHONE', 'GRADUATION']
word = random.choice(words)

total_chances = len(word)
guessed_word = '-'*len(word)

while total_chances != 0:
    print(guessed_word)
    letter = input('Guess a letter: ').upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
                print(guessed_word)
        if guessed_word == word:
            print('\nCongratulation you won!')
            break
    else:
        total_chances -= 1
        print('Incorrect Guess')
        print(f'The remaining chances are: {total_chances}.')
else:
    print(f'\nGame Over. \nYou Lose. \nAll the chances are exhausted. \nThe correct word is: {word}.')
