import os

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__ (self):
        self.root = None

  # insert data into the tree
    def insert (self, data):
        new_node = Node (data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node
    
    #returns True is tree is empty, False otherwise
    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False
    
    #recursively determines if 2 trees are similar
    def is_similar_helper (self, aNode, bNode):
        current_1 = aNode
        current_2 = bNode

        if current_1 == None and current_2 == None:
            return True
        elif current_1 !=
        elif current_1 != None and current_2 != None:
            return self.is_similar_helper(aNode.lchild, bNode.lchild) and self.is_similar_helper(aNode.rchild, bNode.rchild)
        else:
            return False 

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        if self.root == True and pNode == None:
            return True
        return self.is_similar_helper(self.root, pNode)

     # Prints out all nodes at the given level
    def print_level (self, current_root, level):
        if current_root == None:
            return
        if level == 1:
            print(current_root.data,end=' ')
        else:
            self.print_level(current_root.lchild, level-1)
            self.print_level(current_root.rchild, level-1)
        

    #recursively finds height of tree 
    def get_height_helper(self, aNode):
        if aNode == None:
            return -1
        else:
            left_height = self.get_height_helper(aNode.lchild)
            right_height = self.get_height_helper(aNode.rchild)
            max_height = max(left_height,right_height) + 1
            return max_height

        
    # Returns the height of the tree
    def get_height (self): 
        if self.root == None:
            return 0
        return self.get_height_helper(self.root)
         

    #recursively finds number of nodes
    def num_nodes_helper(self, aNode):
        if  aNode == None:
            return 0
        else:
            left_nodes = self.num_nodes_helper(aNode.lchild)
            right_nodes = self.num_nodes_helper(aNode.rchild)
            return left_nodes + right_nodes + 1


    # Returns the number of nodes in tree which is 
    # equivalent to 1 + number of nodes in the left 
    # subtree + number of nodes in the right subtree
    def num_nodes (self):
        return self.num_nodes_helper(self.root)
    

def main():
    # write code here
    tree1 = input().strip().split()
    tree2 = input().strip().split()

    #convert str numbers into int
    for i in range(len(tree1)):
        tree1[i] = int(tree1[i])

    for i in range(len(tree2)):
        tree2[i] = int(tree2[i])

    #create Trees
    Tree1 = Tree()
    Tree2 = Tree() 
    for i in tree1:
        Tree1.insert(i)
    for i in tree2:
        Tree2.insert(i)

    #states whether trees are similar
    print('The Trees are similar:',Tree1.is_similar(Tree2.root))
    print()

    #prints tree 1
    print('Levels of Tree 1:')
    for i in range (1,Tree1.get_height()+2):
        Tree1.print_level(Tree1.root,i)
        print()
    print()

    #prints tree 2
    print('Levels of Tree 2:')
    for i in range (1,Tree2.get_height()+2):
        Tree2.print_level(Tree2.root,i)
        print()
    print()

    #height and num nodes for Tree 1
    print('Height of Tree 1:',Tree1.get_height())
    print('Nodes in Tree 1:',Tree1.num_nodes())

    #height and num nodes for Tree 2
    print('Height of Tree 2:',Tree2.get_height())
    print('Nodes in Tree 2:', Tree2.num_nodes())


main()
