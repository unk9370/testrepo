from typing import Dict, List, Tuple, Optional

Assignment = Dict[str, str]  # Node → Color mapping


class GraphColoring:
    def __init__(
        self, variables: List[str], edges: List[Tuple[str, str]], colors: List[str]
    ):
        self.variables = variables
        self.colors = colors

        # Build adjacency list
        self.neighbors = {v: [] for v in variables}
        for u, v in edges:
            self.neighbors[u].append(v)
            self.neighbors[v].append(u)

        self.nodes_explored = 0

    def is_consistent(self, var: str, value: str, assignment: Assignment) -> bool:
        for neighbor in self.neighbors[var]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack(self, assignment: Assignment) -> Optional[Assignment]:
        if len(assignment) == len(self.variables):
            return assignment

        for var in self.variables:
            if var not in assignment:
                break

        for color in self.colors:
            if self.is_consistent(var, color, assignment):
                assignment[var] = color
                self.nodes_explored += 1

                result = self.backtrack(assignment)
                if result is not None:
                    return result

                assignment.pop(var)

        return None

    def solve(self) -> Optional[Assignment]:
        self.nodes_explored = 0
        return self.backtrack({})


def example_graph():
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    edges = [
        ("WA", "NT"),
        ("WA", "SA"),
        ("NT", "SA"),
        ("NT", "Q"),
        ("SA", "Q"),
        ("SA", "NSW"),
        ("SA", "V"),
        ("Q", "NSW"),
        ("NSW", "V"),
    ]
    return variables, edges


def run_demo():
    variables, edges = example_graph()
    colors = ["Red", "Green", "Blue"]
    csp = GraphColoring(variables, edges, colors)
    solution = csp.solve()
    print("Solution:", solution)
    print("Nodes explored:", csp.nodes_explored)


if __name__ == "__main__":
    run_demo()
