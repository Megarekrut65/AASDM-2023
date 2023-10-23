## Implementration of converting e-NFA to DFA algorithm

Moore and Mealy automatons are presented in the form of a json file.

<img src="https://github.com/Megarekrut65/AASDM-2023/blob/main/Lab2/images/input1.png?raw=true" alt="automaton" width="500"/>
Here is an example for this Moore automaton:

````json
{
    "states": ["q0", "q1", "q2", "q3", "q4"],
    "input_alphabet": ["0", "1"],
    "output_alphabet": ["0", "1"],
    "transition_function": {
        "('q0', '0')": "q1",
        "('q0', '1')": "q2",
        "('q1', '0')": "q1",
        "('q1', '1')": "q3",
        "('q3', '0')": "q4",
        "('q3', '1')": "q2",
        "('q2', '0')": "q4",
        "('q2', '1')": "q2",
        "('q4', '0')": "q1",
        "('q4', '1')": "q3"
    },
    "output_function": {
        "q0": "0",
        "q1": "0",
        "q2": "0",
        "q3": "1",
        "q4": "1"
    }
}

````

Program converts all Moore automatons from folder 'automatons' to Mealy automatons and saves its to folder 'results'