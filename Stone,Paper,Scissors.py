'''AUTHOR=SEBIN PRINCE
DESCRIPTION:PRINT A PYHON PROGRAM OF STONE,PAPER,SCISSORS GAME

import random
while True:
    options=['Rock','Paper','Scissors']
    choice=(input("select rock,paper or scissors\nchoose:"))
    selection=random.choice(options)
    print("my choice:",choice)
    print("computer choice:",selection)
    if choice=='Rock' and selection=='Scissors':
        print("you win")
    elif choice=="Scissors" and selection=="Paper":
        print("you win")
    elif choice=='Paper' and selection=='Rock':
        print("you win")
    elif choice==selection:
        print("tie")
    else:
        print("lose")
      '''
