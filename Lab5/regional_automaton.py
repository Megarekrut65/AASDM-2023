class RegionalAutomaton:
    def __init__(self):
        self.current_state = "a"
        self.transitions = {
            "d": {"NextState": "a"},
            "a": {"NextState": "b"},
            "b": {"NextState": "c"},
            "c": {"NextState": "d"}
        }

    def run(self, total_iterations=4):
        iterations = 0
        while iterations < total_iterations:
            self.print_current_state()
            self.transition()
            iterations += 1

    def transition(self):
        next_state = self.transitions[self.current_state]["NextState"]
        print(f"Transitioning from {self.current_state} to {next_state}")
        self.current_state = next_state

    def print_current_state(self):
        print(f"Current state: {self.current_state}")


