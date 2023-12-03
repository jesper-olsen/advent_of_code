import glob
import functools
import operator
# answers prob 1: 4361, 544433
# answers prob 2: 467835, 76314915 

def extract_number(x, line):
    i=x
    while i>0 and line[i-1].isdigit():
        i-=1
    j=x
    while j<len(line)-1 and line[j+1].isdigit():
        j+=1
    return i,j
     
def find_numbers(x,y, lines, WIDTH):
    used=set()
    for (z,k) in [(x+u,y+v) for u in (-1,0,1) for v in (-1,0,1) if (u,v)!=(0,0)]:
        if z>=0 and z<WIDTH and k>=0 and k<len(lines):
             if lines[k][z].isdigit() and not k*WIDTH+z in used:
                i,j=extract_number(z, lines[k])
                used |= set([k*WIDTH+q for q in range(i,j+1)])
                yield int(lines[k][i:j+1])

for fname in glob.glob("day3_input*.txt"):
    lines=[line.strip() for line in open(fname)]
    WIDTH=len(lines[0])
    SYMBOLS=((x,y) for (y,line) in enumerate(lines) for (x,c) in enumerate(line) if c not in "0123456789.")
    N=sum([n for (x,y) in SYMBOLS for n in find_numbers(x,y,lines,WIDTH)])
    print(f"Problem 1, {fname}: {N}")

    GEARS=((x,y) for (y,line) in enumerate(lines) for (x,c) in enumerate(line) if c in "*")

    N=0
    for (x,y) in GEARS:
        l=[n for n in find_numbers(x,y, lines, WIDTH)]
        if len(l)>1:
            N+=functools.reduce(operator.mul, l, 1)
    print(f"Problem 2, {fname}: {N}")
