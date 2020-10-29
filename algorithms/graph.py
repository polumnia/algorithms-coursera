from abc import ABC, abstractmethod
from collections import defaultdict

class Graph:
    """Representation of a simple graph using an adjacency map."""

    def __init__(self, directed=False):
        """Create an empty graph (undirected, by default)
        
        Graph is directed if optional parameter is set to True."""
        self._outgoing = dict()
        # only create second map for directed graph; use alias for undirected
        self._incoming = dict() if directed else self._outgoing
    
    def is_directed(self):
        """Return True if this is a directed graph; False if undirected.
        
        Property is based on the original declaration of the graph, not its contents."""
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """Return the number of vertices of the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all the vertices of the graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges of the graph."""
        total_edge_count = sum(self.degree(v) for v in self._outgoing)
        return total_edge_count if self.is_directed() else total_edge_count // 2

    def edges(self):
        """Return an iteration of all the edges of the graph."""
        set_of_edges = set()
        for secondary_map in self._outgoing.values():
            set_of_edges.update(secondary_map.values())
        return set_of_edges

    def get_edge(self, u, v):
        """Return the edge from vertex u to vertex v, if one exists; otherwise return None."""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """Return the number of (outgoing) edges incident to vertex v in the graph. 
        
        If graph is directed, optional paramter is used to count incoming edges."""
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, out=True):
        """Return an iteration of all (outgoing) edges incident to vertex v. 
        
        If graph is directed, optional paramter is used to request incoming edges."""
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex storing element x."""
        new_vertex = Vertex(x)
        self._outgoing[new_vertex] = dict()
        if self.is_directed():
            self._incoming[new_vertex] = dict()
        return new_vertex

    def insert_edge(self, u, v, x=None):
        """Create and return a new Edge from vertex u to vertex v, storing element x (None by default)."""
        new_edge = Edge(u, v, x)
        self._outgoing[u][v] = new_edge
        self._incoming[v][u] = new_edge
        return new_edge

    def remove_vertex(v):
        """Remove vertex v and all its incident edges from the graph."""
        for opposite in self._outgoing[v]:
            del self._incoming[opposite][v]
        del self._outgoing[v]

    def remove_edge(e):
        """Remove edge e from the graph."""
        u, v = e.endpoints
        del self._outgoing[u][v]
        del self._incoming[v][u]


class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_element'
    
    def __init__(self, element):
        """Do not call constructor directy. Use Graph's insert_vertex(element)"""
        self._element = element
    
    @property
    def element(self):
        """Return element associated with vertex."""
        return self._element

    def __hash__(self):
        return hash(id(self))


class Edge:
    """Lightweight edge structure for a graph."""
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, origin: Vertex, destination: Vertex, element):
        """Do not call constructor directy. Use Graph's insert_edge(u, v, x)"""
        self._origin = origin
        self._destination = destination
        self._element = element
    
    @property
    def endpoints(self):
        """Return tuple of origin and destination vertices"""
        return (self._origin, self._destination)
    
    def opposite(self, v: Vertex):
        """Return vertex that is opposite v on this edge"""
        return self._destination if v is self._origin else self._origin
    
    @property
    def element(self):
        return self._element
    
    def __hash__(self)
    return hash((self._origin, self._destination))


# def depth_first_search(graph: Graph, source: Vertex, marked_vertices: set = set()):
#     marked_vertices.add(source)
#     for e in graph.incident_edges(source):
#         v = e.opposite(source)
#         if v not in marked_vertices:
#             depth_first_search(graph, v, marked_vertices)

def depth_first_search(graph: Graph, source: Vertex, discovered: dict):
    for e in graph.incident_edges(source):
        v = e.opposite(source)
        if v not in discovered:
            discovered[v] = e
            depth_first_search(graph, v, discovered)
    

# class Graph:
#     def __init__(self):
#         self.adj_dict = defaultdict(set)

#     def add_edge(self, left_vertex, right_vertex):
#         self.adj_dict[left_vertex].add(right_vertex)
#         self.adj_dict[right_vertex].add(left_vertex)
    
#     def adj_to(self, vertex):
#         return self.adj_dict[vertex]

#     @property
#     def vertices_count(self):
#         return len(self.adj_dict)

#     @property
#     def edges_count(self):
#         pass

#     def __str__(self):
#         pass


# class DFS_Paths:
#     def __init__(self, graph: Graph, source):
#         self.marked = set()
#         self.path_to = dict()
#         self.source = source
#         self.depth_first_search(graph, source)

#     def has_path_to(vertex) -> bool:
#         return vertex in self.marked

#     def path_to(self, vertex):
#         if not self.has_path_to(vertex):
#             return None
#         current_vertex = vertex
#         path = []
#         while True:
#             path.append(current_vertex)
#             if current_vertex == self.source:
#                 break
#             current_vertex = self.path_to[current_vertex]
#         return list(reversed(path))

#     def depth_first_search(self, graph, source):
#         self.marked.add(source)
#         for v in graph.adj_to(source):
#             if v not in self.marked:
#                 self.path_to[v] = source
#                 self.depth_first_search(graph, v)


# if __name__ == '__main__':
#     edges = [
#         (0, 5),
#         (4, 3),
#         (0, 1),
#         (9, 12),
#         (6, 4),
#         (5, 4),
#         (0, 2),
#         (11, 12),
#         (9, 10),
#         (0, 6),
#         (7, 8),
#         (9, 11),
#         (5, 3)
#     ]
#     my_graph = Graph()
#     for v, w in edges:
#         my_graph.add_edge(v, w)
    
#     paths = DFS_Paths(my_graph, 0)
#     print(paths.marked)
#     print(paths.path_to)