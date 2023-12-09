""" advent of code 2023-12-9
answers: input0 part1:     6 part2:              6
answers: input1 part1: 18023 part2: 14449445933179
"""
import glob
import itertools
import math

for fname in sorted(glob.glob("day9_input1.txt")):
    g = (line.strip() for line in open(fname, encoding="ascii"))
    l=[]
    for line in g:
        rows=[[int(w) for w in line.split()]]
        while not all(n==0 for n in rows[-1]):
            row=[rows[-1][i]-rows[-1][i-1] for i in range(1,len(rows[-1]))]
            rows+=[row]
        print(rows)
        last=0
        for row in rows[::-1]:
            row+=[row[-1]+last]
            last=row[-1]

        l+=[rows[0][-1]]
    print("part1:", sum(l))

    g = (line.strip() for line in open(fname, encoding="ascii"))
    l=[]
    for line in g:
        rows=[[int(w) for w in line.split()]]
        while not all(n==0 for n in rows[-1]):
            row=[rows[-1][i]-rows[-1][i-1] for i in range(1,len(rows[-1]))]
            rows+=[row]
        print(rows)
        first=0
        for row in rows[::-1]:
            row.insert(0,row[0]-first)
            first=row[0]
        print("Predict first")
        print(rows)

        l+=[rows[0][0]]
    print("part2:", sum(l))
