import finite_automaton as fa


def build_e(state, automaton):

    if not isinstance(state, set):
        return build_e({state}, automaton)

    res = set()
    for item in state:
        res.add(item)

        result = automaton(item, "e")

        res = res.union(result)
        res = res.union(build_e(result, automaton))

    return frozenset(res)


def to_deterministic(automaton):
    result = fa.FiniteAutomaton(set(), automaton.alphabet, dict(), None, set())

    result.begin = build_e(automaton.begin, automaton)
    result.states.add(result.begin)
    states = {result.begin}

    if len(result.begin.intersection(automaton.finals)) != 0:
        result.finals.add(result.begin)

    removed = set()

    while len(states) != 0:
        state = next(iter(states))
        removed.add(state)

        for sign in automaton.alphabet:
            new_state = frozenset()
            for item in state:
                element = build_e(automaton(item, sign), automaton)
                new_state = new_state.union(element)

            if len(new_state.intersection(automaton.finals)) != 0:
                result.finals.add(new_state)

            result.states.add(new_state)

            if (state, sign) in result.transitions:
                result.transitions[(state, sign)].add(new_state)
            else:
                result.transitions[(state, sign)] = {new_state}

            if not (new_state in removed):
                states.add(new_state)
        states.remove(state)

    return result


def rename_states(automaton):
    states = set()
    transitions = dict()

    names = dict()
    for i, state in enumerate(automaton.states):
        names[frozenset(state)] = f"a{i}"
        states.add(names[frozenset(state)])

    names[frozenset({})] = ""

    for key, value in automaton.transitions.items():
        new_key = (names[key[0]], key[1])
        transitions[new_key] = {names[item] for item in value}

    finals = {names[item] for item in automaton.finals}

    return fa.FiniteAutomaton(states, automaton.alphabet, transitions, names[automaton.begin], finals), names


def main():
    """automaton = fa.FiniteAutomaton({0, 1, 2}, {"a", "b", "e"},
                                   dict({
                                       (0, "a"): {0},
                                       (0, "b"): {2},
                                       (0, "e"): {1},
                                       (1, "a"): {0},
                                       (1, "b"): {2},
                                       (1, "e"): {2},
                                       (2, "a"): {2},
                                       (2, "b"): {1, 2},
                                   }), 0, {2})
    """
    """automaton = fa.FiniteAutomaton({0, 1, 2, 3}, {"a", "b", "c"},
                                   dict({
                                       (0, "a"): {0, 1, 2, 3},
                                       (0, "b"): {1, 2},
                                       (0, "e"): {1},
                                       (1, "c"): {2},
                                       (1, "b"): {1},
                                       (1, "e"): {2},
                                       (2, "c"): {2},
                                       (3, "e"): {0},
                                   }), 0, {2})"""
    automaton = fa.FiniteAutomaton({"s", "g", "a", "f"}, {"1", "0"},
                                   dict({
                                       ("s", "1"): {"a", "s", "f"},
                                       ("s", "e"): {"f"},
                                       ("a", "e"): {"s", "f"},
                                       ("s", "0"): {"g"},
                                       ("a", "1"): {"a", "s", "f"},
                                       ("a", "0"): {"f"}
                                   }), "s", {"f", "g"})

    result = to_deterministic(automaton)
    print(result)

    renamed, names = rename_states(result)
    print(names)
    print(renamed)


if __name__ == "__main__":
    main()
