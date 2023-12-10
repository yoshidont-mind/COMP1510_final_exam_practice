import itertools

# count_with_floats = itertools.count(start=0.5, step=0.75)
# float_sequence = []
# for _ in range(5):
#     float_sequence.append(next(count_with_floats))
# print(float_sequence)
# next_value = next(count_with_floats)
# print(next_value)

# choices = []
# boolean_generator = itertools.cycle([True, False])
# for _ in range(20):
#     choices.append(next(boolean_generator))
# print(choices)

# primary_colours = ['cyan', 'magenta', 'yellow']
# permutations = list(itertools.permutations(primary_colours))
#
# print("There are %d permutations: " % len(permutations))
#
# for sequence_number, permutation in enumerate(permutations, 1):
#     print("%d:\t%s" % (sequence_number, permutation))

# size = 2
# combos = list(itertools.combinations(
#     ["ginger", "allspice", "cumin", "mint"], size
# ))
# print("There are %d combos of size %d: " % (len(combos), size))
# for seq_number, combo in enumerate(combos, 1):
#     print("%d:\t%s" % (seq_number, combo))

pairs = []
names = ("A", "B", "C", "D")
for pair in zip(itertools.count(1), names):
    pairs.append(pair)
print(pairs)
