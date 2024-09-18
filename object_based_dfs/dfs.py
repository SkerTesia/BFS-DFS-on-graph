class Vertex:
    def __init__(self, v_id):
        self.id = v_id
        self.neighbors = []

    def add_neighbor(self, end, cap):
        edge = {"end":end,"cap":cap}
        if end not in self.neighbors:
            self.neighbors.append(edge)

class Graph:
    def __init__(self):  # graph na začetku vsebuje prazen dict
        self.vertices = {}

    def __str__(self):
        niz = "graf: \n"
        for id, vertex in self.vertices.items():
            niz += str(id) + ":"
            for nei in vertex.neighbors:
                niz += str(nei) + " "
            niz += "\n"
        return niz

    def add_vertex(self, v):  # v dict dodam na mesto v.id objekt v
        if isinstance(v, Vertex) and v.id not in self.vertices:
            self.vertices[v.id] = v
            return True
        return False

    def add_vertices(self, v_list):  # vertices iz seznama se dodajajo prek zgornje funkcije
        for v in v_list:
            self.add_vertex(v)

    def add_edge(self, start, end, cap):  # dodaj id-je v sosede vozlišč
        if start in self.vertices.keys() and end in self.vertices.keys():
            self.vertices[start].add_neighbor(end,cap)
            return True
        return False

    def clone(self):
        resGraph = Graph()
        for v_id in self.vertices.keys():
            resGraph.add_vertex(Vertex(v_id))
        for v_id, vertex in self.vertices.items(): # grem čez vertexe
            for e in vertex.neighbors: # grem čez povezave na vertexu
                resGraph.add_edge(v_id,e["end"],e["cap"]) # kopiram povezave
        return resGraph


# Initialize the graph
graph = Graph()
graph.add_vertices([Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4), Vertex(5)])
# Add edges with capacities
graph.add_edge(0, 1, 11)
graph.add_edge(0, 2, 12)
graph.add_edge(1, 3, 12)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 4, 11)
graph.add_edge(3, 5, 19)
graph.add_edge(4, 3, 7)
graph.add_edge(4, 5, 4)
# Print the graph to verify
print(graph)

def DFS(graph, source_id):
    print("source id", source_id)
    path_num = 0
    source_node = graph.vertices[source_id]
    if len(source_node.neighbors) == 0:
        return 1
    else: 
        for i in source_node.neighbors:
            print("edge", i)
            poti = DFS(graph, i['end'])
            path_num += poti
        print(path_num)
        return path_num



DFS(graph, 0)