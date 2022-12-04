data = []
with open("3/inp.txt", "r") as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    temp = []
    for d in data:
        temp.append(d[:int(len(d)/2)])  # split
        temp.append(d[int(len(d)/2):])
    data = temp


def transform(data):  # transform into numbers
    new_data1, new_data2 = [], []
    temp = [new_data1, new_data2]
    for c, d in enumerate(data):
        t = []
        for l in d:
            t.append(ord(l)-38 if l.isupper() else ord(l)-96)
        temp[c % 2].append(t)
    return (temp[0], temp[1])


d1, d2 = transform(data)
priorities = []
for fc, sc in zip(d1, d2):
    for ef in fc:
        if ef in sc:
            priorities.append(ef)
            break
print(sum(priorities))
