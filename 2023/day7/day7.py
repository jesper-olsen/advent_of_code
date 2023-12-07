import collections, glob    

# part0      6440
# part1 249726565

ORDER_CARDS = "23456789TJQKA"
ORDER_HANDS = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]

def score(hand):
    c = collections.Counter(hand)
    k = sorted(c.values())
    return (ORDER_HANDS.index(k), [ORDER_CARDS.index(x) for x in hand])

for fname in glob.glob("day7_input[01].txt"):
    g = (line.split() for line in open(fname))
    g = ((hand, int(bid)) for (hand, bid) in g)
    g = ((score(hand), int(bid)) for (hand, bid) in g)
    N = sum([(i + 1) * bid for i, (_, bid) in enumerate(sorted(g))])
    print(f"{fname}:",N)
