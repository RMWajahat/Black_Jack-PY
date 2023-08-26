# DAY 11-------------------THE BALCk JAck GAME

# import random for COMPUTER SELECTION
import random 

# clear screen 
from os import system


# set all cards dictionary
All_cards={
    "A":11,
    "J":10,
    "Q":10,
    "K":10,
    "2":5,
    "3":5,
    "4":5,
    "5":5,
    "6":5,
    "7":5,
    "8":5,
    "9":5,
    "10":5,
}
sumPerson=0
sumComp=0


# ---------------------------------------------------------------------Now Choose two cards
my_cards=[]
comp_cards=[]
#--------------------------------------------------------------------- set person initial cards
def set_initial_cards(All_cards,sum_person):
    print("CARDS : ")
    for card in All_cards:
        print(card)
    while len(my_cards)<2:
        try:
            Card_val=input("Select any card from above cards\n\t\tNote: Don't repeat cards \n\n\tCARD :  ")
            if Card_val not in All_cards:
                print("You selected an un-recorganized card.\n\tYou missad the Turn")
                system("pause")
            else:
                if Card_val not in my_cards:
                    my_cards.append(Card_val)
                    sum_person=sum_person+All_cards[Card_val]
                    print("MY CARDS : ",my_cards)
                else:
                    print(f"You already have card  :   {Card_val}")
                    print("MY CARDS : ",my_cards)
                system("pause")
                system("cls")
        except Exception as e:
            print(e)
    return sum_person
# ---------------------------------------------------------------------computer turn block
def Comp_turn(Comp_cards,all_cards,sum_comp):
    print("\n COMPUTER:  Wait let me decide mine\n")
    print("Computer CARDS : ")
    for card in Comp_cards:
        print(card)
    
    Sum=int(sum_comp)
    try:
        Card_key=str(random.randint(2,10))
        if not Card_key in Comp_cards:
            Comp_cards+=Card_key
            Sum+=int(all_cards[Card_key])
        else:
            Card_key=random.randint(2,10)
            Comp_cards+=Card_key
            Sum+=int(all_cards[Card_key])
    except Exception as e:
        print(e)
    return Sum
# ---------------------------------------------------------------------person turn block
def Person_turn(my_cards,All_cards,sum_person):
    print("Your CARDS : ")
    for card in my_cards:
        print(card)
    try:
        Card_key=input("Select any card\n\t\tNote: Don't repeat cards \n\tCHOICE :  ")
        if Card_key not in All_cards:
            print("You selected an un-recorganized card.\n\tYou missad the Turn")
            system("pause")
            system("cls")
        else:
            if not Card_key in my_cards:
                my_cards+=Card_key
                sum_person=sum_person+int(All_cards[Card_key])
            else:
                Card_key=input("Select any card\t\tNote: Don't repeat cards  :  ")
                my_cards+=Card_key
                sum_person=sum_person+int(All_cards[Card_key])
    except Exception as e:
        print(e)
    return sum_person


# making a play
sumPerson=set_initial_cards(All_cards=All_cards,sum_person=sumPerson)
sumComp= Comp_turn(Comp_cards=comp_cards,all_cards=All_cards,sum_comp=sumComp)
print(type(sumComp),": sum comp")
print(type(sumPerson),": sum person")
i=1
system("CLS")
GAMEOVER=False
while not GAMEOVER:
    if sumComp>21 or sumPerson>21:
        GAMEOVER=True
    if int(sumComp)<=21 and sumPerson<=21:
        if i%2==1:
            sumPerson= int(Person_turn(my_cards=my_cards,All_cards=All_cards,sum_person=sumPerson))
        elif i%2==0 and int(sumComp)<17:
            sumComp= Comp_turn(Comp_cards=comp_cards,all_cards=All_cards,sum_comp=sumComp)
        system("PAUSE")
        i=i+1
        system("CLS")
    else:
        continue


if sumPerson>sumComp and sumPerson<=21:
    print(f"You win with score of {sumPerson}")
else:
    print(f"You lose with score of {sumPerson}  😭")