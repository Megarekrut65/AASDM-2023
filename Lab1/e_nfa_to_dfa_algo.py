import finite_automaton as fa
import epsilon_set as e_set


def e_nfa_to_dfa(automaton):
    """
    Algorithm of converting e-NFA to DFA
    :param automaton: Finite automaton(e-NFA)
    :return: Finite automaton(DFA)
    """
    epsilon = e_set.EpsilonSet()

    result = fa.FiniteAutomaton(set(), automaton.alphabet, dict(), None, set())

    result.begin = epsilon.build_e(automaton.begin, automaton)
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
                element = epsilon.build_e(automaton(item, sign), automaton)
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
    """
    Renames sets of old states to new names. Example: state {1,2,3} will be state a1.
    :param automaton: FA
    :return: FA with same states but other names of states
    """
    states = set()
    transitions = dict()

    names = dict()
    i = 0
    for state in automaton.states:
        names[frozenset(state)] = f"a{i}"
        if len(frozenset(state)) != 0:
            states.add(names[frozenset(state)])
            i += 1

    names[frozenset({})] = ""

    for key, value in automaton.transitions.items():
        new_key = (names[key[0]], key[1])
        transitions[new_key] = {names[item] for item in value}

    finals = {names[item] for item in automaton.finals}

    return fa.FiniteAutomaton(states, automaton.alphabet, transitions, names[automaton.begin], finals), names
