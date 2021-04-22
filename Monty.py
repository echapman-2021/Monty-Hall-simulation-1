import random
#-------Presentation(input/output)------------
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
    def first_choice():
        print(f"you have chosen {choice}",
              f"\nThe goat was behind door {goat}")
        print()
        print("Do you want to make a new choice?")
# -----------main body------------
IO.welcome()
user_choice = IO.input_choice()
try:
    if user_choice == 1:
        choice = "the first door"
        goat = random.randint(2,3)
        if goat == 2:
            other = "the third door"
            prize = random.randint(1,3)
            while prize == 2:
                prize = random.randin(1,3)
        else:
            other = "The second door"
    elif user_choice == 2:
        choice = "the second door"
        goat = random.randint(1,3)
        while goat == 2:    #FIXED?
            goat = random.randint(1,3)
        if goat ==1:
            other = "the third door"
            prize = random.randint(2,3)
        if goat == 3:
            other = "the first door"
            prize = random.randint(1,2)
    elif user_choice == 3:
        choice = "the third door"
        goat = random.randint(1, 2)
        if goat == 1:
            other = "the second door"
            prize = random.randint(2, 3)
        if goat == 2:
            other = "The first door"
            prize = random.randint(1, 3)
            while prize == 2:
                prize = random.randint(1,3)
except:
    print("try again")

IO.first_choice()
choice_again = IO.yes_or_no()
if choice_again.lower() == "yes":
    print(f"So you are choosing the {other}?")
    choice_again = IO.yes_or_no()
    if choice_again.lower() == "yes":
        print(f'this is what was behind {choice}')
        print(f'this is what was behind {other}')
    elif choice_again.lower() == "no":
        print(f'this is what was behind {choice}')
        print(f'this is what was behind {other}')
    else:
        print("try again")
else:
    print(f'this is what was behind {choice}')
    print(f'this is what was behind {other}')
