import random
print("WELCOME TO 'GUESS THE NUMBER'!")
number_to_guess = random.randint(1, 100)
user_guess = None
attempts = 0
print("""i have selected a number between 1 and 100.
    Try to guess the number.
    I will tell you if your guess is too low or too high.""")
while user_guess != number_to_guess:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess < number_to_guess - 10:
            print("Too low! Try again.")
        elif user_guess > number_to_guess + 10:
            print("Too high! Try again.")
        elif user_guess < number_to_guess:
            print("low! Try again.")
        elif user_guess > number_to_guess:
            print("high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {number_to_guess} in {attempts} attempts.")
   