import random

from art import logo
print(logo)

def number_guess_game():
    global attempts
    level = input("Welcome to the Number Guessing Game. I think of a number between 1 and 100. "
                      "Choose a difficulty. Type 'e' for Easy or 'h' for Hard.   ").lower()
    while level not in ["e", "h"]:
        level = input("Invalid input. Choose a difficulty. Type 'e' for Easy or 'h' for Hard.   ").lower()
    if level == "e":
        level_print = "EASY"
        attempts = 10
    elif level == "h":
        level_print = "HARD"
        attempts = 5
    print(f"Selected level: {level_print}")

    num_a_guess = random.randint(1, 100)

    def play_again():
        retry = input("Do you want to guess again? Input 'y' to guess, 'n' to quit.   ").lower()
        while retry not in ["y", "n"]:
            retry = input("Invalid input. Input 'y' to guess, 'n' to quit.   ").lower()
        if retry == "y":
            number_guess_game()
        elif retry == "n":
            print("Bye!")
            return

    def play_game(attempts):
        num = input(f"You have {attempts} attempts to guess the number. Make a guess: ")  
        while not num.isdigit():  
            num = input(f"Number to be input. You have {attempts} attempts to guess the number. Make a guess: ")
        num = int(num)  
        while num not in range(1,101):
            num = int(input(f"Number between 1 to 100 to be input. You  have {attempts} attempts to guess the number. Make a guess:   "))
        while attempts > 0:
            attempts -= 1
            if num_a_guess == num:
                print(f"Congrat! I thought of {num_a_guess}.")
                play_again()
                return
            elif attempts == 0:
                print(f"No more attempts remaining. I thought of {num_a_guess}.")
                play_again()
                return
            elif num_a_guess > num:
                num = int(input(f"It's TOO LOW. Guess again! You have {attempts} attempts remaining."
                                f"Make a guess:   "))
            elif num_a_guess < num:
                num = int(input(f"It's TOO HIGH. Guess again! You have {attempts} attempts remaining."
                                f"Make a guess:   "))

    play_game(attempts)

number_guess_game()
