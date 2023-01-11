from random import choice

doors = ['door1', 'door2', 'door3']

winning_door = choice(doors)
select_door = choice(doors)

stay = 0
change = 0

if winning_door == select_door:
    stay += 1
else:
    change += 1

