import random 


def player_computer_number():
    player_number=int(input("Choose a number from 0 to 6 : "))
    computer_number=random.randint(0, 6)
    return player_number,computer_number
    
def computer_toss():
    player_toss_choice=''
    choice=['bat','bowl']
    computer_toss_choice=random.choice(choice)
    if computer_toss_choice=='bat':
        player_toss_choice='bowl'
    else:
        player_toss_choice='bat'
    return computer_toss_choice,player_toss_choice
  
    
    
def toss():
    player_toss_choice=''
    computer_toss_choice=''
    print('*********Welcome to Odd or even Cricket********* \n')
    overs=int(input("Enter number of overs: "))
    player_choice=input("Pick odd or even: ").lower()
    player_number,computer_number=player_computer_number()
    if (player_number+computer_number)%2==0 and player_choice== 'even':
        player_toss_choice=input(f"Player won toss because computer put {computer_number}, please pick bat or bowl:  \n").lower()
        if player_toss_choice=='bat':
            computer_toss_choice='bowl'
        else:
            computer_toss_choice='bat'
    elif (player_number+computer_number)%2!=0 and player_choice== 'odd':
        player_toss_choice=input(f"Player won toss because computer put {computer_number}, please pick bat or bowl: \n").lower()
        if player_toss_choice=='bat':
            computer_toss_choice='bowl'
        else:
            computer_toss_choice='bat'
    else:
        computer_toss()
        computer_toss_choice,player_toss_choice=computer_toss()
        print(f"Computer won toss because it put {computer_number}. Computer chooses to {computer_toss_choice} \n")
    return computer_toss_choice,player_toss_choice,overs
        
        
def innings(innings_no=1,computer_toss_choice='',player_toss_choice='',target_score=0,overs=1):
    for i in range(1,3):
        innings_no=i    
        if innings_no==1:    
            final_score=0
            balls=overs*6
            print(f"*****{i} innings started, you are {player_toss_choice}ing and computer is {computer_toss_choice}ing*******  \n")
            if player_toss_choice=='bat':
        
                while balls>0:
                    player_number,computer_number=player_computer_number()
                    
                    balls-=1
                    if player_number==computer_number:
                        print(f"You are out because Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
                        break  
                    final_score+=player_number          
                    print(f"Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
            else:
   
                while balls>0:
                    player_number,computer_number=player_computer_number()
                    
                    balls-=1
                    if player_number==computer_number:
                        print(f"Computer is out because Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
                        break    
                    final_score+=computer_number        
                    print(f"Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
            computer_toss_choice,player_toss_choice=player_toss_choice,computer_toss_choice
            target_score=final_score
        
        elif innings_no==2:    
            final_score=0
            balls=overs*6
            
            print(f"*****{i} innings started, you are {player_toss_choice}ing and computer is {computer_toss_choice}ing, target score is {target_score+1}******* ")
            if player_toss_choice=='bat':

                while balls>0 :
                    player_number,computer_number=player_computer_number()
                    
                    balls-=1
                    if player_number==computer_number:
                        print(f"******GAME OVER. YOU LOSE******")
                        print(f"your score is {final_score} and computer score is {target_score}")
                        print(f"Computer put: {computer_number},balls left: {balls}, total score: {final_score}")

                        break
                    final_score+=player_number
                    if final_score>target_score:
                        print(f"******GAME OVER. YOU WIN******")
                        print(f'your score is {final_score} and computer score is {target_score}')        
                        print(f"Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
                        break
                    print(f"Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
    
            else:
                while balls>0:
                    player_number,computer_number=player_computer_number()
                    
                    balls-=1
                    if player_number==computer_number:
                        print(f"******GAME OVER. COMPUTER LOST*****")
                        print(f'Computer score is {final_score} and your score is {target_score}')        
                        print(f"Computer is out because Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
                        break 
                    final_score+=computer_number
                    if final_score>target_score:
                        print(f"******GAME OVER. COMPUTER WINS******")
                        print(f'Computer score is {final_score} and your score is {target_score}')         
                        print(f"Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
                        break
                    print(f"Computer put: {computer_number},balls left: {balls}, total score: {final_score}")
                    
            
                
computer_toss_choice,player_toss_choice,overs=toss()
innings(1,computer_toss_choice,player_toss_choice,0,overs)
            
        
        
    
        
        
        
        
    
    
    

