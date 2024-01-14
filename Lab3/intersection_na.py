import buchi_automaton as ba


def inter_nba(automaton1, automaton2):
    begin = (list(automaton1.begins)[0], list(automaton2.begins)[0], 1)

    result = ba.BuchiAutomaton(set(), automaton1.alphabet, dict(), {(begin[0], begin[1])}, set())

    set_w = {begin}
    names = {(begin[0], begin[1]): begin}

    while len(set_w) != 0:
        state = set_w.pop()
        a, b, i = state

        result.states.add((a, b))
        if a in automaton1.finals and b in automaton2.finals:
            result.finals.add((a, b))
            names[(a, b)] = state

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

                    if (item_a, item_b) not in names:
                        names[(item_a, item_b)] = new_state

                    if ((a, b), x) in result.transitions:
                        result.transitions[((a, b), x)].add((item_a, item_b))
                    else:
                        result.transitions[((a, b), x)] = {(item_a, item_b)}
                    if (item_a, item_b) not in result.states:
                        set_w.add(new_state)


    return result
