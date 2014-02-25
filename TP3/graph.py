from pygraph.classes.graph import graph
from pygraph.algorithms.minmax import shortest_path

class Graph:
    def __init__(self,nodes,edges,specialNodes):
        self.edges = edges
        self.nodes = nodes
        self.graph = graph()
        self.graph.add_nodes(nodes)
        for (v1,v2,c) in edges:
            self.graph.add_edge((v1,v2), c)

        self.paths = {}
        self.pathsLength = {}
        for v in self.graph.nodes():
            self.paths[v] = {}
            self.pathsLength[v] = {}
            for w in self.graph.nodes():
                self.paths[v][w] = []
                self.pathsLength[v][w] = 0 if v == w else float('inf')

        for v in self.graph.nodes():
            (tree,lengths) = shortest_path(self.graph,v)
            for w in self.graph.nodes():
                self.pathsLength[v][w] = lengths[w]
                self._extractPath(v,w,tree)

        self.specialNodes = specialNodes

    def _extractPath(self,v,w,tree):
        """ Return the list of positions in the shortest path between two vertices 
            (these two vertices are not cotained in the list)"""    
        node = tree[w]
        if node != None:
            while node != v:
                self.paths[v][w].append(node)
                node = tree[node]
        self.paths[v][w].reverse()
         
    def shortestPath(self,v1,v2):
        return self.paths[v1][v2]

    def shortestPathLength(self,v1,v2):
        return self.pathsLength[v1][v2]

    def connected(self,node1,node2):
        return (node1,node2) in [(n1,n2) for (n1,n2,d) in self.edges] + [(n2,n1) for (n1,n2,d) in self.edges]

