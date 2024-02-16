class node() :
    
    def __init__(self, nodeName, children, parent) :
        self.nodeName = nodeName
        self.children = children
        self.parent = parent
        self.level = 0
        
        if(self.parent != None):
            self.level = self.parent.level + 1
    
class tree() :
    def __init__(self, root) :
        self.root = root
    
    def insertNode(self, nodeName, parent) :
        childNode = node(nodeName, [], parent)
        parent.children.append(childNode)
        return childNode

def searchNode(elementName, tree):
    solutionNode = None
    processQueue = []
    processQueue.append(tree.root)
    while(processQueue):
        queueElement = processQueue.pop(0)
        if(queueElement.nodeName == elementName):
            solutionNode = queueElement
            break
        processQueue.extend(queueElement.children)
    return solutionNode

def drawPath(solutionNode):
    answer = []
    temp = solutionNode
    
    while(temp != None):
        answer.append(temp.nodeName)
        temp = temp.parent
    
    answer.reverse()
    print(* answer, sep = "->")
    print("Path Cost: ", len(answer) - 1)

Amit = node("Amit", [], None)
tree = tree(Amit)

Rahul = tree.insertNode("Rahul", Amit)
Priya = tree.insertNode("Priya", Amit)
Sanjay = tree.insertNode("Sanjay", Rahul)
Ravi = tree.insertNode("Ravi", Rahul)
Nisha = tree.insertNode("Nisha", Priya)
Claire = tree.insertNode("Claire", Priya)
Deepak = tree.insertNode("Deepak", Sanjay)
Raj = tree.insertNode("Raj", Sanjay)
Suresh = tree.insertNode("Suresh", Sanjay)
Lisa = tree.insertNode("Lisa", Nisha)
Eric = tree.insertNode("Eric", Claire)
Vinay = tree.insertNode("Vinay", Deepak)
Akash = tree.insertNode("Akash", Deepak)
Gaurav = tree.insertNode("Gaurav", Raj)
Meena = tree.insertNode("Meena", Suresh)
Sam = tree.insertNode("Sam", Lisa)
John = tree.insertNode("John", Lisa)
Ankit = tree.insertNode("Ankit", Vinay)
Harsh = tree.insertNode("harsh", Vinay)
Aditya = tree.insertNode("Aditya", Gaurav)
Sneha = tree.insertNode("Sneha", Gaurav)
Alice = tree.insertNode("Alice", Gaurav)
Reena = tree.insertNode("Reena", Meena)
Abhishek = tree.insertNode("Abhishek", Ankit)
Puneet = tree.insertNode("Puneet", Harsh)
Vikas = tree.insertNode("Vikas", Harsh)
Varun = tree.insertNode("Varun", Harsh)
Anjali = tree.insertNode("Anjali", Sneha)
Arjun = tree.insertNode("Arjun", Sneha)
Carol = tree.insertNode("Carol", Alice)
Dave = tree.insertNode("Dave", Alice)
Rohan = tree.insertNode("Rohan", Abhishek)
Ajay = tree.insertNode("Ajay", Abhishek)
Nidhi = tree.insertNode("Nidhi", Anjali)
Sachin = tree.insertNode("Sachin", Arjun)
Sumit = tree.insertNode("Samit", Arjun)
Aruna = tree.insertNode("Aruna", Rohan)
Ramji = tree.insertNode("Ramji", Rohan)
Virat = tree.insertNode("Virat", Ajay)
Isha = tree.insertNode("Isha", Ajay)
Prem = tree.insertNode("Prem", Nidhi)
Lina = tree.insertNode("Lina", Nidhi)

print("21012011163")
search_key = input("Enter the name to search: ")
result = searchNode(search_key, tree)

if(result == None):
    print("Solution not found")
else:
    drawPath(result)