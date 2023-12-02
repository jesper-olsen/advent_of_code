import glob
from collections import defaultdict
import functools
import operator
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

def sample2dict(sample):
    terms = [term.split() for term in sample]
    terms = {label:int(cnt) for (cnt,label) in terms}
    return terms

def read_games(fname):
    g=(line.strip() for line in open(fname))
    g=(line[line.index(':')+1:].split(';') for line in g if line!="")
    g=([sample.split(',') for sample in samples] for samples in g)

    for samples in g:
        yield [sample2dict(sample) for sample in samples]
 
def maxsamples(samples):
    m=defaultdict(int)
    for sample in samples:
        for key in sample:
            m[key]=max(m[key], sample[key])
    return m

def possible(bag, samples):
    d={"red":12, "green": 13, "blue":14}
    for key in bag:
        for sample in samples:
            if key in sample and bag[key]-sample[key]<0:
                return False
    return True
     
foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)

for fname in glob.glob("day2*input*.txt"):
    d={"red":12, "green": 13, "blue":14}
    g=((i+1,possible(d,game)) for (i,game) in enumerate(read_games(fname)))
    g=(i for (i,flag) in g if flag)
    print(f"Problem 1, {fname}: {sum(g)}")

    g=((i+1,maxsamples(game)) for (i,game) in enumerate(read_games(fname)))
    N=sum(foldl(operator.mul, 1, d.values()) for (i,d) in g)
    print(f"Problem 2, {fname}: {N}") 
