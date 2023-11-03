## Implementration of converting e-NFA to DFA algorithm

Buchi automatons are presented in the form of a json file.

<img src="https://github.com/Megarekrut65/AASDM-2023/blob/main/Lab3/images/input1.jpeg?raw=true" alt="automaton" width="500"/>
Here is an example for this Buchi automaton:

````json
{
    "states": [1, 2, 3],
    "alphabet": ["a", "b"],
    "transitions": {
        "(1, 'a')": [2],
        "(2, 'a')": [3],
        "(2, 'b')": [1],
        "(3, 'b')": [3]
    },
    "begins": [1],
    "finals": [3]
}


````

Program intersects automatons with his pair and saves its to folder 'results'