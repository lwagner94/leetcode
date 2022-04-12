
from collections import defaultdict

EPSILON = "ε"

class Node:
    def __init__(self, nr):
        self.nr = nr
        self.transitions = defaultdict(lambda: set())
        self.terminal = False
    
    def add_transition(self, token, node):
        self.transitions[token].add(node)
        
    def next(self, token):
        return self.transitions.get(token)
    
    def __repr__(self):
        return f"Node(nr={self.nr}, terminal={self.terminal})"

    def dump_transitions(self):
        for token, nodes in self.transitions.items():
            for node in nodes:
                print(f"  {self.nr} -> {node.nr} [label=\"{token}\"]")
    
class Automaton:
    def __init__(self, regex):
        self.regex = regex
        self.root = Node(0)
        self.nodes = [self.root, ]
        self.build_nodes()
        
        
    def build_nodes(self):
        counter = 1
        node = self.root        
        for i,c in enumerate(self.regex):
            # if c == "*":
            #     last_node.add_transition(EPSILON, node)
            #     node.add_transition(EPSILON, last_node)
            if c == "*":
                continue
            if i < len(self.regex) - 1 and self.regex[i+1] == "*":
                node_1 = Node(counter)
                node_2 = Node(counter + 1)
                node_3 = Node(counter + 2)
                counter += 3

                self.nodes.extend([node_1, node_2, node_3])
                node.add_transition(EPSILON, node_1)
                node.add_transition(EPSILON, node_3)
                node_1.add_transition(c, node_2)
                node_2.add_transition(EPSILON, node_1)
                node_2.add_transition(EPSILON, node_3)
                node = node_3

            else:
                next_node = Node(counter)
                self.nodes.append(next_node)
                counter += 1
                node.add_transition(c, next_node)
                node = next_node
            
        node.terminal = True

    @staticmethod
    def get_next_states(current_states):
        while True:
            next_states = set()
            for state in current_states:
                next_states.update(state.next(EPSILON) or set())
                next_states.add(state)

            if current_states == next_states:
                return next_states
            current_states = next_states
    
    def matches(self, s: str) -> bool:
        current_states = set()
        current_states.add(self.root)

        current_states = self.get_next_states(current_states)


        for c in s:
            next_states = set()
            for state in current_states:
                next_states.update(state.next(c) or state.next(".") or set())
            current_states = self.get_next_states(next_states)
            # node = node.next(c) or node.next(".")
            # if node == None:
            #     return False
        
        for state in current_states:
            if state.terminal:
                return True
        return False
        
    
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        automaton = Automaton(p)
        for node in automaton.nodes:
            print(node)
            node.dump_transitions()
        
        return automaton.matches(s)