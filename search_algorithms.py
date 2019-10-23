# Utilities: enum datatype & many classes: Window, FifoQueue,
#            LifoQueue, PriorityQueue, Set
from utilities import *

# Search Utilities: Stats class and Node class
from search_utilities import *


def uninformedSearch(problem, frontier, tree: bool):
    stats = Stats()
    node = Node(problem.initState, None, None, 0)
    if problem.goalTest(node.state):
        return (node.solution(), stats)
    frontier.add(node)
    stats.fPlusPlus(node.state)  # **
    explored = Set()

    def alreadyExists(child): return explored.contains(
        child.state) or frontier.find(lambda e: e.state == child.state)

    while True:
        if frontier.isEmpty():
            return (None, stats)
        node = frontier.pop()
        stats.fMinusMinus(node.state)  # **
        if(not tree):
            explored.add(node.state)

        stats.ePlusPlus(node.state)  # **
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if problem.goalTest(child.state):
                return (child.solution(), stats)
            if tree or not alreadyExists(child):
                frontier.add(child)
                stats.fPlusPlus(child.state)  # **

######################################################################
# UCS Tree Search
######################################################################
def ucsTree(problem):
    stats = Stats()
    def f (x): return x.pathCost
    node = Node(problem.initState,None,None,0)
    frontier = PriorityQueue()
    frontier.add(node,f(node))
    stats.fPlusPlus(node.state) #**
    while True:
        if frontier.isEmpty(): return (None,stats) 
        node = frontier.pop()
        stats.fMinusMinus(node.state) #**
        if problem.goalTest(node.state): return (node.solution(),stats) 
        stats.ePlusPlus(node.state) #**
        for action in problem.actions(node.state):
            child = node.child(problem,action) 
            frontier.add(child,f(child)) 
            stats.fPlusPlus(child.state) #**


# BFS Tree Search
def bfsTree(problem):
    return uninformedSearch(problem, FifoQueue(), tree=True)


# BFS Graph Search
######################################################################
def bfsGraph(problem):
    return uninformedSearch(problem, FifoQueue(), tree=False)

    # ********************************
    # REPLACE THIS LINE WITH YOUR CODE
    return (None,stats)
    # ********************************

######################################################################
# DFS Graph Search
######################################################################
def dfsGraph(problem):
    return uninformedSearch(problem, LifoQueue(), tree=False)


    stats = Stats() #**

    # ********************************
    # REPLACE THIS LINE WITH YOUR CODE
    return (None,stats)
    # ********************************

######################################################################
# DFS Graph Search       
######################################################################
def ucsGraph(problem):
    stats = Stats() #**

    # ********************************
    # REPLACE THIS LINE WITH YOUR CODE
    return (None,stats)
    # ********************************

######################################################################
# GBFS Graph Search
######################################################################
# def gbfsGraph(problem):
#     stats = Stats() #**

#     # ********************************
#     # REPLACE THIS LINE WITH YOUR CODE
#     return (None,stats)
#     # ********************************



######################################################################
# A* Graph Search
######################################################################
# def aStarGraph(problem):
#     stats = Stats() #**

#     # ********************************
#     # REPLACE THIS LINE WITH YOUR CODE
#     return (None,stats)
#     # ********************************
