import time


class BuchiTimeAutomaton:
    def __init__(self):
        self.current_state = "State1"
        self.acceptance_states = {"State3"}
        self.transitions = {
            "State1": {"NextState": "State2", "Time": 3},
            "State2": {"NextState": "State3", "Time": 5},
            "State3": {"NextState": "State1", "Time": 7}
        }

    def run(self, max_iterations=10):
        iterations = 0
        while iterations < max_iterations:
            self.print_current_state()
            time.sleep(self.transitions[self.current_state]["Time"])
            self.transition()
            iterations += 1

    def transition(self):
        next_state = self.transitions[self.current_state]["NextState"]
        print(f"Transitioning from {self.current_state} to {next_state}")
        self.current_state = next_state

    def print_current_state(self):
        print(f"Current state: {self.current_state}")