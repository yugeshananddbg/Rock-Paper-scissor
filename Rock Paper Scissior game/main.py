import random as r
l = ["Rock", "Paper", "Scissor"]
up = 0
cp = 0
print('Game Starts.............')
while True:
    up = 0
    cp = 0
    print('''
    1- Play
    2- Exit''')

    a=int(input('Enter Your choice :- '))

    if a==1:
        name = input("Enter your name :- ")
        for b in range(0,5):
            c=5-b
            print("Left Chance :- {}".format(c))
            inp = int(input('''Enter your choice
            1. Rock 
            2. Paper
            3. Scissor
            '''))
            if inp == 1:
                Uchoice="Rock"
            elif inp == 2:
                Uchoice="Paper"
            elif inp == 3:
                Uchoice="Scissor"
            else:
                print("Wrong Choice")
            print("Your choice is {}".format(Uchoice))
            Cchoice= r.choice(l)
            print("Computer choice is {}".format(Cchoice))
            if Uchoice==Cchoice:
                print("Draw")
                up= up+1
                cp= cp+1
                print('{} point is {} and Computer Point {}'.format(name,up, cp))
            elif(Uchoice=="Rock" and Cchoice=="Scissor") or (Uchoice=="Paper" and Cchoice=="Rock") or (Uchoice=="Scissor" and Cchoice == "Paper"):
                print("You won ")
                up=up+1
                print('{} point is {} and Computer Point {}'.format(name,up, cp))
            else:
                print("Computer won")
                cp=cp+1
        if up == cp:
            print("Finally Game Draw "
                  "{} Score is {}"
                  "Computer Score is {}".format(name,up,cp))
        elif up > cp:
            print("{} Won".format(name))
        else:
            print("Computer Won")
    elif a==2:
        break
    else:
        print("Invalid Choice")