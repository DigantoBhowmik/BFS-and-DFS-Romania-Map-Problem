graph = {
    "S": {"B": 1, "A": 2,"G": 9},
    "B": {"E": 4, "D": 2},
    "A": {"D": 3, "C": 2},
    "D": {"G": 4},
    "C": {"G": 4},
}



class graphProblem:

    def __init__(self,initial,goal,graph):

        self.initial=initial
        self.goal=goal
        self.graph=graph


    def actions(self,state):
        return list(graph[state].keys())

    def result(self,state,action):
        return action

    def goalTest(self,state):
        return state == self.goal

    def pathCost(self,cost_so_far, fromState,action,toState):
        return cost_so_far + graph[fromState][toState]


class Node:

    def __init__(self,state,parent=None,action=None,path_cost=0):
        
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost


    def childNode(self,gp,action):
        
        childState=gp.result(self.state,action)
        path_cost_to_childNode = gp.pathCost(self.path_cost,self.state,action,childState)
        
        return Node(childState,self,action,path_cost_to_childNode)

    def expand(self,gp):

        return [self.childNode(gp,action) for action in gp.actions(self.state)]
        

def graphSearch(gp,index):

    frontier=[]
    initialNode=Node(gp.initial)
    frontier.append(initialNode)

    explored=set()

    while frontier:

        print('Frontier: ')
        print([node.state for node in frontier])
        if len(frontier) == 0 : return 'Failure'
  
        node= frontier.pop(index)
        print('Pop : ', node.state)
        
        if gp.goalTest(node.state): return node

        explored.add(node.state)
        
        for child in node.expand(gp):
            print('Chld Node: ',child.state)
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                

    return None




def breadthFirstSearch(gp):

    node=Node(gp.initial)
    
    if gp.goalTest(node.state): return node

    frontier=[]

    frontier.append(node)
    
    explored=set()

    while frontier:

        print('Frontier: ')
        print([node.state for node in frontier])
        if len(frontier) == 0 : return 'Failure'
        
        node= frontier.pop(0)
        print('Pop : ', node.state)

        explored.add(node.state)

        for child in node.expand(gp):
            if child.state not in explored or frontier:
                if gp.goalTest(child.state): return child
                frontier.append(child)



                

gp=graphProblem('S','G',graph)

print ( " Result of BFS " )
print('===================================')
node=breadthFirstSearch(gp)
print('Path Cost to the Goal: ', node.path_cost)

print('===================================')
print ( " Result of DFS " )
print('===================================')
node=graphSearch(gp,-1)
print('Path Cost to the Goal: ', node.path_cost)
