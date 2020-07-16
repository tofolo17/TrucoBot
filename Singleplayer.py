from sp_functions import *

# Game loop
total_p = total_b = who_plays = result = 0
while total_p < 12 and total_b < 12:

    card_values = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
    card_suits = ['Ouros', 'Espadas', 'Copas', 'Paus']

    # Scores
    score_text = f'--- Placar geral: {total_p} x {total_b} ---'
    print('')  # Sadly necessary
    print('-' * len(score_text))
    print(score_text)
    print('-' * len(score_text))
    print(' ' * (len(score_text) - 20), 'Nova rodada\n')

    # Flipped card and shackle
    flipped_card = randint(0, 9)
    print(f'Vira: {card_values[flipped_card]} de {card_suits[randint(0, 3)]}')
    shackle = card_values[0] if flipped_card == 9 else card_values[flipped_card + 1]

    # Reorganize the card_values based on the shackle
    for element in card_values:
        if element == shackle:
            card_values.remove(shackle)
            card_values.append(shackle)

    # Distributing the cards
    player_cards = get_cards(card_values, card_suits)
    bot_cards = get_cards(card_values, card_suits)

    # Game variables
    round_p = round_b = draw_counter = 0
    conditional = first_score = ''

    # Round loop
    who_plays = 2 if (total_b + total_p) % 2 == 0 else 1
    while round_p < 2 and round_b < 2:

        # Showing points
        if round_p != 0 or round_b != 0:
            print(f'\n--- Pontos nessa rodada: {round_p} x {round_b} ---\n')

        # Cards and options
        if draw_counter <= 2 and conditional != 'play biggest':
            print('Suas cartas: ')
            for i in range(len(player_cards)):
                print(f'{i + 1}°: {player_cards[i][0]} de {player_cards[i][1]}')
            print('\n0: Truco\n9: Fugir')

        # First conditional
        if round_p == round_b == 0 and conditional != 'play biggest':

            # Who plays first
            if draw_counter < 2:
                if who_plays == 1:
                    result = bot_plays(card_values, card_suits, bot_cards, player_cards, conditional=conditional)
                    who_plays = 2
                else:
                    result = player_plays(card_values, card_suits, bot_cards, player_cards, conditional=conditional)
                    who_plays = 1

            # First result analysis
            if result == 1:
                if draw_counter == 1:
                    round_p += 2
                    total_p += 1
                    print('\nEmpatamos a primeira, mas você levou a segunda. Logo, você ganha!')
                else:
                    first_score = 'p'
                    round_p += 1
                    print('\nVocê venceu')
                conditional = 'p did first'
            elif result == 2:
                print('\n--- Temos um empate ---\n')
                conditional = 'draw'
                draw_counter += 1
                if draw_counter == 2:
                    conditional = 'play biggest'
            else:
                if draw_counter == 1:
                    round_b += 2
                    total_b += 1
                    print('\nEmpatamos a primeira, mas eu levei a segunda. Logo, eu ganho!')
                else:
                    first_score = 'b'
                    round_b += 1
                    print('\nEu venci')
                conditional = 'b did first'

        # Second conditional
        else:

            # if x win first, x begins next round --> second result analysis
            if conditional == 'p did first':
                result = player_plays(card_values, card_suits, bot_cards, player_cards, conditional=conditional)
                if result == 1 or result == 2:
                    round_p += 1
                    total_p += 1
                    if result == 2:
                        print('\nComo você fez a primeira, e agora empatamos, você ganha!')
                else:
                    round_b += 1
                    conditional = 'play biggest'
            elif conditional == 'b did first':
                result = bot_plays(card_values, card_suits, bot_cards, player_cards, did_first=True,
                                   conditional=conditional)
                if result == 2 or result == 3:
                    round_b += 1
                    total_b += 1
                    if result == 2:
                        print('\nComo eu fiz a primeira, e agora empatamos, eu ganho!')
                else:
                    round_p += 1
                    conditional = 'play biggest'

            # if x win and after y win -- > get higher card // if draw --> x win because he did first
            else:
                if card_values.index(player_cards[-1][0]) > card_values.index(bot_cards[-1][0]):
                    print(f'Sua: {player_cards[0][0]} de {player_cards[0][1]} '
                          f'x Minha: {bot_cards[0][0]} de {bot_cards[0][1]}')
                    print('Como a sua carta mais forte é maior, você ganha!')
                    round_p += 2
                    total_p += 1
                elif card_values.index(player_cards[-1][0]) == card_values.index(bot_cards[-1][0]):
                    print('Empatamos! Quem pontuou primeiro vence!')
                    if first_score == 'p':
                        round_p += 2
                        total_p += 1
                        print('E como essa pessoa foi você, você ganha!')
                    elif first_score == 'b':
                        round_b += 2
                        total_b += 1
                        print('E como eu fui essa pessoa (ou máquina), eu ganho!')
                    else:
                        print('Ninguem pontuou!')
                        round_p = round_b = 10
                else:
                    print(f'Sua: {player_cards[0][0]} de {player_cards[0][1]} '
                          f'x Minha: {bot_cards[0][0]} de {bot_cards[0][1]}')
                    print('Como a minha carta mais forte é maior, eu ganho!')
                    round_b += 2
                    total_b += 1
