import collections, glob

# example part0      6440 part2 5905
# problem part1 249726565 part2 251135960

ORDER_HANDS = [
    [1, 1, 1, 1, 1], #high card
    [1, 1, 1, 2],    #1 pair
    [1, 2, 2],       #2 pairs 
    [1, 1, 3],       #3 of a kind
    [2, 3],          #full house
    [1, 4],          #4 of a kind
    [5]              #5 of a kind
]

def score(hand):
    return (score_type(hand), score_cards(hand))

def score_type(hand):
    c = collections.Counter(hand)
    k = sorted(c.values())
    return ORDER_HANDS.index(k)

def score_type_J(hand):
    i=hand.find('J')
    if i!=-1:
        return max([score_type_J(xhand) for xhand in [hand[:i]+x+hand[i+1:] for x in set(ORDER_CARDS)-set('J')]])
    return score_type(hand)

def score_cards(hand):
    return [ORDER_CARDS.index(x) for x in hand]


ORDER_CARDS = "23456789TJQKA"
for fname in glob.glob("day7_input[01].txt"):
    g = (line.split() for line in open(fname))
    g = (((score_type(hand),score_cards(hand)), int(bid)) for (hand, bid) in g)
    N = sum([(i + 1) * bid for i, (_, bid) in enumerate(sorted(g))])
    print(f"{fname} part1: ",N)

ORDER_CARDS = "J23456789TQKA"
for fname in glob.glob("day7_input[01].txt"):
    g = (line.split() for line in open(fname))
    g = (((score_type_J(hand),score_cards(hand)), int(bid)) for (hand, bid) in g)
    N = sum([(i + 1) * bid for i, (_, bid) in enumerate(sorted(g))])
    print(f"{fname} part2: ",N)
