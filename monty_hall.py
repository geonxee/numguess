from random import choice


doors = ['door1', 'door2', 'door3']

iter_num = int(input('Enter some num(100-10000): '))

stay = 0
change = 0

for _ in range(iter_num):
    winning_door = choice(doors)
    select_door = choice(doors)
        
    if winning_door == select_door:
        stay += 1
    else:
        change += 1

stay_rate = round((stay/iter_num) * 100,2)
change_rate = round((change/iter_num) * 100,2)

print(f'{iter_num} times of simulation: {change} times win({change_rate}% change) {stay} times win({stay_rate}% stay)')
    
