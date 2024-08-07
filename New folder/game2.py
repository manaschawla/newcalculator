import random

words = ['python', 'programming', 'developer', 'challenge', 'hangman', 'example', 'guess', 'word', 'game', 'code']
    
    # Pick a random word
chosen_word = random.choice(words)
word_length = len(chosen_word)
dashes = ['_'] * word_length
chances = 5
    
print("Welcome to the Word Guessing Game!")
    
while chances > 0:
        # Display current state of dashes
    print(' '.join(dashes))
    print(f"You have {chances} chances left.")
        
        # Get user input
    guess = input("Guess a letter: ").lower()
        
        # Check if the guess is correct
    if guess in chosen_word:
            # Update dashes with correct guesses
        for index, letter in enumerate(chosen_word):
                if letter == guess:
                    dashes[index] = guess
    else:
            # Decrease chances if guess is incorrect
        chances -= 1
        
        # Check if the user has won
    if '_' not in dashes:
        print(f"Congratulations! You guessed the word: {chosen_word}")
        break
        
    # If out of chances
if '_' in dashes:
    print(f"Sorry, you lost. The word was: {chosen_word}")

play_again = input("Do you want to play again? (yes/no): ").lower()
while True:
    if play_again != 'yes':
        print("Thank you for playing!")
        break
        