import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      'Rock vs Paper -> Paper wins\n'
      'Rock vs Scissors -> Rock wins\n'
      'Paper vs Scissors -> Scissors wins\n')

while True:
    print("Enter your choice:\n1 - Rock\n2 - Paper\n3 - Scissors\n")

    # Take the input from the user
    choice = int(input("Enter your choice: "))

    # Validate the user input
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please (1-3): "))

    # Map numeric choice to name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is:', choice_name)
    print("Now it's Computer's turn...")

    # Computer makes a random choice
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        print("<== It's a tie! ==>")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print("<== Paper wins! ==>")
        winner = 'User' if choice_name == 'Paper' else 'Computer'
        print(f"<== {winner} wins! ==>")
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("<== Rock wins! ==>")
        winner = 'User' if choice_name == 'Rock' else 'Computer'
        print(f"<== {winner} wins! ==>")
    else:
        print("<== Scissors wins! ==>")
        winner = 'User' if choice_name == 'Scissors' else 'Computer'
        print(f"<== {winner} wins! ==>")


    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")
