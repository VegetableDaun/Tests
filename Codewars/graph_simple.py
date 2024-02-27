class IllegalArgumentError(Exception):
    pass


class Graph:
    def __init__(self, v):
        # Initialize an empty graph with v vertices(V) and 0 edges(E).
        # Raise IllegalArgumentError unless 0 <= v
        if v < 0:
            raise IllegalArgumentError

        self.adj = [[] for _ in range(v)]
        self.V = v
        self.E = 0

    def add_edge(self, v, w):
        # Add the undirected edge v-w to this graph.
        # Raise IllegalArgumentError unless both 0 <= v < V and 0 <= w < V
        if (self.V < v or v < 0) or (self.V < w or w < 0):
            raise IllegalArgumentError

        self.adj[v].append(w)
        self.E += 1
        # if v != w:
        #     self.adj[w].append(0)
        # else:
        #     self.adj[v].append(w)
        self.adj[w].append(v)


z = Graph(100)
z.add_edge(2, 54)
# z.add_edge(54, 2)


for i in range(len(z.adj)):
    if (i + 1) % 10 != 0:
        print(z.adj[i], end=' ,')
    else:
        print(z.adj[i], end='\n')
