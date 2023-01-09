from random import randint

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

# Print True or False
print("True or False? >", random == usernumber)
