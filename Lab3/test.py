from collections import deque


def intersect_Buchi_automata(automaton1, automaton2):
    # Початкові стани та алфавіти автоматів
    states1, alphabet1, transitions1, initial_state1, accepting_states1 = automaton1
    states2, alphabet2, transitions2, initial_state2, accepting_states2 = automaton2

    # Початковий стан для нового автомата
    initial_state = (initial_state1, initial_state2)

    # Визначення функції для обчислення переходів в новому автоматі
    def compute_transition(state1, state2, symbol):
        new_state1 = transitions1.get((state1, symbol), set())
        new_state2 = transitions2.get((state2, symbol), set())
        return new_state1, new_state2

    # Ініціалізація черги для обходу
    queue = deque([initial_state])

    # Відвідані стани
    visited = set()

    # Перетин множин приймаючих станів
    accepting_states = accepting_states1.intersection(accepting_states2)

    # Формування нових переходів для перетину
    new_transitions = {}
    while queue:
        current_state = queue.popleft()
        visited.add(current_state)

        for symbol in alphabet1.intersection(alphabet2):
            next_states1, next_states2 = compute_transition(current_state[0], current_state[1], symbol)
            new_state = (frozenset(next_states1), frozenset(next_states2))
            new_transitions[(current_state, symbol)] = new_state

            if new_state not in visited and new_state not in queue:
                queue.append(new_state)

    return states1, alphabet1.intersection(alphabet2), new_transitions, initial_state, accepting_states


# Задані автомати
automaton1 = (
    {0, 1},
    {'x', 'y'},
    {(0, 'x'): {1}, (0, 'y'): {1}, (1, 'y'): {0, 1}},
    0,
    {0}
)

automaton2 = (
    {0, 2},
    {'x', 'y'},
    {(0, 'x'): {2}, (0, 'y'): {2}, (2, 'x'): {2}, (2, 'y'): {2}},
    0,
    {2}
)

# Обчислення перетину автоматів
result_automaton = intersect_Buchi_automata(automaton1, automaton2)

# Виведення результатів
print("Перетин автоматів:")
print("Стани:", result_automaton[0])
print("Алфавіт:", result_automaton[1])
print("Початковий стан:", result_automaton[3])
print("Приймаючі стани:", result_automaton[4])
print("Функції переходу:")
for (state, symbol), next_state in result_automaton[2].items():
    print(f"({state}, '{symbol}') -> {next_state}")
