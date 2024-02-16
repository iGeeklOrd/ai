class Node:
    def __init__(self, x ,y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def bsf(self, rule, w):
        x = self.x
        y = self.y

        if rule == 1:
            if(x<w.maxJug1):
                x = w.maxJug1

class waterJug:
    def __init__(self, maxjug1, maxJug2, goalState):
        self.maxJug1 = maxJug1
        self.maxJug2 = maxJug2
        self.goalState = goalState

    def test(self):
        if self.maxjug1 <= 0 or self.maxjug2 <= 0:
            return None
        if self.g_state > self.maxjug1:
            return None
    
        
maxJug1 = input("Enter the maximum capacity of Jug 1: ")
maxJug2 = input("Enter the maximum capacity of Jug 2: ")
goalState = input("Enter the goal state: ")
        
Node(maxJug1, maxJug2, goalState)
