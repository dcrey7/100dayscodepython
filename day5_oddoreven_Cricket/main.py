import random 


def player_computer_number():
    player_number=int(input("Choose a number from 0 to 6 : "))
    computer_number=random.randint(0, 6)
    return player_number,computer_number
    
def computer_toss():
    choice=['bat','bowl']
    computer_toss_choice=random.choice(choice)
    return computer_toss_choice
    
    
    
def toss():
    
    print('*********Welcome to Odd or even Cricket********* \n')
    overs=int(input("Enter number of overs: "))
    player_choice=input("Pick odd or even: ").lower()
    player_number,computer_number=player_computer_number()
    if (player_number+computer_number)%2==0 and player_choice== 'even':
        player_toss_choice=input("Player won toss, please pick bat or bowl: ")
    elif (player_number+computer_number)%2!=0 and player_choice== 'odd':
        player_toss_choice=input("Player won toss, please pick bat or bowl: ")
    else:
        computer_toss()
        computer_toss_choice=computer_toss()
        print(f"Computer won toss because it put {computer_number}. Computer chooses to {computer_toss_choice}")
        
        

    
        
        
        
        
    
    
    

