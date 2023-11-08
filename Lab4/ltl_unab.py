import itertools

atomic_props = {'p', 'q'}
formula = 'G(p ∧ q)'

closure = {formula, f'!{formula}', 'p', '!p', 'q', '!q', 'true'}

A0 = set()
A = set()
f = set()
F = set()

A0 = {frozenset({'p', 'q', 'G(p ∧ q)'})}

C = set(A0)

while C:
    s = C.pop()
    A.add(s)

    if 'G(p ∧ q)' in s and 'p' in s and 'q' in s:
        F.add(s)

    for truth_assignment in itertools.product([False, True], repeat=len(atomic_props)):
        truth_assignment_dict = dict(zip(atomic_props, truth_assignment))
        if truth_assignment_dict['p'] and truth_assignment_dict['q']:
            s_next = frozenset({prop if truth_assignment_dict[prop] else f'!{prop}' for prop in atomic_props} | {'G(p ∧ q)'})
            f.add((s, s_next))
            if s_next not in A:
                C.add(s_next)

print(A0, A, f, F, closure)
