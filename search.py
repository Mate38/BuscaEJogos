# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import copy


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def goalTest(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """
        util.raiseNotDefined()

    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """
        util.raiseNotDefined()

    def getCost(self, state, action):
        """
        Given a state and an action, returns step cost, which is the incremental cost 
        of moving to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()
        
    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    You are not required to implement this, but you may find it useful for Q5.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth.

    Begin with a depth of 1 and increment depth by 1 at every step.
    """
    "*** YOUR CODE HERE ***"

    max_depth = 0

    actualState = problem.getStartState()

    while True:
        path = util.Queue()
        visitedStates = util.Queue()
        close_nodes = util.Stack()

        found = iterative_recursive_deepening(actualState, max_depth, problem, path, visitedStates, close_nodes)

        if found:
            return path.list

        max_depth += 1


def iterative_recursive_deepening(actual_state, max_depth, problem, path, visitedStates, close_nodes):

    visitedStates.push(actual_state)

    if problem.goalTest(actual_state):
        return True
    elif max_depth > 0:
        actions = util.Queue()

        for action in problem.getActions(actual_state):
            child = problem.getResult(actual_state, action)
            actions.push(action)
            close_nodes.push(child)

        for action in actions.list:
            child = close_nodes.pop()
            if child not in visitedStates.list and child not in close_nodes.list:
                found = iterative_recursive_deepening(child, max_depth - 1, problem, path, visitedStates, close_nodes)
                if found:
                    path.push(action)
                    return True
    return False


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()

    moves = util.Stack()

    visited = util.Stack()

    nodes = util.PriorityQueue()

    start_cost = heuristic(state, problem)

    while True:

        visited.push(state)

        if problem.goalTest(state) == True:
            break

        actions = problem.getActions(state)

        for i in range(0, len(actions)):
            
            aux = list(moves.list)

            aux.append(actions[i])

            result = problem.getResult(state, actions[i])

            cost = (heuristic(result, problem) + problem.getCost(state, actions[i])) + (start_cost - heuristic(state, problem))
            
            nodes.push((result, cost, aux), cost)

        while nodes.isEmpty() != True:

            (state, start_cost, moves.list) = nodes.pop()

            if state not in visited.list:
                break

    return moves.list

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
