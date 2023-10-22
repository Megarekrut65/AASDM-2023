import json


class MooreAutomaton:
    def __init__(self, states, input_alphabet, output_alphabet, transition_function, output_function):
        self.states = states  # A
        self.input_alphabet = input_alphabet  # X
        self.output_alphabet = output_alphabet  # Y
        self.transition_function = transition_function  # f
        self.output_function = output_function  # g

    def build_e(self, state):
        e = set()

        for s in self.states:
            equivalent = True
            for x in self.input_alphabet:
                if self.transition_function[(s, x)] != self.transition_function[(state, x)]:
                    equivalent = False
                    break
            if equivalent:
                e.add(s)

        return e

    def to_json(self):
        moore_automaton_data = {
            "states": list(self.states),
            "input_alphabet": list(self.input_alphabet),
            "output_alphabet": list(self.output_alphabet),
            "transition_function": {str(key): list(value) for key, value in self.transition_function.items()},
            "output_function": {str(key): list(value) for key, value in self.output_function.items()},
        }
        return json.dumps(moore_automaton_data, indent=4)

    @classmethod
    def from_json(cls, json_str):
        moore_automaton_data = json.loads(json_str)
        states = set(moore_automaton_data["states"])
        input_alphabet = set(moore_automaton_data["input_alphabet"])
        output_alphabet = set(moore_automaton_data["output_alphabet"])

        transition_function = {eval(key): set(value) for key, value in
                               moore_automaton_data["transition_function"].items()}
        output_function = {eval(key): set(value) for key, value in moore_automaton_data["output_function"].items()}
        return cls(states, input_alphabet, output_alphabet, transition_function, output_function)
