import random
from random import choice

goat = "0"
# -------Presentation(input/output)------------
class IO:
    """Performs Input and Output Tasks"""

    @staticmethod
    def input_choice():
        """ Gets the choice from a user"""
        choice = int(input("Choose 1, 2, 3: "))
        return choice

    @staticmethod
    def welcome():
        print("Welcome to a Monty Hall style simulation! "
              "\n *based on the classic statistics problem")
        print()
        print("In front of you, there are 3 doors."
              "\n Behind one door is a goat,"
              "\n Behind another is a grand prize,"
              "\n And behind the other door is nothing")
        print()
        print("Please select 1 of 3 doors")

    @staticmethod
    def yes_or_no():
        yes_choice = input("yes or no: ")
        return yes_choice

    @staticmethod
    def first_choice(choice):
        print(f"you have chosen {choice}",
              f"\nThe goat was behind door {goat}")
        print()
        print("Do you want to make a new choice?")

    @staticmethod
    def prize_reveal(prize, other):
        print(f" The prize was located at door: {prize}")
        print("The door you chose was: ", other)
        other = int(other)
        if prize == other:
            print("You win!")
            print("The key to Monty's hall is that, by sticking with your original choice you would have only a "
                  "\n 1/3 chance of winning, but by choosing a new door, you have a 2/3rds chance of winning."
                  "\n That is to say, those who change their mind, win twice as as often as those who don\'t ")
        else:
            print("You Lose!")
            print()
            print("The key to Monty's hall is that, by sticking with your original choice you would have only a "
                  "\n 1/3 chance of winning, but by choosing a new door, you have a 2/3rds chance of winning."
                  "\n That is to say, those who change their mind, win twice as as often as those who don\'t ")
            print()
            print("but sadly, you still lost")

    @staticmethod
    def first_choice_reveal(choice, prize):  # test: adding choice as param
        print(f"The grand prize was located at door: {prize}")
        print("The door you chose was: ", choice)
        choice = int(choice)
        if prize == choice:
            print("You win!")
            print()
            print("The key to Monty's hall is that, by sticking with your original choice you would have only a "
                  "\n 1/3 chance of winning, but had you chosen a new door, you would have had a 2/3rds chance of winning."
                  "\n That is to say, those who change their mind, win twice as as often as those who don\'t ")
            print()
            print("But in this case, it worked in your favor")
        else:
            print("You Lose!")
            print()
            print("The key to Monty's hall is that, by sticking with your original choice you would have only a "
                  "\n 1/3 chance of winning, but had you chosen a new door, you would have had a 2/3rds chance of winning."
                  "\n That is to say, those who change their mind, win twice as as often as those who don\'t ")

    # -----------main body------------
IO.welcome()
user_choice = IO.input_choice()

if user_choice == 1:
    choice = "1"
    goat = random.randint(2, 3)
    if goat == 2:
        other = "3"
        exclude = 2
        prize = random.randint(1, 3)
        if prize == exclude:
            prize += 1
    else:
        other = "2"
        prize = random.randint(1, 2)
elif user_choice == 2:
    choice = "2"
    exclude = 2
    goat = random.randint(1, 3)
    if goat == exclude:
        goat =+ 1
    elif goat == 1:
        other = "3"
        prize = random.randint(2, 3)
    elif goat == 3:
        other = "1"
        prize = random.randint(1, 2)
elif user_choice == 3:
    choice = "3"
    goat = random.randint(1, 2)
    if goat == 1:
        other = "2"
        prize = random.randint(2, 3)
    if goat == 2:
        other = "1"
        exclude = 2
        prize = random.randint(1, 3)
        if prize == exclude:
            prize +=1

IO.first_choice(choice)
choice_again = IO.yes_or_no()
if choice_again.lower() == "yes":
    print(f"So you are choosing door {other}?")
    choice_again = IO.yes_or_no()
    if choice_again.lower() == "yes":
        IO.prize_reveal(prize, other)
    elif choice_again.lower() == "no":
        IO.first_choice_reveal(choice, prize)
    else:
        print("try again")
else:
    IO.first_choice_reveal(choice, prize)
