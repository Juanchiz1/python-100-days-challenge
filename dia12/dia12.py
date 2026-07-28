#Scope Local and Global
from PIL.ImageChops import constant

if 3>2:
    a_variable=7

game_level=3

enemies=["skeleton","Zombie","Alien"]

def createEnemy():
    if game_level<5:
        new_enemy=enemies[0]

    print(new_enemy)

#Global Constant

PI=3.14
