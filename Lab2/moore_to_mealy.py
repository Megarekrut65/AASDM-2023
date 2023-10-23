from moore_mealy_automaton import MooreMealyAutomaton


def moore_to_mealy(moore):
    new_states = {frozenset(moore.build_e(s)) for s in moore.states}
    new_input_alphabet = moore.input_alphabet.copy()
    new_output_alphabet = moore.output_alphabet.copy()
    new_transition_function, new_output_function = dict(), dict()

    for state in moore.states:
        for letter in moore.input_alphabet:
            tf = moore.transition_function
            if (state, letter) in tf and tf[(state, letter)] in moore.output_function:
                e_state = frozenset(moore.build_e(state))
                new_transition_function[(e_state, letter)] = moore.build_e(tf[(state, letter)])
                new_output_function[(e_state, letter)] = moore.output_function[tf[(state, letter)]]

    return MooreMealyAutomaton(
        new_states,
        new_input_alphabet,
        new_output_alphabet,
        new_transition_function,
        new_output_function
    )


def rename_states(automaton):
    """
    Renames sets of old states to new names. Example: state {1,2,3} will be state a1.
    :param automaton: Mealy FA
    :return: Mealy FA with same states but other names of states
    """

    states = set()
    transitions = dict()
    output = dict()

    names = dict()
    for index, state in enumerate(automaton.states):
        names[frozenset(state)] = f"a{index}"
        states.add(names[frozenset(state)])

    for key, value in automaton.transition_function.items():

        new_key = (names[key[0]], key[1])
        transitions[new_key] = {names[value]}

    for key, value in automaton.output_function.items():
        new_key = (names[key[0]], key[1])
        output[new_key] = value

    return MooreMealyAutomaton(
        states,
        automaton.input_alphabet,
        automaton.output_alphabet,
        transitions,
        output
    ), names
