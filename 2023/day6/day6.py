# times = [7, 15, 30]
# dists = [9, 40, 200]

def calc_beats_prod(times, dist):
    F = 1
    for i, t in enumerate(times):
        n = sum([1 for hold in range(1, t) if (t - hold) * hold > dist[i]])
        F *= n
    return F

for fname in ["day6_input.txt"]:
    g = (line.split(":")[1] for line in open(fname))
    g = [[int(w) for w in l.split()] for l in g]
    times, dists = g
    print("Part1: ", calc_beats_prod(times, dists))

    times = [int("".join(map(str, times)))]
    dists = [int("".join(map(str, dists)))]
    print("Part2: ", calc_beats_prod(times, dists))
