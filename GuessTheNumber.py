import random

# Generate a hidden number between 1 and 100
secret_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

while True:
    # Get user guess
    guess = int(input("Take a guess: "))
    
    # Check if the guess is high, low, or correct
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
        break  # Exit the loop
