def get_rounds(number):
    round_list = []
    for i in range(0,3):
        hand = number +i
        round_list.append(hand)
    return round_list
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
def list_contains_round(rounds, number):
    return number in rounds
def card_average(hand):
    return sum(hand)/len(hand)
def approx_average_is_average(hand):
    media = (len(hand)+1) / 2 -1
    valoreMedio=hand[int(media)]
    valloreF = sum(hand)/len(hand)
    first_and_last = (hand[0]+hand[-1])/2
    return valloreF==valoreMedio or first_and_last == valloreF
def average_even_is_average_odd(hand):
    media = (len(hand)+1) / 2 -1
    valoreMedio=hand[int(media)]
    valloreF = sum(hand)/len(hand)
    if valloreF == valoreMedio:return True
    else:return False
def maybe_double_last(hand):
    if hand[-1]== 11:hand[-1]= 22
    return hand