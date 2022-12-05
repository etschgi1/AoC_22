data = []
with open("4/inp.txt", "r") as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    fe, se = [], []
    for d in data:
        fe.append(d.split(",")[0])
        se.append(d.split(",")[1])


def checkfulloverlap(str1, str2):
    l1_min, l1_max, l2_min, l2_max = int(str1.split("-")[0]), int(
        str1.split("-")[1]), int(str2.split("-")[0]), int(str2.split("-")[1])
    if (l1_min >= l2_min and l1_max <= l2_max) or (l2_min >= l1_min and l2_max <= l1_max):
        return 1
    return 0


def checkpartialoverlap(str1, str2):
    l1_min, l1_max, l2_min, l2_max = int(str1.split("-")[0]), int(
        str1.split("-")[1]), int(str2.split("-")[0]), int(str2.split("-")[1])
    if (l1_max >= l2_min and l1_max <= l2_max) or (l2_max >= l1_min and l2_max <= l1_max):
        return 1
    return 0


count = 0
debuglist = []
for e1, e2 in zip(fe, se):
    if checkpartialoverlap(e1, e2):
        debuglist.append((e1, e2))
        count += 1
print(count)
print(debuglist[:10])
