import os
class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))


class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len (self.queue))

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

  # determine if a vertex was visited
    def was_visited (self):
        return self.visited

  # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)

class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # get the index from the vertex label
    # returns -1 if label does not exist
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex object with a given label to the graph
    def add_vertex (self, label):
        if (not self.has_vertex (label)):
            self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        #check if vertices exists
        if self.has_vertex(fromVertexLabel) == True and self.has_vertex(toVertexLabel) == True:
            from_index = self.get_index(fromVertexLabel)
            to_index = self.get_index(toVertexLabel)

            #check if edge exist. Return weight if exist
            if self.adjMat[from_index][to_index] > 0:
                return self.adjMat[from_index][to_index]
            #return -1 if edge not exist
            else:
                return -1 

        #if vertices don't exist
        return -1 

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        neighbors_list = []
        v = self.get_index(vertexLabel)
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0:
                neighbors_list.append(i)
        return neighbors_list

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        vertices_copy = self.Vertices[:]
        return vertices_copy 
    
    # do a depth first search in a graph starting at vertex v (index)
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs (self, v):
         #create queue
        theQueue = Queue()
        current_node = v
        
        #the vertex x is visited and enqueue it
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)
            
        while not theQueue.is_empty():
          
            while self.get_adj_unvisited_vertex(current_node) != -1:
                u = self.get_adj_unvisited_vertex(current_node)
                self.Vertices[u].visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)
            
            current_node = theQueue.dequeue()
          
        # the queue is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete the edge if the graph is going from start to finish
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        from_index = self.get_index(fromVertexLabel)
        to_index = self.get_index(toVertexLabel)
        self.adjMat[from_index][to_index] = 0
        self.adjMat[to_index][from_index] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        vertex_index = self.get_index(vertexLabel)

        #remove vertex from adjacency matrix 
        #remove column
        for i in range(len(self.adjMat)):
          self.adjMat[i].pop(vertex_index)
          
        #remove row
        self.adjMat.pop(vertex_index)
        
        #removes vertex from Vertices list
        self.Vertices.pop(vertex_index)


def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    num_vertices = int (input().strip())
    #print (num_vertices)

    # read all the Vertices and add them the Graph
    for i in range (num_vertices):
        city = input().strip()
        #print (city)
        cities.add_vertex (city)
    
    # read the number of edges
    num_edges = int (input().strip())
    #print (num_edges)

    # read the edges and add them to the adjacency matrix
    for i in range (num_edges):
        edge = input().strip()
        #print (edge)
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    #print the adjacency matrix
    # print ("\nAdjacency Matrix")
    # for i in range (num_vertices):
    #     for j in range (num_vertices):
    #         print (cities.adjMat[i][j], end = " ")
    #     print ()
    # print ()

    # read the starting vertex for dfs and bfs
    start_vertex = input().strip()
    #print (start_vertex)

    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)
    #print (start_index)

    # test depth first search
    print ("Depth First Search") 
    cities.dfs (start_index)

    # test breadth first search
    print("\nBreadth First Search")
    cities.bfs(start_index)
    print()

    # test deletion of an edge
    print('Deletion of an edge')
    delete_edge_from = input().strip().split()
    from_city = delete_edge_from[0]
    to_city = delete_edge_from[1]
    cities.delete_edge(from_city,to_city)

    print ("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range (num_vertices):
            print (cities.adjMat[i][j], end = " ")
        print ()
    print ()

    # # test deletion of a vertex
    delete_city = input().strip()
    cities.delete_vertex(delete_city)
    print('Deletion of a vertex')
    print()
    print('List of Vertices')
    for i in cities.Vertices:
        print(i.label)

    
    print ("\nAdjacency Matrix")
    for i in range (num_vertices - 1):
        for j in range (num_vertices - 1):
            print (cities.adjMat[i][j], end = " ")
        print ()
    print ()


    #### additional tests: get_edge_weight, get_neighbors, get_vertices ######
    #print('Edge weight from San Francisco to Los Angeles:')
    #print(cities.get_edge_weight('San Francisco','Los Angeles'))

    #print('Edge weight from Kansas City and San Francisco:')
    #print(cities.get_edge_weight('Kansas City','San Francisco'))

main()
