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

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
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


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    stack = util.Stack()
    stack.push((start, 'Root', 1))
    visited = list()
    ptoc = dict()

    while stack.isNotEmpty():
        currnode = stack.pop()
        # print "currnode is",currnode
        if (problem.isGoalState(currnode[0])):
            # print currnode,"isgoalstate"
            break
        else:
            if currnode[0] not in visited:
                visited.append(currnode[0])
            else:
                continue
            nextnodes = problem.getSuccessors(currnode[0])
            # print "nextnodes", nextnodes
            for node in nextnodes:
                if node not in visited:
                    stack.push(node)
                    ptoc[node] = currnode

        # print 'ptoc is'
        # for i in ptoc:
        #     print i, ptoc[i]
        # print "stack is"
        #    stack.printList()

    # print 'ptoc is'
    # for i in ptoc:
    #    print i, ptoc[i]
    # print "stack is"
    # stack.printList()
    temp = currnode
    rvalue = list()
    while (temp[1] != 'Root'):
        rvalue.append(temp[1]);
        #   print temp
        temp = ptoc[temp]
    rvalue.reverse()
    return rvalue


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    print 'starting bfs?'
    start = problem.getStartState()
    queue = util.Queue()
    queue.push([(start, 'Root', 1), ['Root']])
    visited = list()
    ptoc = dict()
    temp1= list()
    print "start:", start
    print "list of visited nodes:", visited
    print "current queue:"
    queue.printList()
    print ptoc
    # raw_input()

    while queue.isNotEmpty():
        currnode = queue.pop()
        print "currnode is", currnode
        if problem.isGoalState(currnode[0][0]):
            print currnode, "is goal state!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            #raw_input()
            break
        else:
            if currnode[0][0] not in visited:
                print "\ncurrnode not in visited"
                visited.append(currnode[0][0])
            else:
                print "currnode in visited, continuing"
                continue

            nextnodes = problem.getSuccessors(currnode[0][0])
            print "nextnodes", nextnodes
            for node in nextnodes:
                if node[0] not in visited:
                    temp1 = list(currnode[1])
                    temp1.append(node[1])
                    queue.push([node, temp1])
                    ptoc[node] = currnode[0]

            print "list of visited nodes:", visited
            print "current queue:"
            queue.printList()
            print"Current dictionary:"

    rvalue = list()
    temp = currnode[0]
    print "final dict"
    for i in ptoc:
        print i, ptoc[i]

    #raw_input()
    while temp[1] != 'Root':
        rvalue.append(temp[1])
        print temp
        #raw_input()
        print rvalue
        temp = ptoc[temp]
    rvalue.reverse()
    print rvalue
    #raw_input()
    return currnode[1][1:]


# node template is ((x,y),'Direction',cost)
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    pq = util.PriorityQueue()
    start = problem.getStartState();
    pq.push(start, 0)
    pq.printList()
    ntpac = dict()
    visited = list()
    ntpac[start] = (['Root'], 0)
    while pq.isNotEmpty():  # node[0] is syntetagmenes, node[1] is direction, node[2] is cost
        node = pq.pop();
        # print node
        tempPathToParent = list(ntpac[node][0])
        cost = ntpac[node][1]
        # print tempPathToParent
        if problem.isGoalState(node):
            print "ISGOALSTATEEEEEE!!!!!!"
            rvalue = ntpac[node][0]
            # print node
            # print rvalue
            # pq.printList()
            # raw_input()
            # dicprint(ntpac)

            print rvalue[1:]

            return rvalue[1:]
        successors = problem.getSuccessors(node)
        for s in successors:
            # print s
            tempPath = list(tempPathToParent)
            tempPath.append(s[1])
            newCost = cost + s[2]

            # print 'newCost', newCost
            if s[0] not in ntpac:
                # print "node not logged"

                # print 'tempPath ', tempPath

                # print 'tempPath1 ', tempPath

                ntpac[s[0]] = (tempPath, newCost)
                pq.push(s[0], newCost)
                pq.printList()
                # dicprint(ntpac)
                # raw_input()
            else:
                # print 'hi'
                if ntpac[s[0]][1] > newCost:
                    ntpac[s[0]] = (tempPath, newCost)

    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # raw_input()
    pq = util.PriorityQueue()
    start = problem.getStartState();
    pq.push(start, 0)
    # pq.printList()
    ntpac = dict()
    visited = list()
    ntpac[start] = (['Root'], 0)
    while pq.isNotEmpty():  # node[0] is syntetagmenes, node[1] is direction, node[2] is cost
        node = pq.pop();
        print 'now examining', node
        tempPathToParent = list(ntpac[node][0])
        cost = ntpac[node][1]
        # print tempPathToParent
        if problem.isGoalState(node):
            print "ISGOALSTATEEEEEE!!!!!!"
            rvalue = ntpac[node][0]
            # print node
            # print rvalue
            # pq.printList()
            # raw_input()
            # dicprint(ntpac)

            print rvalue[1:]

            return rvalue[1:]
        successors = problem.getSuccessors(node)
        for s in successors:
            print "    ", s
            tempPath = list(tempPathToParent)
            tempPath.append(s[1])

            newCost = problem.getCostOfActions(tempPath[1:]) + heuristic(s[0], problem)
            print '        hv', heuristic(s[0], problem)
            print '        newCost!', newCost
            if s[0] not in ntpac:
                print "               node not logged"

                print '               tempPath ', tempPath
                ntpac[s[0]] = (tempPath, newCost)
                pq.push(s[0], newCost)

                # dicprint(ntpac)
                # raw_input()
            else:
                print '                 hi'
                if ntpac[s[0]][1] > newCost:
                    ntpac[s[0]] = (tempPath, newCost)
                    pq.push(s[0], newCost)
                # raw_input()
            pq.printList()

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
