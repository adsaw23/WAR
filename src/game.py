from player_class import Player
from deck_class import Deck
import card_class
import random
Player1 = Player('P1')
Player2 = Player('P2')

new_deck = Deck()
new_deck.shuffle_deck()

for _ in range(26):
    Player1.add_cards(new_deck.deal_one())
    Player2.add_cards(new_deck.deal_one())

game_on = True
round = 0

while game_on:
    round += 1
    print(f'Round Number: {round}')
    
    if len(Player1.all_cards) == 0:
        game_on = False
        print("Player 1 ran out of cards! Player 2 wins")
        break

    if len(Player2.all_cards) == 0:
        game_on = False
        print("Player 2 ran out of cards! Player 1 wins")
        break
    
    P1_current_round_cards = [Player1.remove_one()]
    P2_current_round_cards = [Player2.remove_one()]
    
    at_war = True

    while at_war:
        if P1_current_round_cards[-1].value > P2_current_round_cards[-1].value:
            Player1.add_cards(P1_current_round_cards)
            Player1.add_cards(P2_current_round_cards)
            at_war = False
        elif P1_current_round_cards[-1].value < P2_current_round_cards[-1].value:
            Player2.add_cards(P2_current_round_cards)
            Player2.add_cards(P1_current_round_cards)
            at_war = False
        else:
            print("WAR!")
            if len(Player1.all_cards) < 5:
                print("Player 1 unable to declare war")
                print("Player 2 wins")
                game_on = False
                break
            elif len(Player2.all_cards) < 5:
                print("Player 2 unable to declare war")
                print("Player 1 wins")
                game_on = False
                break
            else:
                for _ in range(5):
                    P1_current_round_cards.append(Player1.remove_one())
                    P2_current_round_cards.append(Player2.remove_one())