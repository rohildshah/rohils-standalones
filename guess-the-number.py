import time
from random import randint
number = (randint(0,100))
print("Hi, you have chosen Guess the number")
time.sleep(0.5)
print("The computer will generate a random number between 0-100")
time.sleep(0.5)
print("You have to guess that number by typing in your guess")
time.sleep(0.5)
print("If your number is too large, then the computer will say smaller, and the same vise versa")
time.sleep(0.5)
print("Let's start")
time.sleep(0.5)
a = 7
b = 7
while a == b:
    guess = input("Your guess:")
    guess = int(guess)
    if guess == number:
        print("You got it correct! Restart the program to play another game")
         return
    elif guess > number:
         print("Good guess, but smaller")
    elif guess < number:
        print("Good guess, but larger")

