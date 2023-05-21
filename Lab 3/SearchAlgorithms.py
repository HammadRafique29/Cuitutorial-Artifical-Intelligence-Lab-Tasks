class Algos:
    def __init__(self, gr):
        self.graph = gr
        self.GoalNode = ""
        self.visited = []
        self.queue = []
        self.stack = []

    def BFS(self, sourceNode):
        self.visited.append(sourceNode)
        print(sourceNode)
        for childNodes in self.graph[sourceNode]:
            if childNodes not in self.visited:
                self.queue.append(childNodes)
        if self.queue:
            self.BFS(self.queue.pop(0))
        else:
            return 0

    def DFS(self, sourceNode):
        self.visited.append(sourceNode)
        print(sourceNode)
        for childNodes in self.graph[sourceNode]:
            if childNodes not in self.visited:
                self.queue.append(childNodes)
                if self.queue:
                    self.DFS(self.queue.pop(0))
                else:
                    return 0


graph = {
    '5': ['3', '7'],
    '3': ['5', '2', '4'],
    '7': ['5', '8'],
    '2': ['3'],
    '4': ['3'],
    '8': ['7']
}
obj = Algos(graph)
# obj.BFS('5')
# obj.visited = []
obj.DFS('5')
