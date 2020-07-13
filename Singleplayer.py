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
}  # Sei lá ta tudo bugado

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
    print(f'\n--- Placar geral: {total_p} x {total_b} ---')
    print('Nova rodada\n')

    # Game variables
    round_p = round_b = 0
    conditional = first_point = who_started = ''
    draw_counter = 0

    # Flipped card and shackle
    flipped_card = randint(1, 10)
    print(f'Vira: {inverted_card_values[flipped_card]} de {inverted_card_suits[randint(1, 4)]}')
    shackle = inverted_card_values[1] if flipped_card == 10 else inverted_card_values[flipped_card + 1]

    # Distributing the cards
    player_cards = get_cards(inverted_card_values, inverted_card_suits)
    bot_cards = get_cards(inverted_card_values, inverted_card_suits, flipped_card)

    # Round loop
    while round_p < 2 and round_b < 2:

        # Showing points
        if round_p != 0 or round_b != 0:
            print(f'Pontos nessa rodada: {round_p} x {round_b}\n')

        # Cards and options
        if not round_b == round_p == 1:
            print('Suas cartas: ')
            for i in range(len(player_cards)):
                print(f'{i + 1}°: {player_cards[i]}')
            print('\n0: Truco\n9: Fugir')

        # First conditional
        if round_p == round_b == 0 or conditional == 'draw':

            # Who plays first
            who_plays = randint(1, 2)
            if who_plays == 1 or who_started == 'player':
                result = bot_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards, did_first=True) \
                    if conditional == 'draw' else \
                    bot_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards)
                who_started = 'bot'
            else:
                result = player_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards)
                who_started = 'player'

            # First result analysis
            if result == 1:
                if draw_counter == 1:
                    round_p += 2
                else:
                    round_p += 1
                first_point = 'player did first'
                conditional = 'p starts'
            elif result == 2:
                conditional = 'draw'
                draw_counter += 1
                if draw_counter == 2:
                    conditional = 'play biggest'
                elif draw_counter == 3:
                    print('Ninguem pontuou!')
                    round_p = round_b = 100
            else:
                if draw_counter == 1:
                    round_b += 2
                else:
                    round_b += 1
                first_point = 'bot did first'
                conditional = 'b starts'

        # Second conditional
        else:

            # if x win first, x begins next round --> second result analysis
            if conditional == 'p starts':
                result = player_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards)
                if result == 1 or result == 2:
                    round_p += 1
                    total_p += 1
                else:
                    round_b += 1
                    conditional = 'play biggest'
            elif conditional == 'b starts':
                result = bot_plays(inverted_card_values, inverted_card_suits, bot_cards, player_cards,
                                   did_first=True)
                if result == 2 or result == 3:
                    round_b += 1
                    total_b += 1
                else:
                    round_p += 1
                    conditional = 'play biggest'

            # if x win and after y win -- > get higher card // if draw --> x win because he did first
            else:
                result = compare_highest_cards(inverted_card_values, inverted_card_suits, bot_cards, player_cards)
                if result == 1:
                    round_p += 1
                    total_p += 1
                elif result == 2:
                    if first_point == 'player did first':
                        round_p += 1
                        total_p += 1
                    else:
                        round_b += 1
                        total_b += 1
                else:
                    round_b += 1
                    total_b += 1
