from random import randint

def rock_paper_scissor_game(user_input):

    visual = {1 : open('rock.txt').read(), 2 : open('paper.txt').read(), 3 : open('scissor.txt').read()}
    
    print("Your choice:")
    print(visual[user_input])
    print()
    
    print("Computer's choice:")
    computer_input = randint(1, 3)
    print(visual[computer_input])
        
    if user_input == computer_input:
        print("Tie")
    elif (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 3) or (user_input == 3 and computer_input == 1):
        print("You lose.")
    elif (user_input == 1 and computer_input == 3) or (user_input == 2 and computer_input == 1) or (user_input == 3 and computer_input == 2):
        print("You win.")

user_input = int(input("Where Rock=1, Paper=2, Scissors=3, input your choice as an integer: "))
rock_paper_scissor_game(user_input)