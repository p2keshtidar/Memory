"""
Memory
"""

import time
import random


__author__ = "7723278, Keshtidar"
_email__ = "pkeshtidar@gmail.com"


def emoj(nu):
    """

    param nu:
    return:
    """
    avatar = ""
    player_name = input("🧙 Player " + nu +
                        " ,What's your name : ").capitalize()
    gender = ""
    while gender not in ("M", "W"):
        gender = input("Enter Player " + nu + " gender (M/W): ").upper()
    if gender == "M":
        base = "x"
        while base not in ("A", "J", ""):
            base = input("🧙 Base on age=A or job=J or nothing: ").upper()
        if base == "A":  # base Age
            while True:
                age = input("🧙 How old are you player " + nu + "? ")
                if age.isdigit():  # make sure user give number
                    age = int(age)
                    break
                else:
                    print("🧙 Please enter a number")
                    continue
            if 4 < age < 25:
                avatar = boys["boy"]
            elif 25 <= age <= 50:
                avatar = boys["sir"]
            elif age > 50:
                avatar = boys["Opa"]
            else:
                avatar = boys["baby"]
        elif base == "J":  # base job
            job = "0"
            print("1:Student\n2:Astronaut\n3:Programmer\n4:Teacher"
                "\n5:Doctor\n6:Koch\n7:Police\n8:Artist\n9:Farmer"
                "\n10:mechanic")
            while job not in boys:
                job = input("Enter number of job: ")
            avatar = boys[job]
        else:
            avatar = boys["prinz"]
    if gender == "W":
        base = "y"
        while base not in ("A", "J", ""):
            base = input("🧙 Base on age=A or job=J or nothing: ").upper()
        if base == "A":  # base Age
            while True:
                age = input("🧙 How old are you player " + nu + " ? ")
                if age.isdigit():  # make sure user give number
                    age = int(age)
                    break
                else:
                    print("🧙 Please enter a number")
                    continue
            if age < 25:
                avatar = girls["girl"]
            elif 25 <= age <= 50:
                avatar = girls["lady"]
            elif age > 50:
                avatar = girls["Oma"]
            else:
                avatar = girls[baby]
        elif base == "J":  # base job
            job = "0"
            print("1:Student, 2:Astronaut, 3:Programmer, 4:Teacher, 5:Doctor" +
                  ", 6:Koch, 7:Police, 8:Artist, 9:Farmer, 10:mechanic")
            while job not in girls:
                job = input("Enter number of job: ")
            avatar = girls[job]
        else:
            avatar = girls["princess"]
    return player_name, avatar


def draw_grid(ls1):
    """

    param ls1:
    """
    for i in range(0, 4):
        for j in range(0, 5):
            print(ls1[i][j], end='  ')
        print('\r')
        continue


def card_pos(ls2, card):
    """

    param ls2:
    param card:
    return:
    """
    for i in ls2:
        if card in i:
            return ls.index(i), i.index(card)


def get_symbols(ls3, fn1, fn2):
    """

    param ls3:
    param fn1:
    param fn2:
    """
    for i in range(0, 4):
        for j in range(0, 5):
            if (i == fn1[0] and j == fn1[1]) or (i == fn2[0] and j == fn2[1]):
                print(CARDS[(5 * i) + j], end="  ")
            else:
                print(ls3[i][j], end="  ")
        print("\r")
        continue
    print("✨\n")


def take_cards(ls3, fn1, fn2):
    """

    :param ls3:
    :param fn1:
    :param fn2:
    """
    for i in range(0, 4):
        for j in range(0, 5):
            if i == fn1[0] and j == fn1[1]:
                ls3[i][j] = "  "
                if p == 1:
                    player1_cards.append(CARDS[i * 5 + j])
                else:
                    player2_cards.append(CARDS[i * 5 + j])
            elif i == fn2[0] and j == fn2[1]:
                ls3[i][j] = "  "
                if p == 1:
                    player1_cards.append(CARDS[i * 5 + j])
                else:
                    player2_cards.append(CARDS[i * 5 + j])
        print('\r')


