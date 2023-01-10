from random import randint
from time import sleep


# Get username
username = input("Enter your name >")

# Greeting
print("Hi!" , username)

# random number
random = randint(1,100)

# Get user's number
usernumber = int(input("What's your guess? >"))

# Print user's number
print("Your guess is ", usernumber)

# Compare answer with user's guess
if usernumber == random:
    print("*******************")
    sleep(1)
    print("*******************")
    sleep(1)
    print("*******************")
    sleep(1)
    print(f'You got it right!! The answer is {random}!!')
elif usernumber > random:
    print(f'Keep going, man~! That was too high, {username}..')
elif usernumber < random:
    print(f'Keep going, man~! That was too low, {username}..')
