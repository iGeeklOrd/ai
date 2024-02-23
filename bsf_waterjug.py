class Node:
    def __init__(self, x ,y, parent):
        self.x = x
        self.y = y
        self.parent = parent

    def bfs(self, rule, w):
        x = self.x
        y = self.y

        if rule == 1:
            if x<w.maxJug1:
                x = w.maxJug1
            else:
                return None
            
        elif rule == 2:
            if y<w.maxJug2:
                y = w.maxJug2
            else:
                return None
            
        elif rule == 3:
            if x>0:
                x = 0
            else: 
                return None
        
        elif rule == 4:
            if y>0:
                y= 0
            else:
                return None

        elif rule == 5:
            if 0 < x + y >= w.maxJug1 and y > 0:
                x = w.maxJug1
                y -= (w.maxJug1 - x)
            else:
                return None
        
        elif rule == 6:
            if 0 < x + y >= w.maxJug2 and x > 0:
                y = w.maxJug2
                x = x - (w.maxJug2 - y)
            else:
                return None
            
        elif rule ==7:
            if 0<x+y<=w.maxJug1 and y>=0:
                x=x+y
                y=0
            else:
                return None
        
        elif rule ==8:
            if 0<x+y<=w.maxJug2 and x>=0:
                x=0
                y=x+y
            else:
                return None
       
        else:
            if x==self.x and y==self.y:
                return None
            else:
                return Node(x,y,self)
    
    

class waterJug:
    def __init__(self, maxJug1, maxJug2, goalState):
        self.maxJug1 = maxJug1
        self.maxJug2 = maxJug2
        self.goalState = goalState

    def test(self):
        if self.maxJug1 <= 0 or self.maxJug2 <= 0:
            return False
        if self.goalState > self.maxJug1:
            return False
        return True

    def bfs_search(self):
        visited = set()
        queue = [Node(0, 0, None)]

        while queue:
            current_node = queue.pop(0)
            if (current_node.x, current_node.y) == (self.goalState, 0):
                return self.trace_path(current_node)
            visited.add((current_node.x, current_node.y))

            for rule in range(1, 9):
                next_node = current_node.bfs(rule, self)
                if next_node and (next_node.x, next_node.y) not in visited:
                    queue.append(next_node)
                    visited.add((next_node.x, next_node.y))
        return None
    

def main():
    maxJug1 = int(input("Enter the maximum capacity of Jug 1: "))
    maxJug2 = int(input("Enter the maximum capacity of Jug 2: "))
    goalState = int(input("Enter the goal state: "))
            
    jug = waterJug(maxJug1, maxJug2, goalState)




if __name__ == "__main__":
    main()