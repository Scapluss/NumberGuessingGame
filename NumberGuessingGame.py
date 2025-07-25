import random
number_to_guess = random.randint(1,100)
attempts = 0

while attempts < 10:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
    print()
    if attempts == 10 and guess != number_to_guess:
        print("*** Game over! Better luck next time! ***")