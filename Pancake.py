#  File: Pancake.py

#  Description: This program sorts pancakes by size so that the largest pancake
#               is at the bottom of the stack and the smallest one on top.

#  Student's Name: Emily Zhou

#  Student's UT EID: ejz274

#  Partner's Name: Jenna Zhang

#  Partner's UT EID:  jz22846

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 2/18/2020

#  Date Last Modified: 2/21/2020

#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula 
#          this is a list of lists
#          the last item in this list is the sorted stack

def sort_pancakes ( pancakes ):

  #copy pancake list and initializes starting values
  maximum = max(pancakes)
  every_flip = []
  flip_list_var = len(pancakes)
  sorted_list = pancakes.copy()
  pancakes_list = pancakes.copy()

  #sorts the list to determine the correct order using selection sort
  for i in range(len(sorted_list) - 1):
    index_smallest = i
    for j in range(i + 1, len(sorted_list)):
      if sorted_list[j] < sorted_list[index_smallest]:
        index_smallest = j
    temp = sorted_list[i]
    sorted_list[i] = sorted_list[index_smallest]
    sorted_list[index_smallest] = temp

  #if list is already in order
  if all(i<=j for i,j in zip(pancakes,pancakes[1:])):
    every_flip.append(pancakes)
  #if list is in opposite order - reverse it
  elif all(i>=j for i,j in zip(pancakes,pancakes[1:])):
    pancakes.reverse()
    every_flip.append(pancakes)
  #if list is not ordered at all
  else:
    i = len(pancakes) - 1#initializes value for i
    while sorted_list[i] != pancakes[i] or sorted_list[i] == pancakes[i]:#starts from last value, but compares it to the sorted list index to check if it's in right place
      if sorted_list[i] == pancakes[i]:#if it happens to be in the right place already before flipping
        pancakes_list.remove(maximum)#removes from a separate list used to find mix values
        maximum = max(pancakes_list)#finds the new maximum of remaining numbers
        flip_list_var -= 1#subtracts one from flip list variable
        i -= 1#decrements one from i
      else:#run through flip sequence
        max_index = pancakes.index(maximum)#finds index of the max
        if max_index != 0:#if the max index isn't already at the top of the stack
          flip_index = max_index + 1#finds index to slice the list
          flip_list1 = pancakes[:flip_index]#slices the list after the max value
          flip_list1.reverse()#flips max value to the top of stack
          pancakes[:flip_index] = flip_list1#puts back together with pancakes list
          pancakes_copy = pancakes.copy() #makes a copy
          every_flip.append(pancakes_copy)#appends it
        
        #SECOND FLIP
        second_flip = pancakes[:flip_list_var]#slices the max value to the bottom in respective location based on flip list variable
        second_flip.reverse()#flips it
        pancakes[:flip_list_var] = second_flip#sets back to the pancakes list
        

        pancakes_copy = pancakes.copy()#makes a copy
        every_flip.append(pancakes_copy)#appends it
        flip_list_var -= 1#decrements the flip list variable
        i -= 1#decrements i
        pancakes_list.remove(maximum)#removes the value from the list where we find the next max value
        maximum = max(pancakes_list)#finds the next max value
      if i == 0:#if the location of the index is at the beginning of the list
        break#break out of the loop

  #return list of flipped pancakes 
  return every_flip    

def main():
  # open the file pancakes.txt for reading
  in_file = open ("./pancakes.txt", "r")

  line = in_file.readline()
  line = line.strip()
  line = line.split()
  print (line)

  #Create list of pancake size
  pancakes = []
  for item in line:
    pancakes.append (int(item))

  # print content of list before flipping
  print ("Initial Order of Pancakes = ", pancakes)

  # call the function to sort the pancakes
  every_flip = sort_pancakes ( pancakes )

  # print the contents of the pancake stack after
  # every flip
  for i in range (len(every_flip)):
    print (every_flip[i])

  # print content of list after all the flipping
  print ("Final Order of Pancakes = ", every_flip[-1])

if __name__ == "__main__":
  main()
