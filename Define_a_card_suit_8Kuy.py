# def define_suit(card):
#
#         if card[-1] in 'C':
#             return 'clubs'
#         elif card[-1] == 'D':
#             return 'diamonds'
#         elif card[-1] == 'H':
#             return 'hearts'
#         else:
#             return 'spades'


def define_suit(card):

    d = {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}
    return d[card[-1]]


DECK = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC']

print(define_suit('QS'))