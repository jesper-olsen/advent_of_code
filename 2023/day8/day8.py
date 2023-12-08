import glob

#answers: input0 part1:      6 
#answers: input1 part1: 618023

for fname in glob.glob("day8_input?.txt"):
    g=(line.strip() for line in open(fname))
    RL = [0 if c == 'L' else 1 for c in next(g)]
    g=((line[:3],line[7:10],line[12:15]) for line in g if line!="")
    network = {node:(l,r) for (node,l,r) in g}

    i=0
    node='AAA'
    while True:
        for rl in RL:
            node=network[node][rl]
        if node=='ZZZ': 
            print(f"{fname} part1: ", len(RL)*(i+1))
            break
        i+=1

        
