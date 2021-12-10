from random import choice
from time import sleep


def question_true_false(question):
    answer = input(question + "? Y/N\n").lower()
    if answer == "y":
        return True
    else:
        return False


def pick_a_card():
    return choice(deck_of_cards)


def return_card(chosen_card):
    card_number = " "
    if len(chosen_card) == 2:
        if chosen_card[0] == "J":
            card_number += "Jack"
        elif chosen_card[0] == "Q":
            card_number += "Queen"
        elif chosen_card[0] == "K":
            card_number += "King"
        elif chosen_card[0] == "A":
            card_number = "n "
            card_number += "Ace"
        else:
            card_number += chosen_card[0]
        card_suit = suit_letter_to_suit(chosen_card[1])
    elif chosen_card[0:2] == "10":
        card_number += "10"
        card_suit = suit_letter_to_suit(chosen_card[2])
    else:
        return "a joker"
    return "a" + card_number + " of " + card_suit


def return_card_name(chosen_card):
    card_number = ""
    if len(chosen_card) == 2:
        if chosen_card[0] == "J":
            card_number += "Jack"
        elif chosen_card[0] == "Q":
            card_number += "Queen"
        elif chosen_card[0] == "K":
            card_number += "King"
        elif chosen_card[0] == "A":
            card_number += "Ace"
        else:
            card_number += chosen_card[0]
    elif chosen_card[0:2] == "10":
        card_number += "10"
    return card_number


def return_random_card():
    return_card(pick_a_card())


def suit_letter_to_suit(letter):
    if letter == "h":
        return "hearts"
    elif letter == "d":
        return "diamonds"
    elif letter == "c":
        return "clubs"
    elif letter == "s":
        return "spades"
    else:
        return "no suit"


def create_deck():
    added_card = 0
    for card in range(1, 14):
        for suit in range(0, 4):
            if card >= 11:
                if card == 11:
                    added_card = "J"
                if card == 12:
                    added_card = "Q"
                if card == 13:
                    added_card = "K"
            elif card == 1:
                added_card = "A"
            else:
                added_card = (str(card))
            if suit % 4 == 1:
                added_card += "d"
            elif suit % 4 == 2:
                added_card += "h"
            elif suit % 4 == 3:
                added_card += "c"
            else:
                added_card += "s"
            deck_of_cards.append(added_card)
    """
    joker_choice = input("Would you like to add jokers? Y/N\n")
    if joker_choice == "y":
        deck_of_cards.append("Joker")
        deck_of_cards.append("Joker")
    """


def print_hand(input_hand):
    if input_hand == player_hand:
        total_hand = "You hold "
    else:
        total_hand = "The dealer holds "
    for card in range(0, len(input_hand)):
        if card == len(input_hand) - 1:
            if len(input_hand) == 2:
                total_hand += " and "
            else:
                total_hand += "and "
        chosen_card = input_hand[card]
        total_hand += return_card(chosen_card)
        if card < len(input_hand) - 1 and len(input_hand) > 2:
            total_hand += ", "
    print(total_hand)


def calculate_hand(hand):
    global player_blackjack
    global dealer_blackjack
    global player_bust
    global dealer_bust
    aces_in_hand = 0
    total = 0
    for card in range(0, len(hand)):
        if hand[card][0] == "A":
            aces_in_hand += 1
        elif hand[card][0] == "J" or hand[card][0] == "Q" or hand[card][0] == "K" or hand[card][1] == "0":
            total += 10
        else:
            total += int(hand[card][0])
    while aces_in_hand > 0:
        if aces_in_hand == len(hand):
            return len(hand)
        elif total == 10 and len(hand) == 2:
            if hand == player_hand:
                player_blackjack = True
            elif hand == dealer_hand:
                dealer_blackjack = True
            return
        elif total < 10:
            total += 11
            aces_in_hand -= 1
        else:
            total += 1
            aces_in_hand -= 1
    if total > 21:
        if hand == player_hand:
            player_bust = True
        elif hand == dealer_hand:
            dealer_bust = True
    return total


def deal_cards_blackjack():
    global player_total
    global dealer_total
    for i in range(0, 4):
        if i % 2 == 0:
            player_hand.append(deal_card(False))
        else:
            dealer_hand.append(deal_card(False))
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)


def deal_card(printout):
    dealt_card = pick_a_card()
    deck_of_cards.remove(dealt_card)
    if printout:
        print("You drew a " + return_card(dealt_card))
    return dealt_card


