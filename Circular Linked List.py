class Link(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    # Constructor
    def __init__ ( self ): 
        self.first = None
        self.last = None
        self.num_links = 0

    def get_num_links (self):
        self.num_links = 0
        current = self.first
        if current == None:
            return self.num_links
        else:
            self.num_links += 1
        
        while current.next != self.first:
            self.num_links += 1
            current = current.next
        return self.num_links

    # Insert an element (value) in the list
    def insert ( self, data):
        new_link = Link(data)
        current = self.first

        #insert when LL is empty
        if self.last == None:
            self.first = new_link
            new_link.next = self.first  #set node's next to first node
            self.last = new_link        #set external pointer at last node
            return

        self.last.next = new_link
        new_link.next = self.first      #set node's next to first node
        self.last = new_link            #set external pointer at new node

    # Find the link with the given data (value)
    def find ( self, data ):
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current == self.last:
                return None
            else:
                current = current.next
        return current

    # Delete a link with a given data (value)
    def delete ( self, data ):
        previous = self.first
        current = self.first
        if current == None:
            return None
        while current.data != data:
            if current == self.last:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:           #delete first node
            self.first = self.first.next
            self.last.next = self.first
        elif current == self.last:          #delete last node 
            previous.next = self.first
            self.last = previous
            self.last.next = self.first     
        else:
          previous.next = current.next      #delete within linked list

        return current

    # Delete the nth link starting from the Link start 
    # Return the next link from the deleted Link
    def delete_after ( self, start, n ):
        nth_link = ''

        #given a link, find the nth link
        start_link = self.find(start)
        for i in range(n-1):
            start_link = start_link.next   

        nth_link = start_link

        #find the next link
        next_link = nth_link.next

        #delete nth link
        killed = self.delete(nth_link.data)

        return killed.data, next_link.data
    
    # Return a string representation of a Circular List
    def __str__ ( self ):
        pass
        
def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    soldiers = int(input().strip())
    start = int(input().strip())
    count = int(input().strip())

    if soldiers == 0:
        #fptr.write("None")
        return

    # add code here
    #create circular linked list
    circular_list = CircularList()
    for i in range(1,soldiers+1):
        circular_list.insert(i)

    #kill soldiers
    while circular_list.get_num_links() != 1:
        killed, start = circular_list.delete_after(start, count)
        fptr.write(str(killed))
        fptr.write('\n')
    fptr.write(str(circular_list.first.data))

main()
