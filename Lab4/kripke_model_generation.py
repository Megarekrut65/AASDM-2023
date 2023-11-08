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
