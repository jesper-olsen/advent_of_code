import glob
#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#answers: short part1:    13, part2: 30
#answers: long  part1: 32001, part2: 5037841 

def card_olaps(fname):
    for line in open(fname):
        i=line.index(':')
        j=line.index('|')
        yield len( set(line[i+1:j].split()) & set(line[j+1:].split()) )

def wcards(olap, l):
    return 1+sum([wcards(l[j], l[j:]) for j in range(1,olap+1)])

for fname in glob.glob("*input*.txt"):
    L=list(card_olaps(fname))
    N=sum((int( (o!=0) * 2**(o-1) ) for o in L))
    print(f"{fname} part1: {N}")

    N=sum([wcards(L[i],L[i:]) for i in range(len(L))])
    print(f"{fname} part2: {N}")
