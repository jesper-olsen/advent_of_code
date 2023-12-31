import glob
import collections
import functools
import operator

def sample2dict(sample):
    terms = [term.split() for term in sample]
    return {label:int(cnt) for (cnt,label) in terms}

def read_games(fname):
    g=(line.strip() for line in open(fname))
    g=(line[line.index(':')+1:].split(';') for line in g if line!="")
    g=([sample.split(',') for sample in samples] for samples in g)

    for samples in g:
        yield [sample2dict(sample) for sample in samples]
 
def maxsamples(samples):
    m=collections.defaultdict(int)
    for sample in samples:
        for key in sample:
            m[key]=max(m[key], sample[key])
    return m

def possible(bag, samples):
    return all((bag[key]-sample[key]>=0 for sample in samples for key in sample))
     
for fname in glob.glob("day2_input*.txt"):
    d={"red":12, "green": 13, "blue":14}
    g=((i+1,possible(d,game)) for (i,game) in enumerate(read_games(fname)))
    g=(i for (i,flag) in g if flag)
    print(f"Problem 1, {fname}: {sum(g)}")

    g=((i+1,maxsamples(game)) for (i,game) in enumerate(read_games(fname)))
    N=sum(functools.reduce(operator.mul, d.values(), 1) for (i,d) in g)
    print(f"Problem 2, {fname}: {N}") 
