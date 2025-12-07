# part 1 is naive O(mn) with m = pairs and n = ids
# part 2 is O(m log m) (sort then one arithmetic pass).
# Naive solution is O(m 2^k), where k is the length of the
# smallest input line
path = './2025/day05/input.txt'


def read_input(path):
    with open(path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    fresh = []
    ids = []
    for l in lines:
        if '-' in l:
            left, right = l.split('-')
            left, right = int(left), int(right)
            fresh.append((left, right))
        elif l.isnumeric():
            ids.append(int(l))

    return fresh, ids


fresh_ranges, ids = read_input(path)


def part1():
    count = 0
    for i in ids:
        for l, u in fresh_ranges:
            if l <= i <= u:
                count += 1
                break

    return count


def part2():
    fresh_ranges.sort(key=lambda x: x[0])
    count = 0
    r_max_incl = 0
    for l_incl, r_incl in fresh_ranges:
        count += max(
            0, r_incl - l_incl + 1 if l_incl > r_max_incl else r_incl - r_max_incl
        )
        if r_incl > r_max_incl:
            r_max_incl = r_incl

    print(count)


part2()
