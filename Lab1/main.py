import finite_automaton as fa


def main():
    automaton = fa.FiniteAutomaton({0, 1, 2}, {"a", "b", "e"},
                                   dict({
                                       (0, "a"): 0,
                                       (0, "b"): 2,
                                       (0, "e"): 1,
                                       (1, "a"): 0,
                                       (1, "b"): 2,
                                       (1, "e"): 2,
                                       (2, "a"): 2,
                                       (2, "b"): [1, 2],
                                   }), 0, {2})
    print(automaton)


if __name__ == "__main__":
    main()
