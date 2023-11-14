class BuchiTimeAutomaton:
    def __init__(self, states, alphabet, begins, clocks, transitions, variants, finals):
        """

        :param states: A
        :param alphabet: X
        :param begins: A0
        :param clocks: Y
        :param transitions: E
        :param variants: I
        :param finals: F
        """
        self.states = states
        self.alphabet = alphabet
        self.begins = begins
        self.clocks = clocks
        self.transitions = transitions
        self.variants = variants
        self.finals = finals