# ------------------------------------------------------------------------------------
# Create a Avatar
boys = {"boy": "👦", "sir": "👨", "Opa": "👴", "prinz": "🤴",
        "1": "👨‍🎓", "2": "👨‍🚀", "3": "👨‍💻", "4": "👨‍🏫",
        "5": "👨‍⚕", "6": "👨‍🍳", "7": "👮‍",
        "8": "👨‍🎨", '9': "👨‍🌾", "10": "👨‍🔧", "baby": "👶"}
girls = {"girl": "👧", "lady": "👩", "Oma": "👵", "princess": "👸",
         "1": "👩‍🎓", "2": "👩‍🚀", '3': "👩‍💻", "4": "👩‍🏫",
         "5": "👩‍⚕", "6": "👩‍🍳", "7": "👮‍",
         "8": "👩‍🎨", "9": "👩‍🌾", "10": "👩‍🔧"}

# Define Main Story
print("I'm Gandalf🧙\nI have prepared a 🎁 gift for you:")
print("🎊Game's name: MEMORY🎊\n✨Story: ")
print("There are 20 Cards on the table\nI will show the Cards for 3 Seconds"
      "\n🪄Rules:\nEach player takes 2 Cards\n1.If the Cards were the same "
      ",They'll be removed from the table"
      "\n2.If the cards were not the same, I'll show them for 3 seconds to"
      " memorize cards location\n"
      "The winner is someone who takes more matched Cards\n and the loser "
      "should pay "
      "money to the winner at the End\nLet's Go!\n First let's make an "
      "Avatar for each player")

p1 = emoj("1")
player1 = p1[0] + " " + p1[1]
print("Welcome ", player1)
p2 = emoj("2")
player2 = p2[0] + " " + p2[1]
print("Welcome ", player2)
print("-----------------------------------")

# Define CARDS
CARDS = ["⚽", "⚽", "❄", "❄", "🌟", "🌟", "💘", "💘", "🎲", "🎲",
         "✂", "✂", "🚀", "🚀", "🎵", "🎵", "🌞", "🌞", "🎀", "🎀"]
ls = [['A1', 'B1', 'C1', 'D1', 'E1'],
    ['A2', 'B2', 'C2', 'D2', 'E2'],
    ['A3', 'B3', 'C3', 'D3', 'E3'],
    ['A4', 'B4', 'C4', 'D4', 'E4']]

random.shuffle(CARDS)
player1_cards = []
player2_cards = []

cnt = 0
p = 0
for x in range(1, 21):
    print(CARDS[x - 1], end="  ")
    if x % 5 == 0:
        print("\r")
        continue
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
for _ in range(0, 30):
    print("✨\n")

# Set cards on table
b = 20
draw_grid(ls)

while b != 0:
    cnt += 1
    if p == 0:
        while True:
            pos1 = input(f"{player1} 1.card : ").capitalize()
            fnd1 = card_pos(ls, pos1)
            if fnd1 is None:
                print("Sorry, doesn't exist  . "
                      "Take another card !")
                continue
            else:
                break
        while True:
            pos2 = input(f"{player1} 2.card : ").capitalize()
            fnd2 = card_pos(ls, pos2)
            if fnd2 is None:
                print("Sorry, doesn't exist  . "
                      "Take another card !")
                continue
            else:
                break
        get_symbols(ls, fnd1, fnd2)
        if CARDS[fnd1[0] * 5 + fnd1[1]] == CARDS[fnd2[0] * 5 + fnd2[1]]:
            take_cards(ls, fnd1, fnd2)
            b -= 2
            print("<--match--> Next-->")
        else:
            print("<--No match--> Next-->")
            p = 1
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            for _ in range(0, 50):
                print("✨\n")
        draw_grid(ls)
    else:
        while True:
            pos1 = input(f"{player2} 1.card : ").capitalize()
            fnd1 = card_pos(ls, pos1)
            if fnd1 is None:
                print("Sorry, doesn't exist . Take another card !")
                continue
            else:
                break
        while True:
            pos2 = input(f"{player2} 2.card : ").capitalize()
            fnd2 = card_pos(ls, pos2)
            if fnd2 is None:
                print("Sorry, doesn't exist . Take another card !")
                continue
            else:
                break
        get_symbols(ls, fnd1, fnd2)
        if CARDS[fnd1[0] * 5 + fnd1[1]] == CARDS[fnd2[0] * 5 + fnd2[1]]:
            take_cards(ls, fnd1, fnd2)
            b -= 2
            print("<--match--> Next-->")
        else:
            p = 0
            print("<--No match--> Next-->")
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            for _ in range(0, 50):
                print("✨\n")
        draw_grid(ls)
