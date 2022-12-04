data = []
with open("1/inp.txt", "r") as f:
    data = f.readlines()
    data = [x.strip() for x in data]


def solve(data):
    cur_elf = 1
    running = 0
    runners_up = []
    maximum = (0, 0)
    for line in data:
        if line == "":
            runners_up.append((running, cur_elf))
            if running > maximum[0]:
                maximum = (running, cur_elf)
            cur_elf += 1
            running = 0
        else:
            running += int(line)
    top_3_sum = sum([x[0] for x in sorted(
        runners_up, key=lambda x: x[0], reverse=True)[:3]])
    return maximum, top_3_sum


print(solve(data))
