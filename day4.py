pairs = [l.strip().split(',') for l in open("i.txt")]
contained_p1 = 0
contained_p2 = 0

for pair in pairs:
    range1 = pair[0].split('-')
    range2 = pair[1].split('-')
    pair_tuple = (  [x for x in range(int(range1[0]),int(range1[1]) + 1)],
                    [x for x in range(int(range2[0]),int(range2[1]) + 1)])
    if all(x in pair_tuple[1] for x in pair_tuple[0]) or all(x in pair_tuple[0] for x in pair_tuple[1]):
        contained_p1 += 1
    if any(x in pair_tuple[1] for x in pair_tuple[0]) or any(x in pair_tuple[0] for x in pair_tuple[1]):
        contained_p2 += 1

print("P1:",contained_p1,"P2:",contained_p2)