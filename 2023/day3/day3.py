import glob
import functools
import operator
# answers prob 1: 4361, 544433
# answers prob 2: 467835, 76314915 

def extract_number(x,y, lines, WIDTH):
    x1=x
    while x1>0 and lines[y][x1-1].isdigit():
        x1-=1
    x2=x
    while x2<WIDTH-1 and lines[y][x2+1].isdigit():
        x2+=1
    return y*WIDTH+x1,int(lines[y][x1:x2+1])
     
def find_numbers(x,y, lines, WIDTH, HEIGHT):
    used=set()
    for (z,k) in [(x+u,x+v) for u in (-1,0,1) for v in (-1,0,1) if (u,v)!=(0,0)]:
        if z>=0 and z<WIDTH and k>=0 and k<HEIGHT:
             if lines[k][z].isdigit():
                q,n=extract_number(z,k, lines, WIDTH)
                if not q in used:
                    used.add(q)
                    yield n

for fname in glob.glob("day3_input*.txt"):
    lines=[line.strip() for line in open(fname)]
    WIDTH=len(lines[0])
    HEIGHT=len(lines)
    SYMBOLS=((x,y) for (y,line) in enumerate(lines) for (x,c) in enumerate(line) if c not in "0123456789.")
    N=sum([n for (x,y) in SYMBOLS for n in find_numbers(x,y,lines,WIDTH,HEIGHT)])
    print(f"Problem 1, {fname}: {N}")

    GEARS=((x,y) for (y,line) in enumerate(lines) for (x,c) in enumerate(line) if c in "*")

    N=0
    for (x,y) in GEARS:
        l=[n for n in find_numbers(x,y, lines, WIDTH, HEIGHT)]
        if len(l)>1:
            N+=functools.reduce(operator.mul, l, 1)
 
    print(f"Problem 2, {fname}: {N}")
