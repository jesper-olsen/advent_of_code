import glob
import itertools
import math

# answers: input0 part1:     6 part2:              6
# answers: input1 part1: 18023 part2: 14449445933179

def steps_to_end(node, network, RL, end_nodes):
    for i, rl in enumerate(itertools.cycle(RL)):
        node = network[node][rl]
        if node in end_nodes:
            return i + 1

for fname in sorted(glob.glob("day8_input?.txt")):
    g = (line.strip() for line in open(fname))
    RL = [0 if c == "L" else 1 for c in next(g)]
    g = ((line[:3], line[7:10], line[12:15]) for line in g if line != "")
    network = {node: (l, r) for (node, l, r) in g}

    print(f"{fname} part1: ", steps_to_end("AAA", network, RL, ["ZZZ"]))

    start_nodes = [node for node in network.keys() if node[-1] == "A"]
    end_nodes = [node for node in network.keys() if node[-1] == "Z"]
    l = [steps_to_end(node, network, RL, end_nodes) for node in start_nodes]
    print(f"{fname} part2: ", math.lcm(*l)) 
