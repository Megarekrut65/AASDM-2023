from timed_automaton import TimedAutomaton
from regional_automaton import RegionalAutomaton

timed_automaton = TimedAutomaton()
regional_automaton = RegionalAutomaton(timed_automaton)
regional_automaton.generate_regional_automaton()

for state, attributes in regional_automaton.states.items():
    print(f"{state} --{regional_automaton.transitions}--> {state}")