def begin_play_blackjack():
    create_deck()
    global dealer_total
    global player_total
    playing = True
    deal_cards_blackjack()
    print("The dealer is showing " + return_card(dealer_hand[0]))
    while playing and not player_bust and not dealer_bust:
        player_has_hit = False
        dealer_has_hit = False
        print_hand(player_hand)
        hit_choice = question_true_false("Would you like to hit")
        if hit_choice:
            print("->Hit<-")
            player_hand.append(deal_card(True))
            player_total = calculate_hand(player_hand)
            player_has_hit = True
        if dealer_total <= 17:
            print("The dealer will hit, bringing them to " + str(len(dealer_hand) + 1) + " cards")
            dealer_hand.append(deal_card(False))
            dealer_total = calculate_hand(dealer_hand)
            dealer_has_hit = True
        if not dealer_has_hit and not player_has_hit:
            print_hand(dealer_hand)
            print("\nYou have a total of " + str(player_total) + " points\n")
            print("The dealer has a total of " + str(dealer_total) + " points\n")
            if player_blackjack and dealer_blackjack:
                print("You have tied with blackjacks on both sides, what a rare occurrence")
            elif player_blackjack:
                print("You won with a blackjack, congratulations")
            elif dealer_blackjack:
                print("You have lost to the dealer's blackjack, unfortunate")
            elif player_total > dealer_total:
                print("You have beaten the dealer, good job")
            elif dealer_total > player_total:
                print("You have been beaten by the dealer, hope to see you again")
            else:
                print("You have tied the game, neither the player nor dealer lose anything")
            playing = False
    if player_bust:
        print("You've busted and have lost")
    elif dealer_bust:
        print("The dealer has busted and you win")
    play_again_choice = question_true_false("Would you like to play again")
    if play_again_choice:
        reset()
        begin_play_blackjack()


def reset():
    global deck_of_cards
    global player_total
    global player_hand
    global player_bust
    global dealer_total
    global dealer_bust
    global dealer_blackjack
    global player_blackjack
    global dealer_hand
    deck_of_cards = []
    create_deck()
    player_hand = []
    dealer_hand = []
    player_total = 0
    dealer_total = 0
    player_bust = False
    dealer_bust = False
    player_blackjack = False
    dealer_blackjack = False


def deal_deck():
    for i in range(0, 52):
        if i % 2 == 0:
            dealer_hand.append(deal_card(False))
        else:
            player_hand.append(deal_card(False))


def compare_top_card():
    global card_pool
    dealer_card = dealer_hand.pop(0)
    player_card = player_hand.pop(0)
    print("You show " + return_card(player_card))
    print("The dealer shows " + return_card(dealer_card))
    card_pool += [player_card, dealer_card]
    player_num = convert_card_to_number(player_card)
    dealer_num = convert_card_to_number(dealer_card)
    if player_num > dealer_num:
        print("You have won the war and your spoils have been added to your deck")
        for i in range(0, len(card_pool)):
            player_hand.append(card_pool[i])
    elif dealer_num > player_num:
        print("The dealer has won the war and their spoils have been added to their deck")
        for i in range(0, len(card_pool)):
            dealer_hand.append(card_pool[i])
    else:
        print("<----!The war continues, both sides must put 2 cards face down to fight over!---->")
        if len(player_hand) > 2 and len(dealer_hand) > 2:
            card_pool.extend([dealer_hand.pop(0), dealer_hand.pop(0), player_hand.pop(0), player_hand.pop(0)])
            compare_top_card()
        elif len(dealer_hand) < 2:
            for i in range(0, len(dealer_hand) - 1):
                card_pool.append(dealer_hand[i])
            card_pool.extend([player_hand.pop(0), player_hand.pop(0)])
        else:
            for i in range(0, len(player_hand) - 1):
                card_pool.append(player_hand[i])
            card_pool.extend([dealer_hand.pop(0), dealer_hand.pop(0)])
    card_pool = []


def convert_card_name_to_number(card_name):
    if card_name in word_to_value_dict:
        return word_to_value_dict[card_name]
    else:
        return int(card_name)


def convert_card_to_number(chosen_card):
    return convert_card_name_to_number(return_card_name(chosen_card))


def begin_play_war():
    deal_deck()
    playing = True
    while playing:
        compare_top_card()
        print("You have " + str(len(player_hand)) + " cards left")
        print("The dealer has " + str(len(dealer_hand)) + " cards left")
        if not len(player_hand) > 0 or not len(dealer_hand) > 0:
            playing = False
    play_again_choice = question_true_false("Would you like to play again")
    if play_again_choice:
        reset()
        begin_play_war()


word_to_value_dict = {"Ace": 14, "King": 13, "Queen": 12, "Jack": 11}
deck_of_cards = []
create_deck()
card_pool = []
player_hand = []
dealer_hand = []
player_total = 0
dealer_total = 0
player_bust = False
dealer_bust = False
player_blackjack = False
dealer_blackjack = False
playing_game = True
while playing_game:
    game_choice = input("What game would you like to play? (type the number)"
                        "\n 0: Exit"
                        "\n 1: Blackjack"
                        "\n 2: War"
                        "\n")
    if game_choice == "0":
        playing_game = False
    elif game_choice == "1":
        print("Beginning blackjack")
        sleep(3)
        begin_play_blackjack()
    elif game_choice == "2":
        print("Beginning war")
        sleep(3)
        begin_play_war()
    reset()
