from Lab2.moore_mealy_automaton import MooreMealyAutomaton


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
