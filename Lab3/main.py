import buchi_automaton as ba
import intersection_na as algo
import os

INPUT_DIR = "automatons"
OUTPUT_DIR = "results"


def main():
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    paths = os.listdir(INPUT_DIR)
    for path in paths:
        if "pair" in path:
            continue

        with open(f"{INPUT_DIR}/{path}") as file:
            automaton1 = ba.BuchiAutomaton.from_json(file.read())
        with open(f"{INPUT_DIR}/pair_{path}") as file:
            automaton2 = ba.BuchiAutomaton.from_json(file.read())

        print("First:", automaton1, sep="\n")
        print("Second:", automaton2, sep="\n")

        result = algo.inter_nba(automaton1, automaton2)
        print("InterNBA:", result, sep="\n")

        with open(f"{OUTPUT_DIR}/{'result_' + path}", "w") as file:
            file.write(result.to_json())


if __name__ == "__main__":
    main()
