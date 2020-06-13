
class Span:
    """
    Span objects are used to define boundaries within other iterables.
    """
    def __init__(self, start, end):
        if not start <= end:
            raise ValueError('Start cannot be greater than or equal to End')

        self._start = start
        self._end = end

    @property
    def span(self):
        """
        Return the span start and end scalars
        :return: The start and end indexes
        """
        return self._start, self._end

    def __eq__(self, other):
        start, fin = other.span()
        return self._start == start and self._end == fin


def subst(source, target, cost):
    if source == target:
        return 0
    return cost
    pass


class DistanceCalculator:
    """
    The ADistanceCalculator class defines a metric on strings. It is a way of determining the distance from
    one string to another.
    """

    def __init__(self, insert_cost=1, deletion_cost=1, subst_cost=1):
        """
        The constructor for the distance calculator. The insert, deletion, and substitution cost can be specified
        as state for the object.
        :param insert_cost:
        :param deletion_cost:
        :param subst_cost:
        """
        self._insert_cost = insert_cost
        self._deletion_cost = deletion_cost
        self._subst_cost = subst_cost

    def distance(self, source, target):
        """
        Calculates the distance between two strings.
        :param source: The source string
        :param target: The target string
        :return: The scalar distance between the source and target.
        """
        m = len(source)
        n = len(target)
        dist = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            dist[i][0] = dist[i - 1][0] + self._deletion_cost
        for j in range(1, m + 1):
            dist[0][j] = dist[0][j - 1] + self._insert_cost
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                dist[i][j] = min(dist[i - 1][j] + self._insert_cost,
                                 dist[i][j - 1] + self._deletion_cost,
                                 dist[i - 1][j - 1] + subst(source[j - 1], target[i - 1], self._subst_cost))
        return dist[n][m]
