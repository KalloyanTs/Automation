import random

def game():
    print("Hi, this is a rock, paper and scissors game!\nPlease give your input below\nFor short you can use: \nr for rock\np for paper\ns for scissors\n ")
    game_options = {
        's' : 'scissors',
        'r' : 'rock', 
        'p' : 'paper',
        'scissors' : 'scissors',
        'rock' : 'rock',
        'paper' : 'paper'
        }
    def user_choice():
        while True:
            user_input = str(input("Input: "))
            choice = game_options.get(user_input)
            if choice:
                return choice
            else:
                print(f"Incorrect choice, please enter a correct choice(r, s or p).")

    def comp_choice():
        return game_options.get(random.choice([x for x in game_options]))
    
    def winner(user, computer):
        if user == computer:
            return "\nIt's a Tie!"
        elif (user == 'scissors' and computer == 'paper') or (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock'):
            return "\nCongratulations, you Win!"
        else:
            return "\nSorry, you lose!"
    
    user = user_choice()
    computer = comp_choice()
    print(f"Your choice is: {user} \nThe computer rolled: {computer}! \n {winner(user, computer)}")
    
    end_input = input("\nWould you like to play again?(y): ")
    if end_input in ['yes', 'y']:
        game()
    else: 
        print("\nTerminating")
        exit()
game()