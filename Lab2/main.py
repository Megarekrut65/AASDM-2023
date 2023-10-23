import os
from Lab2.moore_mealy_automaton import MooreMealyAutomaton
from Lab2.moore_to_mealy import moore_to_mealy

INPUT_DIR = "automatons"
OUTPUT_DIR = "results"


def main():
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    paths = os.listdir(INPUT_DIR)
    for path in paths:
        with open(f"{INPUT_DIR}/{path}") as file:
            automaton = MooreMealyAutomaton.from_json(file.read())

        print("Moore:", automaton, sep="\n")

        result = moore_to_mealy(automaton)
        print("Mealy:", result, sep="\n")

        # renamed, names = algo.rename_states(result)
        # print(names)
        # print("DFA after renaming:", renamed, sep="\n")

        with open(f"{OUTPUT_DIR}/{'result_' + path}", "w") as file:
            file.write(automaton.to_json())

    # moore = MooreMealyAutomaton(
    #     states={'a', 'b', 'c', 'd'},
    #     input_alphabet={'x', 'y'},
    #     output_alphabet={'0', '1'},
    #     transition_function={
    #         ('a', 'y'): 'a',
    #         ('a', 'x'): 'c',
    #         ('b', 'y'): 'a',
    #         ('b', 'x'): 'c',
    #         ('c', 'y'): 'd',
    #         ('c', 'x'): 'b',
    #         ('d', 'y'): 'd',
    #         ('d', 'x'): 'c',
    #     },
    #     output_function={
    #         'a': '1',
    #         'b': '0',
    #         'c': '0',
    #         'd': '1',
    #     }
    # )

    # mealy = moore_to_mealy(moore)
    # print(mealy)


if __name__ == "__main__":
    main()
