from buchi_time_automaton import BuchiTimeAutomaton
from regional_automaton import RegionalAutomaton


def convert_to_regional(buchi_automaton):
    regional_automaton = RegionalAutomaton()

    state_mapping = {
        "State1": "d",
        "State2": "b",
        "State3": "c"
    }

    for buchi_state, regional_state in state_mapping.items():
        regional_automaton.transitions[regional_state]["NextState"] = state_mapping[buchi_automaton.transitions[buchi_state]["NextState"]]

    return regional_automaton


buchi_automaton = BuchiTimeAutomaton()
regional_automaton = convert_to_regional(buchi_automaton)
regional_automaton.run()