import e_nfa_to_dfa_algo as algo
import finite_automaton as fa
import os

INPUT_DIR = "automatons"
OUTPUT_DIR = "results"


def main():
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    paths = os.listdir(INPUT_DIR)
    for path in paths:
        with open(f"{INPUT_DIR}/{path}") as file:
            automaton = fa.FiniteAutomaton.from_json(file.read())

        print("e-NFA:", automaton, sep="\n")

        result = algo.e_nfa_to_dfa(automaton)
        print("DFA:", result, sep="\n")

        renamed, names = algo.rename_states(result)
        print(names)
        print("DFA after renaming:", renamed, sep="\n")

        with open(f"{OUTPUT_DIR}/{path}", "w") as file:
            file.write(renamed.to_json())


if __name__ == "__main__":
    main()
