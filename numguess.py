from random import randint
from time import sleep
random = randint(1, 100)

def getname():
  username = input('Enter your name >')
  print(f'Hi! {username}')
  return username

def getnumber():
  usernumber = int(input("What's your guess? >"))
  print(f'Your guess is {usernumber}')
  return usernumber

def answer(random, usernumber):
  if usernumber == random:
    print("*******************")
    print(f'You got it right!! The answer is {random}!!')
    print('*******************')
  elif usernumber > random:
    print(f'Keep going, man~! That was too high..')
  elif usernumber < random:
    print(f'Keep going, man~! That was too low..')

username = getname()
usernumber = getnumber()
answer(random, usernumber)
