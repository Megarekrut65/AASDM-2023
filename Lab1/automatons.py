import finite_automaton as fa


automaton1 = fa.FiniteAutomaton({0, 1, 2, 3}, {"a", "b", "c"},
                                dict({
                                    (0, "a"): {0, 1, 2, 3},
                                    (0, "b"): {1, 2},
                                    (0, "e"): {1},
                                    (1, "c"): {2},
                                    (1, "b"): {1},
                                    (1, "e"): {2},
                                    (2, "c"): {2},
                                    (3, "e"): {0},
                                }), 0, {2})
