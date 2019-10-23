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


def informedSearch(problem, tree: bool, f):
    stats = Stats()
    node = Node(problem.initState, None, None, 0)
    frontier = PriorityQueue()
    frontier.add(node, f(node))
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

        if problem.goalTest(node.state):
            return (node.solution(), stats)
        stats.ePlusPlus(node.state)  # **
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if tree or not alreadyExists(child):
                frontier.add(child, f(child))
                stats.fPlusPlus(child.state)  # **


# BFS Tree Search
def bfsTree(problem):
    return uninformedSearch(problem, FifoQueue(), tree=True)


# BFS Graph Search
def bfsGraph(problem):
    return uninformedSearch(problem, FifoQueue(), tree=False)


# DFS Graph Search
def dfsGraph(problem):
    return uninformedSearch(problem, LifoQueue(), tree=False)


# UCS Tree Search
def ucsTree(problem):
    return informedSearch(problem, True, lambda x: x.pathCost)


# UCS Graph Search
def ucsGraph(problem):
    return informedSearch(problem, False, lambda x: x.pathCost)


# GBFS Graph Search
def gbfsGraph(problem):
    def h(x): return problem.heuristic(x.state)
    return informedSearch(problem, False, h)


# A* Graph Search
def aStarGraph(problem):
    def h(x): return problem.heuristic(x.state)
    def g(x): return x.pathCost
    def f(x): return h(x) + g(x)
    return informedSearch(problem, PriorityQueue(), False, f)
