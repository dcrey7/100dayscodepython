#all imports 
import hangman_art
import hangman_words
import random


def hangman():
    chosen_word=random.choice(hangman_words.word_list)
    chosen_word_len=len(chosen_word)
    lives=6
    end_of_game=False
    print(hangman_art.logo,"\n")
    
    display=[]
    for _ in range(chosen_word_len):
        display+="_"
    print(f"{' '.join(display)}","\n")
    
    while not end_of_game:
        
        guess=input('Guess your letter- ').lower()
        if guess in display:
            print('You have already guessed the letter')
        
        for position in range(chosen_word_len):
            letter=chosen_word[position]
            if guess==letter:
                display[position]=letter
                
        if guess not in chosen_word:
            print(f"Your letter {guess}, is not in the word. Please try again. You lose a life")
            
            lives-=1
            if lives==0:
                end_of_game=True
                print(f'You lose. The actual word is {chosen_word}')
                
        
        print(f"{' '.join(display)}")
        
                    
        if '_' not in display:
            end_of_game=True
            print('You win')
        
        print(hangman_art.stages[lives])
    
option='y'
while not option=='n':
  hangman()
  option=input("Do you want to play again? (y/n) ")