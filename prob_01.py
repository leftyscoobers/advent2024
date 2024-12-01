input_file = 'input_01.txt'
raw_data = open(input_file, 'r').readlines()

def split_lists(raw_string):
    pair = raw_string.strip().split()
    return [int(i) for i in pair]

loc_as_ints = [split_lists(l) for l in raw_data]
l1 = sorted([pairs[0] for pairs in loc_as_ints])
l2 = sorted([pairs[1] for pairs in loc_as_ints])

diffs = [abs(x - y) for x, y in zip(l1, l2)]

print(f'Part 1: {sum(diffs)}')

# Find count of each number in list 1
# And find count of each number in list 2, then mult by list 1 count
set_of_l1 = set(l1)
similiarty_scores = []
for n in set_of_l1:
    l1_count = l1.count(n)
    l2_count = l2.count(n)
    similiarty_scores.append(n * l1_count * l2_count)

print(f'Part 2: {sum(similiarty_scores)}')
