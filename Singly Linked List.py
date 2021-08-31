class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

####################################################################

class LinkedList (object):
  # initialize the linked list
  def __init__ (self):
      self.first = None

  # get number of links 
  def get_num_links (self):
    current = self.first
    if current == None:
        return self.num_links
    else:
       self.num_links += 1
        
    while current.next != None:
        self.num_links += 1
        current = current.next
    
    return self.num_links
  
  # add an item at the beginning of the list
  def insert_first (self, data):
    #GIVEN TO US IN HACKER RANK

  # add an item at the end of a list
  def insert_last (self, data):
    new_link = Link (data)
    current = self.first 
    if current == None:
      self.first = new_link
      return 
    while (current.next != None):
      current = current.next    
    current.next = new_link

  # add an item in an ordered list in ascending order
  def insert_in_order (self, data):
    new_link = Link(data)
    current = self.first 

    if current == None: #if LL is empty
        self.first = new_link
    elif data < current.data: #if new value is less than first link
        self.insert_first(data)      
    else:                     #traverse through LL if new value is greater than head
        while current != None:
          if current.next == None and current.data <= new_link.data:
            current.next = new_link
            return
          elif current.data <= new_link.data and current.next.data > new_link.data:
            new_link.next = current.next
            current.next = new_link
            return
          else:             #current.data <= new_link.data
            current = current.next
      

  # search in an unordered list, return None if not found
  def find_unordered (self, data):
    current = self.first
    if current == None:
      return None 
    while current.data != data:
      if (current.next == None):
        return None
      else:
        current = current.next

    return current


  # Search in an ordered list, return None if not found
  def find_ordered (self, data):
    current = self.first
    if (current == None):
      return None
    while (current.data != data):
      if (current.next == None):#end of list
        return None
      elif (current.data > data):#greater than value
        return None
      else:
        current = current.next

    return current

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, data):
    previous = self.first
    current = self.firsT
    if (current == None):
        return None
    while (current.data != data):
        if (current.next == None):
            return None
        else:
            previous = current
            current = current.next
    if (current == self.first):
        self.first = self.first.next
    else:
        previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    ### GIVEN TO US

  # Copy the contents of a list and return new list
  def copy_list (self):
    new_list = LinkedList()
    current = self.first 
    if current == None:
        return new_list
    while current != None:
        new_list.insert_last(current.data)
        current = current.next
       
    return new_list

  # Reverse the contents of a list and return new list
  def reverse_list (self):
    new_list = LinkedList()
    current = self.first 

    if current == None:
        return new_list
    
    while current != None:
        new_list.insert_first(current.data)
        current = current.next
    
    return new_list

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):
    sorted_list = LinkedList()
    current = self.first 

    if self.get_num_links() == 0:
        return sorted_list
    
    while current != None:
        sorted_list.insert_in_order(current.data)
        current = current.next 
    
    return sorted_list
            

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    if current == None:
      return True
    else:
      while current.next != None:
        if current.data <= current.next.data:
          current = current.next
        else:
          return False
      return True

  # Return True if a list is empty or False otherwise
  def is_empty (self):
    if self.get_num_links() == 0:
      return True
    else:
      return False

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
     merge_list = LinkedList()
        self_current = self.first
        other_current = other.first
        
        if self.get_num_links == 0 and other.get_num_links == 0:
            return merge_list
          
        while self_current != None and other_current != None:
          if self_current.data < other_current.data:
            merge_list.insert_last(self_current.data)
            self_current = self_current.next
          
          elif self_current.data > other_current.data:
            merge_list.insert_last(other_current.data)
          	other_current = other_current.next 
          
        	else: #self_current.data == other_current.data 
            merge_list.insert_last(self_current.data)
            merge_list.insert_last(other_current.data)
            self_current = self_current.next
            other_current = other_current.next
        
        if self_current == None:
          while other_current != None:
            merge_list.insert_last(other_current.data)
            other_current = other_current.next
        else:
          while self_current != None:
            merge_list.insert_last(self_current.data)
            self_current = self_current.next
        
        return merge_list

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):

    #if two list is empty, return true
    if self.get_num_links() == 0 and other.get_num_links() == 0:
        return True
    #if two list have diff num of links, return false
    elif self.get_num_links() != other.get_num_links():
        return False
    #if two list have same num links, check link for link
    else: 
        self_current = self.first 
        other_current = other.first
        while self_current != None and other_current != None:
            if self_current.data == other_current.data:
                self_current = self_current.next
                other_current = other_current.next
            else:
                return False
        return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    # your code goes here

    no_duplicates = LinkedList()
    current = self.first

    #if orginal list is empty
    if self.get_num_links() == 0:
      return no_duplicates

    while current != None:
      if no_duplicates.first == None:
        no_duplicates.insert_last(current.data)
      else:
        if no_duplicates.find_unordered(current.data) == None:
          no_duplicates.insert_last(current.data)  
      current = current.next

    return no_duplicates
        

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()

if __name__ == "__main__":
  main()
