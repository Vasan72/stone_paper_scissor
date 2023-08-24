import random

def play():
    computer=random.choice(['r','s','p'])
    add=True
    while add:
        user=input("r for rock p for paper and s for scissor : ")
        if is_win(user,computer):
            add=False

        elif user==computer: 
            print('Tie')
        else:
            print("you lost")
    print('You Won')
    
def is_win(player,opponent):
    if (player =='r' and opponent=='s') or (player=='s' and opponent=='p') or (player == 'p' and opponent=='r'):
        return True
    
play()