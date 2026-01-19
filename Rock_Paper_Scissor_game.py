''' 
It's a Stone paper scissor game 
Rock for 1
Paper for 2
scissor for 3

'''

import random
import pyttsx3
engine = pyttsx3.init()
computer = random.choice([1,2,3])

a = input("Enter your choice::")
youDict = {"R":1, "P":2, "S":3}
reverseDict = {1:"Rock", 2:"Paper", 3:"Scissor"}

me = youDict[a]
print(f"You chose {reverseDict[me]}\nComputer chose {reverseDict[computer]}")

if(computer == me):
    print("Game is draw!")
    engine.say("Please Enter the number again")
    engine.runAndWait()

else:
    if(computer == 1 and me == 2):
        print("<!> You Win <!>")
        engine.say("Congratulations! Celebrations!")
        engine.runAndWait()
    elif(computer == 2 and me == 1):
        print("<!> You Loss <!>")
        engine.say("Ohhhh Shit ! Here we go again>>>")
        engine.runAndWait()
    elif(computer == 2 and me == 3):
        print("<!> You Win <!>")
        engine.say("Congratulations! Celebrations!")
        engine.runAndWait()
    elif(computer == 3 and me == 2):
        print("<!> You Loss <!>")
        engine.say("Ohhhh shittt! Here we go again>>>")
        engine.runAndWait()
    elif(computer == 1 and me == 3):
        print("<!> You Loss <!>")
        engine.say("Ohhh shitt! Here we go again>>>")
        engine.runAndWait()
    elif(computer == 3 and me == 1):
        print("<!> You win <!>")
        engine.say("Congratulations! Celebrations!")
        engine.runAndWait()
    else:
        print("Something went wrong!!")
        engine.say(":::You entered wrong number:::")
        engine.runAndWait()