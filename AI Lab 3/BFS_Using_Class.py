class Node:
    def __init__(self, state, parent, adjacentNodes, cost):
        self.state = state
        self.parent = parent
        self.adjacentNodes = adjacentNodes
        self.totalCost = cost


def actionSequence(graph, initialNode, goalNode):
    solution = [goalNode]
    currentParent = graph[goalNode].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def BFS():
    graph = {
        'A': Node('A', None, ['B', 'C', 'E'], None),
        'B': Node('B', None, ['A', 'D', 'E'], None),
        'C': Node('C', None, ['A', 'F', 'G'], None),
        'D': Node('D', None, ['B', 'E'], None),
        'E': Node('E', None, ['A', 'B', 'D'], None),
        'F': Node('F', None, ['C'], None),
        'G': Node('G', None, ['C'], None)
    }
    initialNode = 'D'
    goalNode = 'F'

    queue = [initialNode]
    visited = []
    while len(queue) != 0:
        currentNode = queue.pop(0)
        visited.append(currentNode)
        for child in graph[currentNode].adjacentNodes:
            if child not in queue and child not in visited:
                graph[child].parent = currentNode
                if graph[child].state == goalNode:
                    return actionSequence(graph, initialNode, goalNode)
                queue.append(child)


print(BFS())