from sp_functions import *

card_values = {
    '3': 10,
    '2': 9,
    'A': 8,
    'K': 7,
    'J': 6,
    'Q': 5,
    '7': 4,
    '6': 3,
    '5': 2,
    '4': 1
}

card_suits = {
    'Paus': 4,
    'Copas': 3,
    'Espadas': 2,
    'Ouros': 1
}

inverted_card_values = {v: k for k, v in card_values.items()}
inverted_card_suits = {v: k for k, v in card_suits.items()}

# Game loop
total_p = total_b = 0
while total_p < 12 and total_b < 12:
    print(f'Placar geral: {total_p} x {total_b}\n')
    print('Nova rodada')

    # Game variables
    round_p = round_b = 0
    conditional = first_point = ''

    # Flipped card and shackle
    flipped_card = randint(1, 10)
    print(f'Vira: {inverted_card_values[flipped_card]} de {inverted_card_suits[randint(1, 4)]}\n')
    shackle = inverted_card_values[1] if flipped_card == 10 else inverted_card_values[flipped_card + 1]

    # Distributing the cards
    player_cards = get_cards(inverted_card_values, inverted_card_suits)
    bot_cards = get_cards(inverted_card_values, inverted_card_suits, flipped_card)

    # Round loop
    while round_p < 2 and round_b < 2:
        next_turn = False

        # Turn loop
        while not next_turn:
            if round_p != 0 or round_b != 0:
                print(f'Pontos nessa rodada: {round_p} x {round_b}\n')
            # Cartas e opções
            print('Suas cartas: ')
            for i in range(len(player_cards)):
                print(f'{i + 1}°: {player_cards[i]}')
            print('\n0: Truco\n9: Fugir')

            # Who plays first in first and result of the round
            if round_p == round_b == 0:
                who_plays = randint(1, 2)
                result = bot_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards) \
                    if who_plays == 1 else player_plays(inverted_card_values, inverted_card_suits, bot_cards,
                                                        player_cards)
                if result == 1:
                    round_p += 1
                    first_point = 'player did first'
                    conditional = 'p starts'
                elif result == 2:
                    round_p += 1
                    round_b += 1
                    conditional = 'play biggest'
                else:
                    round_b += 1
                    first_point = 'bot did first'
                    conditional = 'b starts'
                next_turn = True

            # Other rounds conditionals
            else:
                if conditional == 'p starts':
                    result = player_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards)
                    if result == 1 or result == 2:
                        get_points(round_p, total_p)
                    else:
                        round_b += 1
                        conditional = 'who did first'
                elif conditional == 'b starts':
                    result = bot_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards)
                    if result == 2 or result == 3:
                        get_points(round_b, total_b)
                    else:
                        round_p += 1
                    conditional = 'who did first'
                elif conditional == 'play biggest':
                    result = get_bigger(inverted_card_suits, inverted_card_suits, bot_cards, player_cards)
                    if result == 1:
                        get_points(round_p, total_p)
                    else:
                        get_points(round_b, total_b)
                else:
                    if first_point == 'player did first':
                        get_points(round_p, total_p)
                    else:
                        get_points(round_b, total_b)
                next_turn = True