print("After", cnt, "efforts")
print(f"{player1} CARDS: ")
for g in range(0, len(player1_cards)):
    print(player1_cards[g], end=" ")

print(f"\n{player2} CARDS: ")
for h in range(0, len(player2_cards)):
    print(player2_cards[h], end=" ")
print("\n\n\n")
if len(player1_cards) > len(player2_cards):
    print(f"🎉 {player1} win 🏆")
elif len(player1_cards) < len(player2_cards):
    print(f"🎉 {player2} win 🏆")
else:
    print("🎉Both win 🏆🏆")

print("I have little price for the winner 😜")
Drink = {1: "🍸", 2: "🍺", 3: "🍷", 4: "☕️", 5: "🥃"}  # cheers🥂
Meal = {1: "🍔", 2: "🌭", 3: "🍕", 4: "🌮", 5: "🥗", 6: "🍣"}  # enjoy🍽
Flower = {1: "🌻", 2: "🌹", 3: "🌷", 4: "🌼"}
Sweets = {1: "🍫", 2: "🍰", 3: "🍦", 4: "🍭"}

while True:
    price = input("Price:\nDrink=D\tMeal=M\tFlower=F\tSweet=S\tChar: ").upper()
    if price == "D":
        What = input("🧙\n1=🍸\t2=🍺\t3=🍷\t4=☕\t5=🥃\nnum:  ")
        if What.isdigit():
            if int(What) in range(1, 6):
                What = int(What)
                if len(player1_cards) > len(player2_cards):
                    print(f"Cheers{Drink[What]}", player1)
                    print("🧙 bye!👋")
                    break
                else:
                    print(f"Cheers{Drink[What]}", player2)
                    print("🧙 bye!👋")
                    break
            else:
                print("🧙 Enter a num from 1 to 4")
        else:
            print("🧙 Enter a num from 1 to 4")
    elif price == "M":
        What = input("🧙\n1=🍔\t2=🌭\t3=🍕\t4=🌮\t5=🥗\t6=🍣\nnum:  ")
        if What.isdigit():
            if int(What) in range(1, 7):
                What = int(What)
                if len(player1_cards) > len(player2_cards):
                    print(f"Enjoy {Meal[What]}", player1)
                    print("🧙 bye!👋")
                    break
                else:
                    print(f"Enjoy {Meal[What]}", player2)
                    print("🧙 bye!👋")
                    break
            else:
                print("🧙 Enter a num from 1 to 4")
        else:
            print("🧙 Enter a num from 1 to 4")
    elif price == "F":
        What = input("🧙\n1=🌻\t2=🌹\t3=🌷\t4=🌼\nnum: ")
        if What.isdigit():
            if int(What) in range(1, 5):
                What = int(What)
                if len(player1_cards) > len(player2_cards):
                    print(f"Enjoy {Flower[What]}", player1)
                    print("🧙 bye!👋")
                    break
                else:
                    print(f"Enjoy {Flower[What]}", player2)
                    print("🧙 bye!👋")
                    break
            else:
                print("🧙 Enter a num from 1 to 4")
        else:
            print("🧙 Enter a num from 1 to 4")
    elif price == "S":
        What = input("🧙\n1=🍫\t2=🍰\t3=🍦\t4=🍭\nnum: ")
        if What.isdigit():
            if int(What) in range(1, 5):
                What = int(What)
                if len(player1_cards) > len(player2_cards):
                    print(f"Enjoy {Sweets[What]}", player1)
                    print("🧙 bye!👋")
                    break
                else:
                    print(f"Enjoy {Sweets[What]}", player2)
                    print("🧙 bye!👋")
                    break
            else:
                print("🧙 Enter a num from 1 to 4")
        else:
            print("🧙 Enter a num from 1 to 4")
    else:
        print("🧙 Please enter D or M or F or S")
