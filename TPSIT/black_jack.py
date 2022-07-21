def value_of_card(card):
    if card == 'K' or card == 'Q' or card == 'J':return 10
    elif card == 'A':return 1
    else:return int(card)
def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):return card_one
    elif value_of_card(card_one) < value_of_card(card_two):return card_two
    else: return card_one, card_two
def value_of_ace(card_one, card_two):
    if (value_of_card(card_one) + value_of_card(card_two) + 11 <=21) and not (card_one=='A' or card_two=='A'):return 11
    else:return 1
def is_blackjack(card_one, card_two):
    if (card_one in ('A','K','Q','J','10') and card_two in ('A','K','Q','J','10')) and not (value_of_card(card_one) == value_of_card(card_two)):return True
    else:return False
def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):return True
    else:return False
def can_double_down(card_one, card_two):
    if 7<(value_of_card(card_one) + value_of_card(card_two)) <12:return True
    else:return False