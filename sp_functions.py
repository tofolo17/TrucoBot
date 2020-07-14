from random import *
from time import sleep


# Get the cards from each player
def get_cards(comparative_card_list, global_card_suits, flipped_card=0):

    # Get random cards ans suits
    entity_card_values = [randint(1, 10) for _ in range(0, 3)]
    entity_card_values.sort()

    # Reorganize the bot's hand to a order of power (shackle included)
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

    # Compare numbers with dictionary indexes
    for i in range(len(entity_cards)):
        entity_cards[i] = f'{comparative_card_list[entity_card_values[i]]} de {global_card_suits[entity_card_suits[i]]}'
    return entity_cards


# Bot "IA"
def bot_plays(comparative_card_list, global_card_suits, bot_cards, player_cards, comparative_card=None,
              did_first=None, draw=None):

    print(f'\n{bot_cards}')

    # Bot "IA" variables

    print(comparative_card_list)
    exit()

    enemy_power = comparative_card_list.index(comparative_card.split()[0]) if comparative_card else 0
    possible_card = bot_cards[0]
    winnable_cards = []
    consequence = 0

    # Bot's turn
    print('\nMinha vez...')
    sleep(1)

    # If the player has 3 cards, plays the first or the second one (order of power)
    if len(player_cards) == 3:
        chosen_card = bot_cards[randint(0, 1)]
        print(f'Eu jogo: {chosen_card}')
        sleep(1)
        bot_cards.remove(chosen_card)
        return player_plays(comparative_card_list, global_card_suits, bot_cards, player_cards, chosen_card)

    # If the player has one or two cards...
    else:

        # If he did not score first, he will compare his cards with the one on the table and eliminate the weakest who
        # can beat him, or the weakest if he cannot.
        if not did_first:
            for card in bot_cards:
                if not draw:
                    if comparative_card_list.index(card.split()[0]) > enemy_power:
                        winnable_cards.append(card)
                    elif comparative_card_list.index(card.split()[0]) == enemy_power:
                        if comparative_card_list.index(bot_cards[-1].split()[0]) >= 8:
                            winnable_cards.append(card)
                else:
                    if comparative_card_list.index(card.split()[0]) > enemy_power:
                        winnable_cards.append(card)
            if len(winnable_cards) >= 1:
                possible_card = winnable_cards[0]
                print(f'Eu jogo: {possible_card}')
            else:
                print(f'Eu jogo: {possible_card}')
            bot_cards.remove(possible_card)
            if len(player_cards) == len(bot_cards):
                sleep(0.5)
                if comparative_card_list.index(comparative_card.split()[0]) > \
                        comparative_card_list.index(possible_card.split()[0]):
                    consequence = 1
                    print('\nVocê venceu.\n')
                elif comparative_card_list.index(comparative_card.split()[0]) == \
                        comparative_card_list.index(possible_card.split()[0]):
                    consequence = 2
                    print('\n --- Temos um empate! ---\n')
                else:
                    consequence = 3
                    print('\nEu venci.\n')
            else:
                return player_plays(comparative_card_list, global_card_suits, bot_cards, player_cards, possible_card)

        # If he did it first, he'll eliminate the weakest
        if did_first:
            chosen_card = bot_cards[0]
            print(f'Eu jogo: {chosen_card}')  # Continuar daqui
            bot_cards.remove(chosen_card)
            return player_plays(comparative_card_list, global_card_suits, bot_cards, player_cards, chosen_card)
    return consequence


def player_plays(comparative_card_list, global_card_suits, bot_cards, player_cards, last_card=None):
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
            for card in card_opt:
                if card == player_choice:
                    played_card = player_cards[card - 1]
                    print(f'Você jogou: {played_card}')
                    player_cards.pop(card - 1)
                    if len(player_cards) == len(bot_cards):
                        sleep(0.5)
                        if comparative_card_list.index(played_card.split()[0]) > \
                                comparative_card_list.index(last_card.split()[0]):
                            consequence = 1
                            print('\nVocê venceu.\n')
                        elif comparative_card_list.index(played_card.split()[0]) == \
                                comparative_card_list.index(last_card.split()[0]):
                            consequence = 2
                            print('\n--- Temos um empate! ---\n')
                        else:
                            consequence = 3
                            print('\nEu venci.\n')
                    else:
                        return bot_plays(comparative_card_list, global_card_suits, bot_cards, player_cards, played_card)
                    break
            return consequence
        except(ValueError, IndexError, ZeroDivisionError):
            print('Inválido. Tente novamente.')


def get_highest_card(cards, comparative):
    card_number_list = []
    for card in cards:
        if card.split()[0] in comparative:
            card_number_list.append(comparative.index(card.split()[0]))
    highest = max(card_number_list)
    return highest


def compare_highest_cards(comparative_card_list, global_card_suits, bot_cards, player_cards):
    bot_biggest = get_highest_card(bot_cards, comparative_card_list)
    player_biggest = get_highest_card(player_cards, comparative_card_list)
    if player_biggest > bot_biggest:
        print('Como a sua última carta é a mais forte, você ganha!\n')
        return 1
    elif player_biggest == bot_biggest:
        print('Empatamos! Quem pontuou primeiro vence!')
        return 2
    else:
        print('Como a minha última carta é a mais forte, eu ganho!\n')
        return 3
