from random import randint

from art import logo

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



# Function to Check user guess against actual answer
def check_answer (user_guess , actual_answer , turns):
    """" Check Answer against Guess , Returns the Number of Turns remaining. """
    if user_guess>actual_answer:
        print("*****Too High!! *******")
        return turns -1
    elif user_guess<actual_answer:
        print("*****Too Low!!********* ")
        return turns -1
    else:
        print(f" ****Congratulations !!! <3.*** You got it, the answer was {actual_answer}")


# Function to Set the difficulty
def set_difficulty():
    level = input("Choose a Difficulty Type.Type 'easy' or 'hard' : ")
    if level =="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choose a random number between 1 to 20
    print("Welcome to the number Gussing Game")
    print("I am thinking of Number Between 1 to 20")
    answer = randint(1, 20)
    print(f"Past , the correct answer is {answer}")

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        # Let the user Guess a Number
        guess = int(input("Make a guess : "))

        # Track The Number of turns and Reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns ==0:
            print("You have run out of guesses !! , You loss the Game.")
            return
        elif guess !=answer:
            print("guess Again. Wish You all the Best !!!")


game()