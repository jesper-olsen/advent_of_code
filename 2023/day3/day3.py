# answers prob 1: 4361, 544433
def extract_number(x,y, lines, WIDTH, HEIGHT):
    x1=x
    while x1>0 and lines[y][x1-1] in '0123456789':
        x1-=1
    x2=x
    while x2<WIDTH-1 and lines[y][x2+1] in '0123456789':
        print(f"{x1}..{x2}, {y}: {lines[y][x1:x2+1]}")
        x2+=1
    return y*WIDTH+x1,int(lines[y][x1:x2+1])
     
def find_numbers(x,y, lines, WIDTH, HEIGHT):
    print("Find", x,y)
    for (z,k) in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x+1,y-1), (x-1,y-1), (x-1,y+1)]:
        if z>=0 and z<WIDTH and k>=0 and k<HEIGHT:
             #print(z,k,lines[k][z])
             if lines[k][z] in '0123456789':
                print(extract_number(z,k, lines, WIDTH, HEIGHT))
                yield extract_number(z,k, lines, WIDTH, HEIGHT)

lines=[line.strip() for line in open("day3_input_short.txt")]
WIDTH=len(lines[0])
HEIGHT=len(lines)
#SYMBOLS=((i,c) for (i,c) in enumerate("".join(lines)) if c in "*#+$*")
SYMBOLS=((x,y) for (x,line) in enumerate(lines) for (y,c) in enumerate(line) if c not in "0123456789.")
N=0
used=set()
for (y,x) in SYMBOLS:
    for (i,n) in find_numbers(x,y, lines, WIDTH, HEIGHT):
        if not i in used:
            N+=n
            used.add(i) 
print(N)
