import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def calculate_score(cards):
    """take a list of cards and calculate their score"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if (sum(cards) > 21 and 11 in cards):
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def deal_card():
    choose=random.choice(cards)
    return choose

def compare(u_score, co_score):
    if u_score == co_score:
        return "Draw 🪙"
    elif co_score==0:
        return "Lose, Opponent has Black Jack o((⊙﹏⊙))o."
    elif u_score==0:
        return "You win with Black Jack 😎"
    elif u_score>21:
        return "You went over, you lose 😒"
    elif co_score>21:
        return "Opponent went over, you win 😊"
    elif u_score>co_score:
        return  "You Win!!! 💵💵"
    else:
        return "You Lose!!! 😶‍🌫️🤐"



def playgame():
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    computer_score=-1
    user_score=-1

    for _  in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards:{computer_cards[0]}")



        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another cards, type 'n' to pass: ").upper()
            if user_should_deal=='Y':
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? type 'y' to continue: ")=="y":
    print("\n"*100)
    playgame()














