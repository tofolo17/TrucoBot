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
total_p1 = total_p2 = 0
while total_p1 < 12 or total_p2 < 12:
    print(f'Placar geral: {total_p1} x {total_p2}\n')
    print('Nova rodada')
    round_p1 = round_p2 = 0
    while round_p1 < 2 or round_p2 < 2:

        # Flipped card and shackle
        flipped_card = randint(1, 10)
        print(f'Vira: {inverted_card_values[flipped_card]} de {inverted_card_suits[randint(1, 4)]}\n')
        shackle = inverted_card_values[1] if flipped_card == 10 else inverted_card_values[flipped_card + 1]

        # Distributing  the cards
        player_cards = get_cards(inverted_card_values, inverted_card_suits)
        bot_cards = get_cards(inverted_card_values, inverted_card_suits, flipped_card)

        # Cartas e opções
        print('Suas cartas: ')
        for i in range(len(player_cards)):
            print(f'{i + 1}°: {player_cards[i]}')
        print('\n0: Truco\n9: Fugir')

        # Who plays first?
        who_plays = randint(1, 2)
        if who_plays == 1:
            bot_plays(bot_cards, player_cards)
        else:
            player_plays(bot_cards, player_cards)

        break
    break


