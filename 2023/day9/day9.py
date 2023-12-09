""" advent of code 2023-12-9
answers: input0 part1:        114 part2:   2
answers: input1 part1: 1972648895 part2: 919
"""
import glob

for fname in sorted(glob.glob("day9_input?.txt")):
    g = (line.strip() for line in open(fname, encoding="ascii"))
    psum = (0, 0)
    for history in ([int(w) for w in line.split()] for line in g):
        rows = [history]
        while any(x!=0 for x in rows[-1]):
            diff=[rows[-1][i]-rows[-1][i-1] for i in range(1,len(rows[-1]))]
            rows+=[diff]
        ht=(0,0)
        while rows!=[]:
            row=rows.pop()
            ht=(row[0]-ht[0],row[-1]+ht[1])
        psum = (psum[0] + ht[0], psum[1] + ht[-1])
    print(f"{fname} part1:", psum[1])
    print(f"{fname} part2:", psum[0])
