#Black JAck Game
import random as r
def deal_card():
    """Genarates Random card"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    rancard=r.choice(cards)
    return rancard 

def cal_score(su):
    """Returns the score of cards"""
    if sum(su)==21 and len(su)==2:
        return 0
    if 11 in su and sum(su)>21:
        su.remove(11)
        su.append(1)
    return sum(su)

def compare(uscore,cscore):
    if uscore==cscore:
        return "Draw Match!!!"
    elif cscore==0:
        return "Lose,opponent has BLACKJACK!!!"
    elif uscore==0:
        return "You won with BLACKJACK!!!"
    elif uscore>21:
        return "You went over. You lose!!"
    elif cscore>21:
        return "Your opponent went over. You Win!"
    elif cscore<uscore:
        return "You Win!!!!"
    else:
        return "You Lose!!!!"


def playgame():
    ycard=[]
    cocard=[]
    gameover=False

    for i in range(2):
        ycard.append(deal_card())
        cocard.append(deal_card())

    while not gameover:
        uscore=cal_score(ycard)
        cscore=cal_score(cocard)
        print(f"\n\n  Your cards:{ycard},score:{uscore}")
        print(f"  Computer's First  cards:{cocard[0]}\n\n")

        if uscore==0 or cscore==0 or uscore>21:
            gameover=True
        else:
            do =input("Do you like to draw another card?y/n: ").lower()
            if do=='y':
                ycard.append(deal_card())
            else:
                gameover=True

    while cscore!=0 and cscore<17:
        cocard.append(deal_card())
        cscore=cal_score(cocard)
    print(f"\n\n  Your Final Hand:{ycard},your score:{uscore}")
    print(f"  Computer's Final Hand:{cocard},Computer score:{cscore}\n\n")
    print(compare(uscore,cscore))

print("\n"*12)
while input("Do you want to play the game of BlackJack?y/n:")=='y':
    playgame()
