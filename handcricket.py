"""This is a simple handcicket game logic
   *The game starts with the question of odd or even
   *you have to choose one of it
   *Then type a number between 1 - 6
   *Computer also generates a number
   *if the sum of two numbers is odd and if you choose odd ,you won the toss
   *if the sum of two nmbers is even and if you choose odd ,you lose the toss
   and the same thing for even also
   *If you won the toss, you have to decide what do you have to do..batting and chasing are the two options led for you
   *if you choose batting you have to type a number between 1 - 6,and the computer also generates number between 1 - 6
   *if your number and the computer number are same,you will be out, otherwise the scores added up
   *Then you have to bowl and the computer bats
   *if your number and computer generated number are same,then the computer is out
   *The computer can bat until to chase your score..you have to make it out before it chases otherwise it will wins
   *If you lose the toss,the computer will decides what you have to do
   and the rules will be the same..
   *Thats all from the comments..
   Enjoy cricket............."""




import random
def bowl():
    comscore = 0
    while True:
        combat = random.randint(1,6)
        try:
            bowl = int(input("bowl "))
        except:
            print("you not entered any input ")
            continue
        print("com = "+str(combat))
        if bowl != combat:
            comscore = comscore + combat
            print("comscore = "+str(comscore))
        else:
            print("com is out")
            print("comscore is "+str(comscore))
            print("you need "+str(comscore + 1)+" runs to win")
            break
    if comscore > 50:
        print("hard target to beat")
    elif comscore < 50:
        print("not a massive target to chase")
    else:
        print("easy target to win")
    score = 0
    while True:
        com = random.randint(1,6)
        try:
            bat = int(input("bat "))
        except:
            print("you are not entering any input")
            continue
        print("com = "+str(com))
        if bat == 1 or bat == 2 or bat == 3 or bat == 4 or bat == 5 or bat == 6:
            if bat != com:
                score = score + bat
                if score > comscore:
                    print("you've won")
                    break
                elif score < comscore:
                    print("your score = "+str(score))
                    print("You need "+str((comscore - score) + 1)+" runs to win")
                else:
                    print("the score are equal")
                    print("your score = "+str(score))
            else:
                if score < comscore:
                    print("you lose the game")
                    break
                elif score == comscore:
                    print("match tied")
                    break
                else:
                    pass
        else:
            print("enter only between 1 - 6")
                    
                    
                
def bat():
    score = 0
    while True:
        com = random.randint(1,6)
        try:
            user = int(input("bat "))
        except:
            print("please enter an input")
            continue
        print("com = "+str(com))
        if user == 1 or user == 2 or user == 3 or user == 4 or user == 5 or user == 6:
            if user == com:
                print("you're out")
                break
            else:
                score = score + user
                print("your score is "+str(score))
        else:
            print("Type only between 1 - 6")
        
    print("your score is "+str(score))
    print("com needs "+str(score + 1)+" runs to win")
    if score > 50:
        print("hard target to beat for com")
    elif score < 50:
        print("not a massive target to beat for com")
    else:
        print("very easy target to beat")

    comscore = 0
    while True:
        combat = random.randint(1,6)
        try:
            bowl = int(input("bowl "))
        except:
            print("Please enter the correct input")
            continue
        print("com = "+str(combat))
        
        if bowl != combat:
            comscore = comscore + combat
            if comscore > score:
                print("you've lost")
                break
            elif comscore < score:
                
                print("comscore = "+str(comscore))
                print("Com needs "+str((score - comscore) + 1)+ " runs to win")

            elif comscore == score:
                print("the score are equal")
            else:
                pass
        else:
            if comscore < score:
                print("you've won")
                break
            elif comscore == score:
                print("match tied")
                break
            else:
                pass


try:      
        t = "null"    
        toss = input("odd or even?? ")
        while True:        
                if toss != "even" and toss != "odd":
                        print("it's neither odd nor even..check the input.progran terminating")
                        toss = input("odd or even?? ")
                else:
                        break
                
        comtoss = random.randint(1,6)
        usertoss = int(input("Type a number "))
        print("com = "+str(comtoss))
        sum = comtoss + usertoss
        sum1 = sum % 2
        if sum1 == 0:
                if toss == "even":
                        
                        t = "won"
                else:
                        t = "lose"
        else:
                if toss == "odd":
                        t = "won"
                else:
                        t = "lose"
        if t == "won":
                print("Well,you've won the toss")
                decide = int(input("what do you decided?? Batting - 1 or Bowling - 2 "))
        else:
                print("you lose the toss")
                print("com decides to bowl")
                bat()
        if decide == 1:
                bat()
        elif decide == 2:
                bowl()
        else:
            pass        
except:
        print("Play again to create records...")
        print("The world is awaiting you!!")
