import random
min = 1
max = 6

num = 1

win1 = 1
win2 = 1

roll_again = "yes"

print ("Rolling the dices Please")
print("___________________________")

while roll_again == "yes" or roll_again == "y":
      
    Player_1=random.randint(min, max)
    print ("Player1 = ",Player_1)

    Player_2=random.randint(min, max)
    print ("Player2 = ",Player_2)

    if(Player_1 > Player_2):
        print ("Player1 is Win!")
        win1=win1+1
    elif(Player_1 < Player_2):
        print ("Player2 is Win!") 
        win2=win2+1
    else:
       while Player_1 == Player_2:  
           Player_1=random.randint(min, max)
           print ("Player1 = ",Player_1)

           Player_2=random.randint(min, max)
           print ("Player2 = ",Player_2)  

           if(Player_1 > Player_2):
               print ("Player1 is Winner!")
               win1=win1+1
           elif(Player_1 < Player_2):
               print ("Player2 is Winner!")
               win2=win2+1 

    print("________________________")
    if(num == 5 ):
        if(win1>win2):
            print("Finally! Player1 is win!!")
        else:
           print("Finally! Player2 is win!!")  
        exit(0)
    num=num+1  

    roll_again = input("Roll the dices again?")

    print("________________________")
    print("________________________")