import random

print ("Welcome!  Pick an option between 'R', 'P' or 'S'")
def main():
    user_action = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    possible_action = ["R", "P", "S"]
    computer_action = random.choice(possible_action)

    if user_action in possible_actions:
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        if user_action == "R":
            if computer_action == "S":
                print("Rock smashes scissors! You win!")
            elif computer_action == "P":
                print("Paper covers rock! You lose.")
        elif user_action == "P": 
            if computer_action == "R":
                print("Paper covers rock! You win!")
            elif computer_action == "S":
                print("Scissors cuts paper! You lose.")
        elif user_action == "S":
            if computer_action == "P":
                print("Scissors cuts paper! You win!")
            elif computer_action == "R":
                print("Rock smashes scissors! You lose.")
    else:
        print("You've entered an invalid option!. Pls try again")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        main()
    else:
        print("Bye")
main()