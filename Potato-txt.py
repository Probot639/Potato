# Potato
import random
import time

name = input('Hello Stranger, what name haveth you?:')
print("Hello " + name + ", welcome to Potato. \n \n you are a halfling, just trying to exist. \n Meanwhile, the dark "
                        "lord rampages across the world. \n You do not care about this, you are trying to farm "
                        "Potatoes. \n \n Because what could a halfling possibly do about it anyway?")
diff = input("What difficulty would you like to play on? \n[1]: easy mode \n[2]: medium mode \n[3]: hard mode \n[4]: "
             "Let the Wizarding Council choose for you\n:")

time.sleep(2.5)
if diff == '1':
    destiny = 0
    potatoes = 7
    orcs = 0
    potato_v_orc = 1
    print("You have chosen the easiest option. \nRest assured, you already have a stockpile of potatoes and enemies "
          "are few and far between.")
elif diff == '2':
    destiny = 0
    potatoes = 4
    orcs = 0
    potato_v_orc = 1
    print("You have chosen the medium option. \nYou have potatoes in your garden, but a few bad days can ruin you. "
          "\nGood luck!")
elif diff == '3':
    destiny = 2
    potatoes = 0
    orcs = 2
    potato_v_orc = 2
    print("This game is basically all chance. \nEverything is now stacked against you. \nStatistically you can win, "
          "but you will need to get really lucky. \nThe Wizarding Council wishes you the best, and will pretend to "
          "care about you should anything happen.")
elif diff == '4':
    destiny = random.randint(0, 5)
    potatoes = random.randint(0, 9)
    orcs = random.randint(0, 5)
    potato_v_orc = random.randint(1, 2)
    print("The Wizarding Council are a bit insane. \nThey have proliferated the surrounding area with a random "
          "assortment of resources, with which you must find your way. \nThis is either an easy win or a horrible "
          "loss, either of which they will look at for entertainment purposes. \nGood luck, lets hope they were kind "
          "this time!")
else:
    destiny = random.randint(0, 9)
    potatoes = random.randint(0, 9)
    orcs = random.randint(0, 9)
    potato_v_orc = random.randint(1, 9)
    print("You have entered a difficulty that the Wizarding Council keeps in secret, as it is in another language. We "
          "don't know what this means, but they certainly do. Lets hope the translator was feeling generous, "
          "because if not you're not going to last very long...")


# Gameplay loop:
# * roll grass and mud
# * check if you have potatoes and ask if you want to Hurl
# * roll either "In The Garden" or "A knock at the door"
# * check iff you have potatoes and ask if you want to Hurl
# * Check to see if you meet an ending condition

# roll gameplay loop
# Hurl y/n

