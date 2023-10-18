## Implementration of converting e-NFA to DFA algorithm

Finite automata are presented in the form of a json file.

<img src="https://github.com/Megarekrut65/AASDM-2023/blob/main/Lab1/images/input1.png?raw=true" alt="automaton" width="500"/>
Here is an example for this automaton:

````json
{
    "states": [1, 2, 3],
    "alphabet": ["a", "b", "c"],
    "transitions": {
        "(1, 'b')": [2],
        "(1, 'c')": [3],
        "(1, 'e')": [2, 3],
        "(2, 'a')": [1, 2],
        "(2, 'b')": [3],
        "(2, 'c')": [1, 2]
    },
    "begin": 1,
    "finals": [3]
}
````

Program converts all automatons from folder 'automatons' to DFA and saves its to folder 'results'