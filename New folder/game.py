# filename should be hangman
import random

words = ["aman", "manas"]
chosen_word = random.choice(words)
word_length = len(chosen_word)
dashes = ["_"] * word_length
chances = 5
while chances>0:
    print(' '.join(dashes))
    print(f"You have {chances} chances left.")
        
        # Get user input
    guess = input("Guess a letter: ")
    if guess in chosen_word:
            # Update dashes with correct guesses
        for index, letter in enumerate(chosen_word):
                if letter == guess:
                    dashes[index]= guess
                    continue
    else:
        print("wrong guess sorry")
        chances= chances - 1
    if "_" not in dashes:
        print(f"Congratulations,You have won the game\n given word was: {chosen_word}")
        break
if "_" in dashes:
    print(f"sorry, you lost the game\n given word was: {chosen_word}")
