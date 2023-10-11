class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, begin, finals):
        """
        :param states: set of states A
        :param alphabet: set of signs X
        :param transitions: transition function f
        :param begin: begin state
        :param finals: set of final stales F
        """
        self.states = states  # A
        self.alphabet = alphabet  # X
        self.transitions = transitions  # f
        self.begin = begin  # a0
        self.finals = finals  # F

    def __str__(self):
        transitions = ""
        for key in self.transitions:
            transitions += f"{key} -> {self.transitions[key]}\n"

        return f"A={self.states}\nX={self.alphabet}\nf=\n{transitions}\na0={self.begin}\nF={self.finals}\n\n"

    def __call__(self, state, sign):

        return self.transitions.get((state, sign), set())