def gameplay_loop():
    global potatoes
    global destiny
    global orcs
    global potato_v_orc
    if potatoes <= orcs:
        print("Lets find out where you are on this morning...")
    elif potatoes > orcs:
        print("Lets find out where you are on this fine morning!")
    location = random.randint(1, 3)
    dieRoll = random.randint(1, 6)
    time.sleep(2.5)
    if location == 1:
        print("You are in the Garden!")
        time.sleep(2.5)
        if dieRoll == 1:
            print("You happily root about all day in your garden. You harvest 1 potato!")
            potatoes += 1
        elif dieRoll == 2:
            print("You narrowly avoid a visitor by hiding in a potato sack. You find an extra potato, but your "
                  "destiny calls just a bit louder...")
            potatoes += 1
            destiny += 1
        elif dieRoll == 3:
            print("A hooded stranger lingers outside your farm. Your destiny whispers to you, and orcs become more "
                  "prevalent in the area. ")
            destiny += 1
            orcs += 1
        elif dieRoll == 4:
            print("Your field is ravaged in the night by unseen enemies. Some of them stick around in the area, "
                  "and you lose a potato in the night.")
            orcs += 1
            if potatoes > 0:
                potatoes -= 1
        elif dieRoll == 5:
            print("You trade potatoes for other delicious foodstuffs. While delicious for the evening, that food "
                  "doesn't last as long as potatoes would have...")
            if potatoes > 0:
                potatoes -= 1
        elif dieRoll == 6:
            print("You burrow into a bumper crop of potatoes. Do you cry with joy? Possibly.")
            potatoes += 2
    elif location == 2:
        print("You hear a knock at the door...")
        time.sleep(2.5)
        if dieRoll == 1:
            print("It is a distant cousin. They are after your potatoes. They may snitch on you. Enemies become more "
                  "plentiful.")
            orcs += 1
        elif dieRoll == 2:
            print("A dwarven stranger. You refuse them entry. Ghastly creatures. But whatever spell they left behind "
                  "whispers to you in the quietest points of the night...")
            destiny += 1
        elif dieRoll == 3:
            print("A wizard strolls by. You pointedly draw the curtains. An orc must have followed them into the "
                  "area, and the wizard's powers try and pull you to an adventure...")
            orcs += 1
            destiny += 1
        elif dieRoll == 4:
            print("There are rumors of war in the reaches. You eat some potatoes.")
            if potatoes > 0:
                potatoes -= 1
            orcs += 2
        elif dieRoll == 5:
            print("It's an elf. They are not serious people. Your destiny calls to you from their arrogant pointed "
                  "ears.")
            destiny += 1
        elif dieRoll == 6:
            print("It's a sack of potatoes from a generous neighbor. You really must remember to pay them a visit one "
                  "of these years.")
            potatoes += 2
    elif location == 3:
        print("The world has become a darker, more dangerous place. Orcs are more tenacious, and it will take more "
              "potatoes to remove them from your garden. Good luck...")
        time.sleep(2.5)
        potato_v_orc += 1
    if (potatoes >= potato_v_orc) & (orcs > 0):
        print("There are", orcs, "Orcs in your garden, and you have", potatoes, "potatoes. Would you like to Hurl",
              potato_v_orc, "Potatoe(s) at them?")
        ynbool = input('y/n: ')
        if ynbool == 'y':
            potatoes -= potato_v_orc
            orcs -= 1
        elif ynbool == 'Y':
            potatoes -= potato_v_orc
            orcs -= 1
        elif ynbool == 'n':
            pass
        elif ynbool == 'N':
            pass
        else:
            print("You have tried to do something not ever meant to be done with Potatoes. The Wizarding council has "
                  "intervened and there will be no [REDACTED] at this time.")
    elif (potatoes >= potato_v_orc) & (orcs == 0):
        print("\nCongratulations, " + name + ", there are no Orcs in your garden, you can continue living your happy "
                                             "little life!")
        input("Press [ENTER] to continue")
    else:
        print("\nI'm sorry " + name + ", you do not have enough potatoes to dissuade an orc from sticking around. You "
                                      "can do nothing as of now...")
        input("Press [ENTER] to continue")
    print("You have", potatoes, "potatoes, " + "There are", orcs, "Orcs in your garden, and your destiny is at",
          10 * destiny, "percent...")


def scoreCheck():
    if orcs >= 10:
        print("\nOrcs finally find your potato farm. Alas, orcs are not so interested in potatoes as they are in eating"
              " you, and you end up in a cook-pot.")
        return 1
    elif (destiny == 10) & (orcs < 10):
        print("\nAn interfering Bard or Wizard turns up at your doorstep with a quest, and you are whisked away against"
              " your will on an adventure.")
        return 1
    elif (destiny < 10) & (orcs < 10) & (potatoes >= 10):
        print("\nYou have enough potatoes that you can go underground and not return to the surface until the danger is"
              " past. You nestle down into  you burrow and enjoy your well earned rest!")
        return 1


while (orcs < 10) & (potatoes < 10) & (destiny < 10):
    gameplay_loop()
    if scoreCheck() == 1:
        break
    else:
        pass
