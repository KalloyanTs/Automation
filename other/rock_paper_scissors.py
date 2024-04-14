import random
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
        #print(choice)
        if choice:
            return choice
        else:
            print(f"Incorrect choice, please enter a correct choice(r, s or p).")

def comp_choice():
    return game_options.get(random.choice([x for x in game_options]))

def winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == 'scissors' and computer == 'paper') or (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock'):
        return "Congratulations, you Win!"
    else:
        return "Sorry, you lose!"

def main():
    user = user_choice()
    computer = comp_choice()
    print(f"Your choice is: {user} \n The computer rolled: {computer}! \n {winner(user, computer)}")

main()

