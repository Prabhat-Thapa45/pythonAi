class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)
        
    def contains_state(self, state:array):
        return any(node.state == state for node in self.frontier)
    
    def empyt(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node
    