import random
print("Task 1: Game King's Treasure")
def kings_treasure():
    try:
        coins = random.randint(1, 1000)
        print(f"Found {coins} gold coins.")
        team_size = int(input("Enter the number of people in your team: "))
        share = coins / team_size
        print(f"Each person gets {share} coins.")
    except ValueError:
        print("Incorrect input! Enter an integer.")
    except ZeroDivisionError:
        print("Division by zero is not possible!")
    finally:
        print("The adventure continues!")

print("Task 2: Game Safe Code")
def safe_code():
    secret_code = random.randint(100, 999)
    attempts = 5
    try:
        while attempts > 0:
            entered_code = int(input("Enter a three-digit code: "))
            attempts -= 1
            if entered_code == secret_code:
                print("Safe opened!")
                break
            elif entered_code < secret_code:
                print("Code is higher.")
            else:
                print("Code is lower.")
            print(f"Attempts left: {attempts}")
        else:
            print(f"Attempts exhausted. Safe code: {secret_code}")
    except ValueError:
        print("Incorrect input! Enter a number.")
print("Task 3: Game Rock-Paper-Scissors-Lizard-Spock")
def rock_paper_scissors_lizard_spock():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(choices)
    try:
        player_choice = input(f"Choose: {', '.join(choices)}: ").lower()
        if player_choice not in choices:
            raise ValueError("Incorrect choice!")

        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("Tie!")
        elif (player_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
             (player_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
             (player_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
             (player_choice == "lizard" and (computer_choice == "paper" or computer_choice == "spock")) or \
             (player_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock")):
            print("You win!")
        else:
            print("You lose!")
    except ValueError as e:
        print(e)
print("Task 4: Bonus Points System with Multipliers")
def bonus_points_system():
    try:
        points = int(input("Enter the number of points scored (0-100): "))
        if points < 0 or points > 100:
            raise ValueError("Incorrect input! Points must be between 0 and 100.")
        if points < 50:
            rating = "Beginner"
            multiplier = 1
        elif points < 70:
            rating = "Silver Player"
            multiplier = 1.5
        elif points < 90:
            rating = "Gold Player"
            multiplier = 2
        else:
            rating = "Platinum Player"
            multiplier = 3
        final_points = points * multiplier
        print(f"Your rating: {rating}! You received {final_points} points (multiplier ×{multiplier})!")
    except ValueError as e:
        print(e)
print("Task 5: Game Escape from Pirate Island")
def escape_from_pirate_island():
    try:
        wood = int(input("Enter the amount of wood for the raft (1-10): "))
        if wood < 3:
            raise ValueError("Not enough wood, the raft sank!")
        escape_choice = input("Choose an escape method (run, hide, fight): ").lower()
        if escape_choice not in ["run", "hide", "fight"]:
            raise ValueError("That option doesn't exist, the pirates caught you!")
        secret_code = random.randint(10,99)
        chest_code = int(input('Enter the two digit chest code: '))
        if chest_code != secret_code:
            raise ValueError('Incorrect code, the chest exploded!')
        print('The treasure is yours, you are saved!')

    except ValueError as e:
        print(e)
    finally:
        print('Game over. Thank you for participating in the adventure!')
kings_treasure()
safe_code()
rock_paper_scissors_lizard_spock()
bonus_points_system()
escape_from_pirate_island()