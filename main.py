# Step 1
from random import randint

import hangman_words
from hangman_words import word_list


index = randint(0, len(hangman_words.word_list) - 1)
chosen_word = word_list[index]
print(chosen_word)

splitted_word = list(chosen_word)

display = []

length = len(chosen_word)


from hangman_art import logo
print(logo)

for i in range(length):
    display.append("_")
print(display)

end_game = False
lives = 6
while end_game is False:

    guess = input("Guess a letter: ").lower()


    for i in range(len(splitted_word)):
        if splitted_word[i] == guess:
            display[i] = guess
    if guess not in splitted_word:
        lives -=1
    if lives == 0:
        print("Game Over.")
        break
    if "_" not in display:
        print("YOU WON!")
        end_game = True
    print()
    print(display)

    from hangman_art import stages
    print(stages[lives])
#



