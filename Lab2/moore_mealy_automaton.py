import json


class MooreMealyAutomaton:
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

        return frozenset(e)

    def __str__(self):
        transition_function = ""
        for key in self.transition_function:
            transition_function += f"{key} -> {self.transition_function[key]}\n"

        output_function = ""
        for key in self.output_function:
            output_function += f"{key} -> {self.output_function[key]}\n"

        return f"A={self.states}\nX={self.input_alphabet}\nY={self.output_alphabet}\nf=\n{transition_function}\ng=\n{output_function}\n\n"

    def to_json(self):
        automaton_data = {
            "states": list(self.states),
            "input_alphabet": list(self.input_alphabet),
            "output_alphabet": list(self.output_alphabet),
            "transition_function": {str(key): list(value) for key, value in self.transition_function.items()},
            "output_function": {str(key): list(value) for key, value in self.output_function.items()},
        }

        return json.dumps(automaton_data, indent=2)

    @classmethod
    def from_json(cls, json_str):
        automaton_data = json.loads(json_str)
        states = set(automaton_data["states"])
        input_alphabet = set(automaton_data["input_alphabet"])
        output_alphabet = set(automaton_data["output_alphabet"])

        transition_function = {eval(key): value for key, value in
                               automaton_data["transition_function"].items()}
        output_function = {key: value for key, value in automaton_data["output_function"].items()}
        return cls(states, input_alphabet, output_alphabet, transition_function, output_function)
