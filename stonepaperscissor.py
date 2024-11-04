import random
print("welcome to the game of stone,paper,scissors")
ych=input("enter a choice out of STONE, PAPER or SCISSORS")
ch=["stone",'paper','scissor']
cho=random.choice(ch)
print('player choice: ',cho)
if cho=='stone':
    if ych=='paper':
        print("you win")
    if ych=='scissor':
        print("you lose !")
if cho=='paper':
    if ych=='stone':
        print("you won")
    if ych=='scissor':
        print("you lose !")
            
if cho=='scissor':
    if ych=='stone':
        print("you won")
    if ych=='paper':
        print('you lose !')
        
if cho==ych:
    print("Its a Tie")

            

    
    
            