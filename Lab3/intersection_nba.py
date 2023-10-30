import buchi_automaton as ba


def inter_nba(automaton1, automaton2):
    begin = (list(automaton1.begins)[0], list(automaton2.begins)[0], 1)

    result = ba.BuchiAutomaton(set(), automaton1.alphabet, dict(), {begin}, set())

    set_w = {begin}

    while len(set_w) != 0:
        state = set_w.pop()
        a, b, i = state

        result.states.add(state)
        if a in automaton1.finals and i == 1:
            result.finals.add(state)

        for x in automaton1.alphabet:
            res1 = automaton1(a, x)
            res2 = automaton2(b, x)

            for item_a in res1:
                for item_b in res2:
                    new_state = None
                    if i == 1 and a not in automaton1.finals:
                        new_state = (item_a, item_b, 1)
                    elif i == 1 and a in automaton1.finals:
                        new_state = (item_a, item_b, 2)
                    elif i == 2 and b not in automaton2.finals:
                        new_state = (item_a, item_b, 2)
                    elif i == 2 and b in automaton2.finals:
                        new_state = (item_a, item_b, 1)

                    if new_state is None:
                        continue

                    if (state, x) in result.transitions:
                        result.transitions[(state, x)].add(new_state)
                    else:
                        result.transitions[(state, x)] = {new_state}
                    if new_state not in result.states:
                        set_w.add(new_state)

    return result
