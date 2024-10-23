import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_limit = 1
    upper_limit = 100
    
    # Generate a random number between the lower and upper limits
    number_to_guess = random.randint(lower_limit, upper_limit)
    
    # Number of guesses the player has
    max_guesses = 7
    attempts = 0
    
    print(f"I have selected a number between {lower_limit} and {upper_limit}.")
    print(f"You have {max_guesses} attempts to guess it.")

    # Loop until the player guesses the number or runs out of attempts
    while attempts < max_guesses:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Increase the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
            break
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")
    
    # If the player runs out of guesses
    if attempts == max_guesses and guess != number_to_guess:
        print(f"Sorry, you've run out of attempts! The correct number was {number_to_guess}.")

# Main program starts here
if __name__ == "__main__":
    number_guessing_game()
