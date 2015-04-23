l = {'T': 10, 'J':11, 'Q':12, 'K':13, 'A':14}


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    ranks = [l[r] if r in l else int(r) for r in ranks]
    ranks.sort(reverse=True)
    return ranks


print(card_ranks(['AC', '3D', '4S', 'KH']))#should output [14, 13, 4, 3]