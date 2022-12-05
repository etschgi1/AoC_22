data = []
with open("5/inp.txt", "r") as f:
    data = f.readlines()
# split data:
index_empty = data.index("\n")
nr_stacks = int(data[index_empty-1].split("   ")[-1].strip())
stacks = [[] for i in range(nr_stacks)]
for line in data[:index_empty-1]:
    for c, pos in enumerate([4*x+1 for x in range(nr_stacks)]):  # check positions
        if line[pos].isupper():
            stacks[c].append(line[pos])
stacks = [list(reversed(l)) for l in stacks]
movement_data = [x.strip() for x in data[index_empty+1:]]

SECOND = True


def rearrange(stacks, movement_data):
    for move in movement_data:
        nr_, from_, to_ = int(move.split(" ")[1]), int(
            move.split(" ")[3]), int(move.split(" ")[5])
        if SECOND:
            if nr_ == 1:
                stacks[to_-1].append(stacks[from_-1].pop())
            else:
                for c in reversed(list(range(nr_))):
                    stacks[to_-1].append(stacks[from_-1].pop(-(c+1)))
        else:
            for c in range(nr_):
                stacks[to_-1].append(stacks[from_-1].pop())


rearrange(stacks, movement_data)
for c, s in enumerate(stacks):
    print(s[-1], end="")
