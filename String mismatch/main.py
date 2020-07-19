input = ['abab', 'aatacanaa', 'bbbb']
for x in input:
    sub = list()
    for i in range(1, len(x)):
        sub.append("".join([x[i:], x[:i]]))
    mismatches = list()
    mismatch = 0
    for element in sub:
        mismatch = 0
        for a, b in zip(x, element):
            if a != b:
                mismatch += 1
        mismatches.append(mismatch)
    print(max(mismatches))
