import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,1,0])
yourstr=input("Enter your choice: ")
youDic={"s":1, "w":-1, "g":0}
reverseDic={1:"Snake", -1:"Water", 0:"Gun"}
you=youDic[yourstr]

# By now we have 2 numbers (variables), you and computer

print(f"You choose {reverseDic[you]}\nComputer choose {reverseDic[computer]}")

if(computer==you):
    print("Its a draw!")
else:
    '''
    if(computer==-1 and you==1):      #computer-you=-2
        print("You Win!")
    elif(computer==-1 and you==0):    #computer-you=-1
        print("You Lose!")
    elif(computer==1 and you==-1):    #computer-you=2
        print("You Lose!")
    elif(computer==1 and you==0):    #computer-you=1
        print("You Win!")
    elif(computer==0 and you==-1):    #computer-you=1
        print("You Win!")
    elif(computer==0 and you==1):    #computer-you=-1
        print("You Lose!")
    else:
        print("Something went wrong!")


        the below logic is written on the basis of the value of computer-you
    '''
    if((computer-you)==-2 or (computer-you)==1):
        print("You Win!")
    else:
        print("You Lose!")
