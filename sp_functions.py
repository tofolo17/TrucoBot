from random import *
from time import sleep


# Get the cards from each player
def get_cards(comparative_card_list, global_card_suits):

    # Get random cards ans suits
    entity_card_values = [randint(0, 9) for _ in range(0, 3)]
    entity_card_values.sort()
    entity_card_suits = [randint(0, 3) for _ in range(0, 3)]
    entity_card_suits.sort()
    entity_cards = [0, 0, 0]

    # Compare numbers with dictionary indexes
    for i in range(len(entity_cards)):
        entity_cards[i] = [comparative_card_list[entity_card_values[i]], global_card_suits[entity_card_suits[i]]]
    return entity_cards


# Return the result of a turn
def compare_cards(comparative_card_list, card_1, card_2):
    if comparative_card_list.index(card_1[0]) > comparative_card_list.index(card_2[0]):
        turn_result = 1
    elif comparative_card_list.index(card_1[0]) == comparative_card_list.index(card_2[0]):
        turn_result = 2
    else:
        turn_result = 3
    return turn_result


# Increase match points
def get_points(this_round, points, total=None):
    new_r = this_round + points
    if total is not None:
        new_t = total + 1
        return new_r, new_t
    else:
        return new_r


# Bot "IA"
def bot_plays(comparative_card_list, comparative_suits_list, bot_cards, player_cards, conditional,
              comparative_card=None, did_first=None):

    # Bot "IA" variables
    enemy_power = comparative_card_list.index(comparative_card[0]) if comparative_card else 0
    possible_card = bot_cards[0]
    playable_cards = []
    consequence = 0

    # print(f'\n{bot_cards}')

    # Bot's turn
    print('\nMinha vez...')
    sleep(1)

    # If the player has 3 cards, plays the first or the second one (order of power)
    if len(player_cards) == 3:
        chosen_card = bot_cards[randint(0, 1)]
        print(f'Eu jogo: {chosen_card[0]} de {chosen_card[1]}')
        bot_cards.remove(chosen_card)
        sleep(1)
        return player_plays(comparative_card_list, comparative_suits_list, bot_cards, player_cards,
                            conditional=conditional, last_card=chosen_card)

    # If the player has one or two cards...
    else:

        # If he did not score first, he will compare his cards with the one on the table and eliminate the weakest who
        # can beat him, or the weakest if he cannot.
        if not did_first:
            for card in bot_cards:
                if conditional != 'draw':
                    if comparative_card_list.index(card[0]) > enemy_power:
                        playable_cards.append(card)
                    elif comparative_card_list.index(card[0]) == enemy_power:
                        if comparative_card_list.index(bot_cards[-1][0]) >= 8:
                            playable_cards.append(card)
                else:
                    possible_card = bot_cards[-1]
            if len(playable_cards) >= 1:
                possible_card = playable_cards[0]
                print(f'Eu jogo: {possible_card[0]} de {possible_card[1]}')
            else:
                print(f'Eu jogo: {possible_card[0]} de {possible_card[1]}')
            bot_cards.remove(possible_card)
            if len(player_cards) == len(bot_cards):
                sleep(0.5)
                consequence = compare_cards(comparative_card_list, comparative_card, possible_card)
            else:
                return player_plays(comparative_card_list, comparative_suits_list, bot_cards, player_cards,
                                    conditional=conditional, last_card=possible_card)

        # If he did it first, he'll eliminate the weakest
        if did_first:
            chosen_card = bot_cards[0]
            print(f'Eu jogo: {chosen_card[0]} de {chosen_card[1]}')
            bot_cards.remove(bot_cards[0])
            return player_plays(comparative_card_list, comparative_suits_list, bot_cards, player_cards,
                                conditional=conditional, last_card=chosen_card)
    return consequence


# Player choosing the card
def player_plays(comparative_card_list, global_card_suits, bot_cards, player_cards, conditional, last_card=None):
    print('\nSua vez...')
    card_opt, act_opt = [1, 2, 3], [0, 9]
    consequence = 0
    while True:
        try:
            player_choice = int(input('Sua opção: '))
            while True:
                if player_choice in card_opt + act_opt:
                    break
                else:
                    _ = 1/0
            for option in card_opt:
                if option == player_choice:
                    chosen_card = player_cards[option - 1]
                    print(f'Você jogou: {chosen_card[0]} de {chosen_card[1]}')
                    player_cards.pop(option - 1)
                    if len(player_cards) == len(bot_cards):
                        sleep(0.5)
                        consequence = compare_cards(comparative_card_list, chosen_card, last_card)
                    else:
                        return bot_plays(comparative_card_list, global_card_suits, bot_cards, player_cards,
                                         conditional=conditional, comparative_card=chosen_card)
                    break
            return consequence
        except(ValueError, IndexError, ZeroDivisionError):
            print('Inválido. Tente novamente.')
