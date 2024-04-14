import random
import sys
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

def winner(u_choice, c_choice):
    outcome = ""
    if u_choice == c_choice:
        outcome = "It's a Tie!"
        return outcome
    elif u_choice == 'scissors' and c_choice == 'paper':
        outcome = "Congratulations, you Win!"
        return outcome
    elif u_choice == 'scissors' and c_choice == 'rock':
        outcome = "Sorry, you lose!"
        return outcome
    elif u_choice == 'rock' and c_choice == 'paper':
        outcome = "Sorry, you lose!"
        return outcome
    elif u_choice == 'rock' and c_choice == 'scissors':
        outcome = "Congratulations, you Win!"
        return outcome
    elif u_choice == 'paper' and c_choice == 'scissors':
        outcome = "Sorry, you lose!"
        return outcome
    elif u_choice == 'paper' and c_choice == 'rock':
        outcome = "Congratulations, you Win!"
        return outcome

def main():
    u_choice = user_choice()
    c_choice = comp_choice()
    print(f"Your choice is: {u_choice} \n The computer rolled: {c_choice}! \n {winner(u_choice, c_choice)}")

main()

