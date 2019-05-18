
# Compute the Powerset of a list
# items = [1, 2]
# powerset = [[], [1], [2], [1, 2]]
import itertools

items = [1, 2, 3, 4]
powerset = [x for length in range(len(items)+1) for x in itertools.combinations(items, length)]