import buchi_automaton as ba
import intersection_nba as algo
import os

INPUT_DIR = "automatons"
OUTPUT_DIR = "results"


def main():
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    with open(f"{INPUT_DIR}/automaton_0.json") as file:
        automaton1 = ba.BuchiAutomaton.from_json(file.read())
    with open(f"{INPUT_DIR}/automaton_0_pair.json") as file:
        automaton2 = ba.BuchiAutomaton.from_json(file.read())

    inter = algo.inter_nba(automaton1, automaton2)
    with open(f"{OUTPUT_DIR}/res.json", "w") as file:
        file.write(inter.to_json())


if __name__ == "__main__":
    main()
