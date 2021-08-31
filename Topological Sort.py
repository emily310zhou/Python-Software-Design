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
        return len (self.stack) == 0

    # return the number of elements in the stack
    def size (self):
        return len (self.stack)



class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty (self):
        return len (self.queue) == 0

    # return the size of the queue
    def size (self):
        return len (self.queue)

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

    # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        vertices_copy = self.Vertices[:]
        return vertices_copy 

    # add a Vertex with a given label to the graph
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

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v, thestacklist):
        nVert = len (self.Vertices)
        for i in range (nVert):
            #if edge exists, check whether unvisited or in current stack
            if self.adjMat[v][i] > 0:
                if not (self.Vertices[i]).was_visited():
                    #print('adjacent vertex:',self.Vertices[i].label)
                    return i
                if i in thestacklist:
                    #print('found cycle at:',self.Vertices[i].label)
                    return -2     #True cycle exists

        #no more adjacent neighbors
        #print('no more adjacent neighbors')
        return -1

    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        #print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):

            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek(),theStack.stack)
            if u == -1:
                u = theStack.pop()
            elif u == -2:
                return True     #there is cycle
            else:
                (self.Vertices[u]).visited = True
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False
        
        #there is no cycle
        return False    


    # do the breadth first search in a graph
    def bfs (self, v):
        pass  

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle (self): 
        if self.dfs(0):
            return True
        else:
            return False

    #count incoming edges at a vertex
    def count_in_degree(self, vertex_idx):
        count = 0
        for i in range(len(self.Vertices)):
            if self.adjMat[i][vertex_idx] > 0:
                count += 1
        return count

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

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        topo_sorted = []
        zero_in_degree =[]

        #find initial vertices with no incoming edges
        for i in range(len(self.Vertices)):
            incoming_edges = self.count_in_degree(i)
            if incoming_edges == 0:
                zero_in_degree.append(self.Vertices[i].label)

        # #conduct topo sort
        while len(zero_in_degree) > 0:
            current = zero_in_degree.pop(0)
            topo_sorted.append(current)
            self.delete_vertex(current)
            for i in range(len(self.Vertices)):
                incoming_edges = self.count_in_degree(i)
                if incoming_edges == 0 and self.Vertices[i].label not in zero_in_degree:
                    zero_in_degree.append(self.Vertices[i].label)

        return topo_sorted

def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # create a Graph object (add vertices and edges)
    theGraph = Graph()
    
    # Get num vertices
    num_vertices = int(input().strip())
    for vert in range(num_vertices):
        theGraph.add_vertex(input().strip())
     
    # Get num edges
    num_edges = int(input().strip())
    for edge in range(num_edges):
        edge_to_edge = input().strip()
        start = theGraph.get_index(edge_to_edge[0])
        finish = theGraph.get_index(edge_to_edge[-1])
        theGraph.add_directed_edge(start, finish)

    #test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        fptr.write("The Graph has a cycle.")
    else:
        fptr.write("The Graph does not have a cycle.")
        #topological sort
        vertex_list = theGraph.toposort()
        fptr.write("\nList of vertices after toposort\n")
        for i in range(len(vertex_list)): 
            fptr.write(str(vertex_list[i]))
            if i < len(vertex_list) - 1:
                fptr.write('\n')
    
    fptr.close()
        
if __name__ == '__main__':
    main()
