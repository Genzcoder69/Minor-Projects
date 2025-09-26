import random
import pyttsx3

engine = pyttsx3.init()
number = random.randint(1,10)
guess  = int(input("Guess any number from 1-10:"))

if guess == number:
    print("YOU WIN!")
    engine.say("congratulations!")
    engine.runAndWait()

else:
    print(f"YOU LOSS! The number was {number}")
    engine.say("game over!")
    engine.runAndWait()