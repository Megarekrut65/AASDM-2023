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
        if len(frozenset(state)) != 0:
            states.add(names[frozenset(state)])

    names[frozenset({})] = ""

    for key, value in automaton.transitions.items():
        new_key = (names[key[0]], key[1])
        transitions[new_key] = {names[item] for item in value}

    finals = {names[item] for item in automaton.finals}

    return fa.FiniteAutomaton(states, automaton.alphabet, transitions, names[automaton.begin], finals), names


def main():
    with open("automatons.json") as file:
        automaton = fa.FiniteAutomaton.from_json(file.read())

    print(automaton)

    result = to_deterministic(automaton)
    print(result)

    renamed, names = rename_states(result)
    print(names)
    print(renamed)

    """file = open("automatons.json", "w")
    file.write(automaton.to_json())
    file.close()"""


if __name__ == "__main__":
    main()
