import os
from moore_mealy_automaton import MooreMealyAutomaton
from moore_to_mealy import moore_to_mealy, rename_states

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

        renamed, names = rename_states(result)
        print(names)
        print("FA after renaming:", renamed, sep="\n")

        with open(f"{OUTPUT_DIR}/{'result_' + path}", "w") as file:
            file.write(renamed.to_json())


if __name__ == "__main__":
    main()
