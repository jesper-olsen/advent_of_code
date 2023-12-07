import collections, glob

# example part1      6440 part2      5905
# problem part1 249726565 part2 251135960

def score_type(hand, card_order):
    c = collections.Counter(hand)
    k = sorted(c.values())
    return [
        [1, 1, 1, 1, 1],  # high card
        [1, 1, 1, 2],  # 1 pair
        [1, 2, 2],  # 2 pairs
        [1, 1, 3],  # 3 of a kind
        [2, 3],  # full house
        [1, 4],  # 4 of a kind
        [5],  # 5 of a kind
    ].index(k)

def score_type_J(hand, card_order):
    i = hand.find("J")
    if i != -1:
        return max(
            [
                score_type_J(xhand, card_order)
                for xhand in [
                    hand[:i] + x + hand[i + 1 :] for x in set(card_order) - set("J")
                ]
            ]
        )
    return score_type(hand, card_order)

def calc_total_score(L, card_order, score_type):
    g = (
        (
            (score_type(hand, card_order), [card_order.index(x) for x in hand]),
            int(bid),
        )
        for (hand, bid) in L
    )
    return sum([(i + 1) * bid for i, (_, bid) in enumerate(sorted(g))])

for fname in glob.glob("day7_input[01].txt"):
    L = [line.split() for line in open(fname)]
    print(f"{fname} part1: ", calc_total_score(L, "23456789TJQKA", score_type))
    print(f"{fname} part2: ", calc_total_score(L, "J23456789TQKA", score_type_J))
