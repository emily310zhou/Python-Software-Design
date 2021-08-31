#  File: Nim.py

#  Description: This program predicts the optimal first move for the Nim game.

#  Student's Name: Emily Zhou

#  Student's UT EID: ejz274
 
#  Partner's Name: Jenna Zhang

#  Partner's UT EID: jz22846

#  Course Name: CS 313E 

#  Unique Number: 50305

#  Date Created: 1/26/2020

#  Date Last Modified: 1/29/2020

#  Input: heaps is a list of integers giving the count in each heap
#  Output: function returns a single integer which is the nim-sum
def nim_sum (heaps):
  nim_sum_x = 0 #initializes the nim sum value
  
  for index in range(len(heaps)):#for loop will run through numbers in the file and find nim sum
    nim_sum_x = nim_sum_x ^ heaps[index] # calculates nim sum
  return nim_sum_x 


#  Input: heaps is a list of integers giving the count in each heap
#         nim_sum is an integer 
#  Output: function returns two integers. The first integer is number
#          of counters that has to be removed. The second integer is
#          the number of the heap from which the counters are removed.
#          If the nim_sum is 0, then return 0, 0
def find_heap (heaps, nim_sum):
  individual_nim_sum = 0 #initializes the values for nim sum for individual heaps
  ind_nim_sum_list = [] #creates an empty list for the individual heap values
  counters_take = 0 #initializes a value for the counters to take
  
  if nim_sum == 0:#this means the player is going to lose the game
    return 0,0
  else:
    for index in range(len(heaps)):#runs through and finds the individual nim sums and puts it into the list
      individual_nim_sum = heaps[index] ^ nim_sum #finds nim sums
      ind_nim_sum_list.append(individual_nim_sum) #appends it to the list
    for index in range(len(heaps)):#runs through and compares the list with individual nim sums with the original nim sum values
      if heaps[index] > ind_nim_sum_list[index]: #if the original heap's nim sum value is greater than the individual nim sum
        counters_take = heaps[index] - ind_nim_sum_list[index] #calculates the number of counters to take to win(difference between heap's nimsum and individual nimsum
        return counters_take, index + 1 #returns the number of counters to take and the heap to take from(index+1)
        break #breaks out of the loop
 
def main():#main function
  #intializes all the values!
  i = 0
  infile = ''
  num_data_sets = ''
  data_line = ''
  heap_size = ''
  heaps_nim_sum = 0
  counters_to_take = 0
  heap_to_take = 0
  
  infile = open('nim.txt','r') #opens the text file
  num_data_sets = int(infile.readline()) #reads line in text file and puts each line into the data set
  while i < num_data_sets:
     data_line =(infile.readline().rstrip())#takes away next line spaces between the text
     heap_size = data_line.split()#separates values by spaces between each number
     heap_size = [int(x) for x in heap_size] #converts all values to ints
     heaps_nim_sum = nim_sum(heap_size)#calls the nim sum functions
     counters_to_take , heap_to_take = find_heap(heap_size, heaps_nim_sum) #puts return values into variables
     if counters_to_take == 0 and heap_to_take == 0: #if else to determine what to print out
       print("Lose Game") #prints out Lose Game
     else:
        print("Remove", counters_to_take, "counters from Heap", heap_to_take) #formats the information relating to how many/which heap to take from
     heap_size = [] #empties heap size list
     i += 1 #increments for the while loop
  infile.close()#closes the file

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
