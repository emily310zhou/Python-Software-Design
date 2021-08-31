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

    # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)

    # return the number of elementsin the stack
    def size (self):
        return (len (self.stack))

class Node (object):
    def __init__ (self, data = None):
        self.data = data
        self.lchild = None
        self.rchild = None
      # self.parent = None
      # self.visited = False

class Tree (object):
    def __init__ (self):
        self.root = None

    def create_tree (self, expr):
        self.root = Node()
        current_node = self.root
        my_stack = Stack()
        operator_list = ['+','-','*','/','//','%','**']
        expr_list = expr.split(' ')

        for current_token in expr_list:

            #token = (
            if current_token == '(':
                current_node.lchild = Node()
                my_stack.push(current_node)
                #print('pushed onto stack:',current_node.data)
                current_node = current_node.lchild
              
            #token is operator
            elif current_token in operator_list:
                current_node.data = current_token
                my_stack.push(current_node)
                #print('pushed onto stack:',current_node.data)
                current_node.rchild = Node()
                current_node = current_node.rchild

            #token is number
            elif current_token != ')':
                current_node.data = current_token
                current_node = my_stack.pop()
                #print('popped from stack:',current_node.data)

            #token is )
            else:
                if not my_stack.is_empty():
                    current_node = my_stack.pop()
                    #print('popped from stack:',current_node.data)
                #else:
                   # break

        #print('Root:',self.root.data)
        #print("Root's left child:",self.root.lchild.data)
        #print("Root's left child's left child:",self.root.lchild.lchild.data)
        #print("Root's left child's right child:",self.root.lchild.rchild.data)

       # print("Root's right child:",self.root.rchild.data)
       # print("Root's right child's left child:",self.root.rchild.lchild.data)
        #print("Root's right child's right child:",self.root.rchild.rchild.data)


    def calculate_rpn (self, op1, op2, token):
        if (token == '+'):
            return op1 + op2
        elif (token == '-'):
            return op1 - op2
        elif (token == '*'):
            return op1 * op2
        elif (token == '/'):
            return op1 / op2
        elif (token == '//'):
            return op1 // op2
        elif (token == '%'):
            return op1 % op2
        elif (token == '**'):
            return op1 ** op2


    def evaluate (self, aNode, po_list):
        eval_stack = Stack()
        operator_list = ['+','-','*','/','//','%','**']
    
        #get postfix expression
        tokens = self.post_order(aNode,po_list).split(' ')

        #convert digits from str into float
        for i in range(len(tokens)):
            if tokens[i] not in operator_list and tokens[i] != '(' and tokens[i] != ')':
                tokens[i] = float(tokens[i])
             
        #go through token list to find operands and operators
        for item in tokens:
            if item in operator_list:
                oper2 = eval_stack.pop()
                oper1 = eval_stack.pop()
                eval_stack.push(self.calculate_rpn(oper1, oper2, item))
            else:
                eval_stack.push (float(item))

        return str(eval_stack.pop())



    # pre order traversal - center, left, right
    def pre_order (self, aNode, pr_list):
        if (aNode != None):
            pr_list.append(aNode.data)
            self.pre_order (aNode.lchild, pr_list)
            self.pre_order (aNode.rchild, pr_list)
        return ' '.join(pr_list)

    # post order traversal - left, right, center
    def post_order (self, aNode, po_list):
        if (aNode != None):
            self.post_order (aNode.lchild, po_list)
            self.post_order (aNode.rchild, po_list)
            po_list.append(aNode.data)
        return ' '.join(po_list)



def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    expr = input().strip(' ')


    #our code
    my_tree = Tree()
    pre_order_list = []
    post_order_list = []
    eval_post_list = []
    my_tree.create_tree(expr)

    #calculate and output expression
    result = my_tree.evaluate(my_tree.root, eval_post_list)
    fptr.write(expr + ' = ' + result + '\n')
    fptr.write('\n')

    #find and output pre-order and post-order expression
    pre_order = my_tree.pre_order(my_tree.root,pre_order_list)
    post_order = my_tree.post_order(my_tree.root, post_order_list)

    fptr.write('Prefix Expression: ' + pre_order + '\n')
    fptr.write('\n')
    fptr.write('Postfix Expression: ' + post_order)
    
    

main()
