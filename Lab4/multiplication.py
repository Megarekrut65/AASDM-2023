import itertools
import random

states = ['s0', 's1', 's2', 's3', 's4']
propositions = ['p', 'q', 'r']

transition_relation = {}
labeling_function = {}

for state in states:
    transition_relation[state] = random.sample(states, 2)

for state in states:
    labeling_function[state] = random.sample(propositions, random.randint(1, 3))

print(transition_relation, labeling_function)

buchi_states = ['before_p', 'after_p']
buchi_transition = {
    'before_p': {('before_p', 'p'), ('after_p', 'p'), ('before_p', None)},
    'after_p': {('after_p', None), ('after_p', 'p')}
}
buchi_initial_state = 'before_p'
buchi_accepting_states = {'after_p'}

buchi_automaton = {
    'states': buchi_states,
    'transitions': buchi_transition,
    'initial_state': buchi_initial_state,
    'accepting_states': buchi_accepting_states
}

print(buchi_automaton)


product_states = list(itertools.product(states, buchi_states))
product_transitions = {}
product_initial_state = ('s0', buchi_initial_state)
product_accepting_states = set()


for (k_state, b_state) in product_states:
    product_transitions[(k_state, b_state)] = set()
    for k_successor in transition_relation[k_state]:
        for (b_successor, prop) in buchi_transition[b_state]:
            if prop is None or prop in labeling_function[k_successor]:
                product_transitions[(k_state, b_state)].add((k_successor, b_successor))
                if b_successor in buchi_accepting_states:
                    product_accepting_states.add((k_successor, b_successor))

product_automaton = {
    'states': product_states,
    'transitions': product_transitions,
    'initial_state': product_initial_state,
    'accepting_states': product_accepting_states
}

print(product_automaton)
