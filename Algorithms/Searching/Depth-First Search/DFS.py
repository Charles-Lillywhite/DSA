graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}

# recursive implementation

def DFS(G, n):
    visited = set()
    
    def _DFS(G, n): # graph G, Node n
        newNode = n
        print(newNode, end = " ")
        visited.add(newNode)
        for node in G[newNode]:
            if node not in visited:
                _DFS(G, node)
    _DFS(G, n)
    
# iterative implementation, using stack

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = " ")

        # reverse iterate through edge list so results match recursive version
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)
