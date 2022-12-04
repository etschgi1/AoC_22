data = []
with open("3/inp.txt", "r") as f:
    data = f.readlines()
    data = [x.strip() for x in data]


def transform(data):  # transform into numbers
    temp = []
    for d in data:
        t = []
        for l in d:
            t.append(ord(l)-38 if l.isupper() else ord(l)-96)
        temp.append(t)
    l, out = [], []
    for c, e in enumerate(temp):
        l.append(e)
        if c % 3 == 2:
            out.append(l)
            l = []
    return out


data = transform(data)
priorities = []
for triple in data:
    f, s, t = triple
    for fe in f:
        if fe in s:
            if fe in t:
                priorities.append(fe)
                break

print(sum(priorities))
