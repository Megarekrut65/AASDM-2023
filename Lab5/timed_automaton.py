class TimedAutomaton:
    def __init__(self):
        self.states = {'a0', 'a1', 'a2'}
        self.initial_states = {'a0'}
        self.alphabet = {'a', 'b'}
        self.transitions = [
            (('a0', 0), 'a', ('a0', 0), 'x<1'),
            (('a0', 0), 'a', ('a1', 0), 'x=1'),
            (('a1', 0), 'b', ('a0', 1), 'y<1'),
            (('a1', 0), 'a', ('a2', 0), 'x<2'),
            (('a2', 1), 'b', ('a1', 1), 'y=1'),
            (('a2', 0), 'a', ('a2', 1), 'x<1'),
        ]
