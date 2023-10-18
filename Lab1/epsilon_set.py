class EpsilonSet:

    def __init__(self):
        self.sets = dict()

    def build_e(self, state, automaton):
        if isinstance(state, set):
            state = frozenset(state)

        if state in self.sets:
            return self.sets[state]

        if not isinstance(state, frozenset):
            self.sets[state] = self.build_e({state}, automaton)
            return self.sets[state]

        res = set()
        for item in state:
            res.add(item)

            result = automaton(item, "e")

            res = res.union(result)
            res = res.union(self.build_e(result, automaton))

        self.sets[state] = frozenset(res)
        return self.sets[state]
