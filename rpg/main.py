
from classes.game import Person, bcolors


magic=[{"name":"Fire","cost":10,"dmg":60},
       {"name":"Thunder","cost":12,"dmg":80},
       {"name":"Blizzard","cost":10,"dmg":60}]

player=Person(460,65,60,34,magic)
enemy=Person(1200,65,45,25,magic)

i=0

r=True

while r:
    print("=====================================")
    player.choose_action()
    choice=input("Choose action: ")
    index=int(choice)-1
    if index==0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ",dmg," points of damage.  Enemy HP:",enemy.get_hp())
    elif index==1:
        player.choose_magic()
        magic_choice=int(input("Choose magic:")) -1
        magic_dmg=player.generate_spell_damage(magic_choice)
    enemy_choice=1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ",enemy_dmg," points of damage.  Enemy HP:",player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN+"You Win!"+bcolors.ENDC)
        r=False
    elif player.get_hp() == 0:
        print(bcolors.FAIL+"Enemy has defeated you!"+bcolors.ENDC)
        r=False