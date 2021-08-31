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

    # function for testing. displays the contents of your queue
    def display(self):
        for item in self.queue:
            print(item + ", ", end="")
        print()

#This is the 'main' function, make the program work by writing HELPER FUNCTIONS.
# The function is expected to return a List of strings.
# The function accepts a list of strings numbers as parameter.

def radix_sort(strings,dictionary):
    num_pass = 0
    queue_list = []
    sorted_list =[]

    #return empty list if string list is empty
    if len(strings) == 0:
        return []

    #creates list of queue objects
    for i in range(37):
        queue_i = Queue()
        queue_list.append(queue_i)

    #find max num of passes
    for word in strings:
        if len(word) > num_pass:
            num_pass = len(word)

    #perform radix sort
    for i in range(num_pass-1,-1,-1):

        #put word in right queue
        for word in strings:
            if len(word) <= i:
                queue_list[0].enqueue(word)
            else:
                numQ = dictionary[word[i]]
                queue_list[numQ].enqueue(word)

        #move semi sorted words to last queue
        for a in range(len(queue_list)):
            if not queue_list[a].is_empty():
                for j in range(queue_list[a].size()):
                    x = queue_list[a].dequeue()
                    queue_list[-1].enqueue(x)
            else:
                continue
            
        #assign semi sorted list to 'strings' for another pass
        strings = queue_list[-1].queue.copy()

        #empty out last queue
        for c in range(queue_list[-1].size()):
            queue_list[-1].dequeue()


        #print('Pass',i)
        #for k in range(37):
           # print('Q',k,':',end='')
            #queue_list[k].display()
        
    #return completely sorted strings
    return strings
        
    

def main(numbers):
    # We went ahead and created the dictionary for you
    dict = {
        '0': 0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,
        'a': 10,'b': 11,'c': 12,'d': 13,'e': 14,'f': 15,'g': 16,'h': 17,'i': 18,
        'j': 19,'k': 20,'l': 21,'m': 22,'n': 23,'o': 24,'p': 25,'q': 26,'r': 27,
        's': 28,'t': 29,'u': 30,'v': 31,'w': 32,'x': 33,'y': 34,'z': 35
    }

    #call helper function
    print(radix_sort(mylist,dict))


#mylist = ['z34','8fg6d','42cb3f','sd67mn9','7ty2d4','xc65ns3','51s23','720','khbw','plaq78d','520ce8','ij9944']
#mylist = ['13','z3','a13']
#mylist = ['9','4','7','6','5','2','3','1','8','0']
#mylist = ['vikas','saad','mahaa','deepthi','ryan']
#mylist = ['deepthi','mahaa','ryan','saad','vikas']
#mylist = ['itgv9','trqg2','27i8t','am02a','0rsct']
#mylist = ['311','96','84','137','21','269','28']
#mylist = ['137', '145', '158', '311', '495', '63', '84', '96']
#mylist = []
mylist = ['13','a13','z3']

main(mylist)
