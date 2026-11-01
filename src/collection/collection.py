from itertools import combinations, permutations
import builtins


class Collection:
    """Operations on collections. Each Collection() is a new object."""

    def contains(self, s, e):
        """Count occurrences of e in s."""
        return sum(1 for item in s if item == e)

    def zip(self, s, p):
        """Return pairs, stopping when the shorter sequence ends."""
        return list(builtins.zip(s, p))

    def pset(self, s):
        """Return subsets as tuples, ignoring repeated input items."""
        items = []
        for item in s:
            if item not in items:
                items.append(item)
        return [
            subset
            for size in range(len(items) + 1)
            for subset in combinations(items, size)
        ]

    def perm(self, p):
        """Return distinct arrangements as tuples."""
        result = []
        for arrangement in permutations(p):
            if arrangement not in result:
                result.append(arrangement)
        return result
