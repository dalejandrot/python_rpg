import random

class Enemy:

    hp=200

    def __init__(self,atkl,atkh):
        self.atkl=atkl
        self.atkh=atkh

    def getAtk(self):
        print("atk is", self.atkl)

    def getHP(self):
        print("HP is", self.hp)
    

enemy1 = Enemy(40,49)
enemy1.getAtk()
enemy1.getHP()

enemy2 = Enemy(40,49)
enemy2.getAtk()
enemy2.getHP()
