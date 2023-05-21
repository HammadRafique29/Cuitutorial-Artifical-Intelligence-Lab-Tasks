#             5
#     3               7
# 2       4               8

# First add current node to visited, then insert current child nodes in queue
# Pop adjacent node from queue, add its child nodes to visited list.

graph = {
    '5': ['3', '7'],
    '3': ['5', '2', '4'],
    '7': ['5', '8'],
    '2': ['3'],
    '4': ['3'],
    '8': ['7']
}
visited = []
queue = []


def BFS(firstNode):
    visited.append(firstNode)
    queue.append(firstNode)
    while queue:
        m = queue.pop(0)
        print(m)
        for child_nodes in graph[m]:
            if child_nodes not in visited:
                visited.append(child_nodes)
                queue.append(child_nodes)



def DFS(firstNode):
    visited.append(firstNode)
    queue.append(firstNode)
    if queue:
        m = queue.pop(0)
        print(m)
        for child_nodes in graph[m]:
            if child_nodes not in visited:
                DFS(child_nodes)


BFS('5')
