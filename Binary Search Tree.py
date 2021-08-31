import os

class Node(object):
    def __init__ (self, data = None):
        self.data = data
        self.rchild = None
        self.lchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
      
        #insert all letters and space
        for ch in encrypt_str:
            #print('this is ch:',ch)
            if ch.isalpha()and ch.islower() or ch == ' ':
                self.insert(ch)

        #print('root:',self.root.data)
        #print("root's left child:",self.root.lchild.data)
        #print("root's left child's left child:",self.root.lchild.lchild.data)
        #print("root's left child's right child:",self.root.lchild.rchild.data)
        #print("root's right child:",self.root.rchild.data)
        #print("root's right child's left child:",self.root.rchild.lchild.data)
        #print("root's right child's right child:",self.root.rchild.rchild.data)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        new_node = Node (ch)
        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while current != None:
                parent = current
    
                #ch is < than current ch 
                if ord(ch) < ord(current.data):
                    current = current.lchild
                    
                #ch is > than current ch
                elif ord(ch) > ord(current.data):
                    current = current.rchild
                    
                #ch = current ch, node already exists
                else:
                    return
        
        #found location now insert node
        if ord(ch) < ord(parent.data):
            parent.lchild = new_node
        else:
            parent.rchild = new_node

        

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        search = '' 
        current = self.root
    
        if current.data == ch:
            search = search + '*'
            return search
    
        while (current != None) and (current.data != ch):
            if ord(ch) < ord(current.data):
                search = search + '<'
                current = current.lchild
            else: #ord(data) > ord(current.data):
                search = search + '>'
                current = current.rchild  
            #else:
                #break
        
        #if ch is not exist in tree, return empty string
        if current == None:
            return ''
        else:
            return search

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        current = self.root
        
        for i in st:
          if i == '*':
            return current.data
          elif i == '<':
            current = current.lchild
          else: # i == '>'
            current = current.rchild
        
        if current == None:
          return ''
        else:
          return current.data
        

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):

        #list to track encrypted ch
        encrypted_list = []
        lower_st = st.lower()

        #print('lowercase:',lower_st)
        #go through lowercase string
        for ch in lower_st:
            #encrypt only letters and space
            if ch.isalpha() or ch == ' ':
                encrypted_ch = self.search(ch)
                encrypted_list.append(encrypted_ch)
        
        #return encrypted ch sepeared by delimiter
        return '!'.join(encrypted_list)

        
    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        split_st = st.split("!")
        decrypted_list = []
        print(split_st)
        for i in split_st:
            decrypted_ch = self.traverse(i)
            decrypted_list.append(decrypted_ch)
        
        return ''.join(decrypted_list)
    
def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    key = input().strip()
    encrypt_string = input().strip()
    decrypt_string = input().strip()
    
    # add your code here
    tree = Tree(key)
    encrypted_line = tree.encrypt(encrypt_string)
    decrypted_line = tree.decrypt(decrypt_string)
    fptr.write(encrypted_line + '\n')
    fptr.write(decrypted_line)
   
    
main()
