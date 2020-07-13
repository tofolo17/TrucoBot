from random import *
from time import sleep


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


def bot_plays(global_card_values, global_card_suits, bot_cards, player_cards, comparative_card=None, did_first=None):
    print('\nMinha vez...')
    sleep(1)
    consequence = 0
    comparative_list = list(global_card_values.values())
    comparative_list.reverse()

    if len(player_cards) == 3:
        chosen_card = bot_cards[randint(0, 1)]
        print(f'Eu jogo: {chosen_card}')
        sleep(1)
        bot_cards.remove(chosen_card)
        return player_plays(global_card_values, global_card_suits, bot_cards, player_cards, chosen_card)

    elif len(player_cards) == 2:
        if not did_first:
            winnable_cards = []
            possible_card = bot_cards[0]
            enemy_power = comparative_list.index(comparative_card.split()[0])
            for card in bot_cards:
                if comparative_list.index(card.split()[0]) >= enemy_power:
                    winnable_cards.append(card)
            if len(winnable_cards) > 1:
                if comparative_list.index(winnable_cards[0].split()[0]) >= 9 and len(winnable_cards) >= 2:
                    print(f'Eu jogo: {possible_card}')
                else:
                    possible_card = winnable_cards[0]
                    print(f'Eu jogo: {possible_card}')
            else:
                print(f'Eu jogo: {possible_card}')
            bot_cards.remove(possible_card)
            if len(player_cards) == len(bot_cards):
                sleep(0.5)
                if comparative_list.index(comparative_card.split()[0]) > \
                        comparative_list.index(possible_card.split()[0]):
                    consequence = 1
                    print('\nVocê venceu.')
                elif comparative_list.index(comparative_card.split()[0]) == \
                        comparative_list.index(possible_card.split()[0]):
                    consequence = 2
                    print('\nTemos um empate!')
                else:
                    consequence = 3
                    print('\nEu venci')
                print('-' * 30)
        if did_first:  # Se a segunda é forte demais, esconde a de agora (mas ainda nao tenho a parada de esconder)
            chosen_card = bot_cards[0]
            print(f'Eu jogo: {chosen_card}')  # Continuar daqui
            bot_cards.remove(chosen_card)
            return player_plays(global_card_values, global_card_suits, bot_cards, player_cards, chosen_card)

    elif len(player_cards) == 1:
        print('Ainda não sei o que fazer\n')
    return consequence


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
        except (ValueError, IndexError):
            print('Inválido. Tente novamente')
    for card in card_opt:
        if card == player_choice:
            played_card = player_cards[card - 1]
            print(f'Você jogou: {played_card}')
            player_cards.pop(card - 1)
            if len(player_cards) == len(bot_cards):
                sleep(0.5)
                comparative_list = list(global_card_values.values())
                comparative_list.reverse()
                if comparative_list.index(played_card.split()[0]) > comparative_list.index(last_card.split()[0]):
                    consequence = 1
                    print('\nVocê venceu.')
                elif comparative_list.index(played_card.split()[0]) == comparative_list.index(last_card.split()[0]):
                    consequence = 2
                    print('\nTemos um empate!')
                else:
                    consequence = 3
                    print('\nEu venci!')
            else:
                return bot_plays(global_card_values, global_card_suits, bot_cards, player_cards, played_card)
    return consequence


def get_highest_card(cards, comparative):
    card_number_list = []
    for card in cards:
        if card.split()[0] in comparative:
            card_number_list.append(comparative.index(card.split()[0]))
    highest = max(card_number_list)
    return highest


def compare_highest_cards(global_card_values, global_card_suits, bot_cards, player_cards):
    comparative_list = list(global_card_values.values())
    comparative_list.reverse()
    bot_biggest = get_highest_card(bot_cards, comparative_list)
    player_biggest = get_highest_card(player_cards, comparative_list)
    if player_biggest > bot_biggest:
        return 1
    elif player_biggest == bot_biggest:
        return 2
    else:
        return 3
