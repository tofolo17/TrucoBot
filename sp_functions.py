from random import *


def get_cards(global_card_values, global_card_suits, flipped_card=0):
    entity_card_values = [randint(1, 10) for _ in range(0, 3)]
    entity_card_values.sort()
    shackle_number = flipped_card + 1 if flipped_card <= 9 else 1
    for card in entity_card_values:
        i = 2
        if card == shackle_number:
            entity_card_values.remove(card)
            entity_card_values.insert(i, shackle_number)
            i -= 1
    entity_card_suits = [randint(1, 4) for _ in range(0, 3)]
    entity_card_suits.sort()
    entity_cards = [0, 0, 0]
    for i in range(len(entity_cards)):
        entity_cards[i] = f'{global_card_values[entity_card_values[i]]} de {global_card_suits[entity_card_suits[i]]}'
    return entity_cards


def bot_plays(global_card_values, global_card_suits, bot_cards, player_cards):
    print('\nMinha vez...')
    if len(player_cards) == 3:
        chosen_card = bot_cards[randint(0, 1)]
        print(f'Eu jogo: {chosen_card}')
        bot_cards.remove(chosen_card)
        return player_plays(global_card_values, global_card_suits, bot_cards, player_cards, chosen_card)
    elif len(player_cards) == 2:
        print('Ainda não sei o que fazer\n')
    elif len(player_cards) == 1:
        print('Ainda não sei o que fazer\n')
    pass


def player_plays(global_card_values, global_card_suits, bot_cards, player_cards, last_card=None):
    print('\nSua vez...')
    consequence = 0
    card_opt, act_opt = [1, 2, 3], [0, 9]
    while True:
        try:
            player_choice = int(input('Sua opção: '))
            if player_choice in card_opt + act_opt:
                break
            else:
                print('Inválido, tente novamente.')
        except ValueError:
            print('Inválido. Tente novamente')
    for card in card_opt:
        if card == player_choice:
            played_card = player_cards[card - 1]
            print(f'\nVocê jogou: {played_card}')
            player_cards.pop(card - 1)
            if len(player_cards) == len(bot_cards):
                comparative_list = list(global_card_values.values())
                comparative_list.reverse()
                if comparative_list.index(played_card.split()[0]) > comparative_list.index(last_card.split()[0]):
                    consequence = 1
                    print('Você venceu.\n')
                elif comparative_list.index(played_card.split()[0]) == comparative_list.index(last_card.split()[0]):
                    consequence = 2
                    print('Temos um empate!\n')
                else:
                    consequence = 3
                    print('Eu venci!\n')
            else:
                return bot_plays(global_card_values, global_card_suits, bot_cards, player_cards)
    return consequence


def get_bigger(global_card_values, global_card_suits, bot_cards, player_cards):
    bot_biggest = player_biggest = 0
    bot_card_numbers, player_card_numbers = [], []
    comparative_list = list(global_card_values.values())
    comparative_list.reverse()
    for card in bot_cards:
        if card.split()[0] in comparative_list:
            bot_card_numbers.append(comparative_list.index(card.split()[0]))
        bot_biggest = max(bot_card_numbers)
    for card in player_cards:
        if card.split()[0] in comparative_list:
            player_card_numbers.append(comparative_list.index(card.split()[0]))
        player_biggest = max(player_card_numbers)
    if player_biggest > bot_biggest:
        return 1
    else:
        return 2


def get_points(turn_point, total):
    turn_point += 1
    total += 1
