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
