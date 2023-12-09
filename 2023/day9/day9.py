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
            row = [rows[-1][i]-rows[-1][i-1] for i in range(1,len(rows[-1]))]
            rows+=[row]
        first, last = 0, 0
        for i,row in enumerate(rows[::-1]):
            erow=[row[0]-first]+row+[row[-1]+last]
            rows[len(rows)-1-i]=erow
            first, last = erow[0], erow[-1]
        psum = (psum[0] + rows[0][0], psum[1] + rows[0][-1])
    print(f"{fname} part1:", psum[1])
    print(f"{fname} part2:", psum[0])
