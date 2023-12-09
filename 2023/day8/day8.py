""" advent of code 2023-12-8
answers: input0 part1:     6 part2:              6
answers: input1 part1: 18023 part2: 14449445933179
"""
import glob
import itertools
import math

def steps_to_end(node, network, inst, end_nodes):
    for i, rl in enumerate(itertools.cycle(inst)):
        node = network[node][rl]
        if node in end_nodes:
            return i + 1

for fname in sorted(glob.glob("day8_input?.txt")):
    g = (line.strip() for line in open(fname, encoding="ascii"))
    inst = [0 if c == "L" else 1 for c in next(g)]
    network = {line[:3]: (line[7:10], line[12:15]) for line in g if line != ""}

    print(f"{fname} part1: ", steps_to_end("AAA", network, inst, ["ZZZ"]))

    start_nodes = [node for node in network.keys() if node[-1] == "A"]
    end_nodes = [node for node in network.keys() if node[-1] == "Z"]
    l = [steps_to_end(node, network, inst, end_nodes) for node in start_nodes]
    print(f"{fname} part2: ", math.lcm(*l))
