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


def bot_plays(bot_cards, player_cards):
    print('\nMinha vez...')
    if len(player_cards) == 3:
        chosen_card = bot_cards[randint(0, 1)]
        print(f'Eu jogo: {chosen_card}')
        bot_cards.remove(chosen_card)
        player_plays(bot_cards, player_cards)
    elif len(player_cards) == 2:
        print('Ainda não sei o que fazer')
    elif len(player_cards) == 1:
        print('Ainda não sei o que fazer')


def player_plays(bot_cards, player_cards):
    print('\nSua vez...')
    card_opt, act_opt = [1, 2, 3], [0, 9]
    while True:
        player_choice = int(input('Sua opção: '))
        if player_choice in card_opt + act_opt:
            break
        else:
            print('Inválido, tente novamente.')
    for card in card_opt:
        if card == player_choice:
            played_card = player_cards[card - 1]
            print(f'Você jogou: {played_card}')
            player_cards.pop(card - 1)
            if len(player_cards) == len(bot_cards):
                print('Rodada terminada')
            else:
                bot_plays(bot_cards, player_cards)