
# Compute the Powerset of a list
# items = [1, 2]
# powerset = [[], [1], [2], [1, 2]]
import itertools

def potenzmenge(items):
    powerset = [x for length in range(len(items)+1) for x in itertools.combinations(items, length)]

    return powerset

def min_potenzmenge(items):
    powerset = [x for length in range(len(items)+1) for x in itertools.combinations(items, length)]
    return powerset