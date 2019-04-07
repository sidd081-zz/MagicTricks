import random
# from colorama import Fore, Back, Style
import time

cards = ["2 of spade", "3 of spade", "4 of spade", "5 of spade", "2 of heart", "3 of heart", "4 of heart", "5 of heart", "2 of diamond", "3 of diamond", "4 of diamond", "5 of diamond", "2 of club", "3 of club", "4 of club", "5 of club", "jack of spade", "jack of club", "jack of diamond", "jack of heart", "queen of spade", "queen of club", "queen of diamond", "queen of heart", "ace of spade", "ace of club", "ace of diamond"]

# print cards

def play_cards(cards):
    
    i = 0
    deck_1 = []
    deck_2 = []
    deck_3 = []
    while i < 27:
        deck_1.append(cards[i])
        deck_2.append(cards[i+1])
        deck_3.append(cards[i+2])
        i = i + 3
    # print len(deck_1) 
    # print len(deck_2)
    # print len(deck_3)

    decks = []
    decks.append(deck_1)
    decks.append(deck_2)
    decks.append(deck_3)
    i = 0
    print "\n"
    while i < 9:
        print "{:20s} {:20s} {:20s}".format(deck_1[i], deck_2[i], deck_3[i])
        i = i + 1
    print "\n"
    return decks


random.shuffle(cards)

for x in cards:
    print x

print "\n\n1. Remember a card from above given list"
raw_input("Press any key to proceed")
user_input = raw_input("2. Input any number from 1 to 26 for game to start\n")

try:
    number = int(user_input)
    if (number < 1 or number > 26):
        print "INVALID INPUT, GAME END"
        exit
    number = number -1
except:
    print "Invalid Input, GAME END"
    exit

nine_quotient = number/9
# print "9 --> " + str(nine_quotient)

three_quotient = (number%9)/3
# print "3 --> " + str(three_quotient)

one_quotient = ((number%9)%3)
# print "1 --> " + str(one_quotient)


arr = [one_quotient, three_quotient, nine_quotient]

for x in arr:
    print "SHUFFLING CARDS"
    decks = play_cards(cards)
    column_input = raw_input("In which column your card is present? 0 or 1 or 2? (From Left To Right)\n")
    try:
        column = int(column_input)  
        if (column < 0 or column > 2):
            print "INVALID INPUT, GAME END"
            exit

    except:
        print "Invalid Input, GAME END"
        exit

    cards = []
    if x == 0: #TOP
        temp = decks[column]
        del decks[column : column+1]
        decks.insert(0, temp)

    elif x == 1: #MIDDLE
        temp = decks[column]
        del decks[column : column+1]
        decks.insert(1, temp)

    elif x == 2: #BOTTOM 
        temp = decks[column]
        del decks[column : column+1]
        decks.append(temp)

    for deck in decks:
        for y in deck:
            cards.append(y)


print "\n\n"
i = 0 

print "OPENING CARDS ONE BY ONE"
while i < number:
    print str(i+1) + " --> "  + cards[i]
    i = i + 1;
    time.sleep(0.5)

print "YOUR CARD IS\n"
print(str(i+1) + " --> " +cards[number])







