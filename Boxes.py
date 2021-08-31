
#  File: Boxes.py

#  Description: This program finds the largest subset of nested boxes.

#  Student Name: Emily Zhou

#  Student UT EID: ejz274

#  Partner Name: Jenna Zhang
 
#  Partner UT EID: jz22846

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 3/6/2020

#  Date Last Modified: 3/9/2020


# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  if idx == len(box_list):#base case, check if finished iterating through entire list
    all_box_subsets.append(sub_set)
    return #returns back to calling function
  else:#finds all combinations
    c = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list,sub_set,idx+1,all_box_subsets)
    sub_sets_boxes(box_list,c,idx + 1,all_box_subsets)
    

# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):
  largest_size = 2#initializes the largest size
  nesting_list = []#initialize list for boxes that nest
  for sub_set in all_box_subsets:#go through all nesting subsets
    if len(sub_set) >= largest_size:#if length has more boxes than the largest size function
      if all(does_fit(sub_set[box_index],sub_set[box_index+1]) for box_index in range(len(sub_set)-1)):#checks does_fit
        nesting_list.append(sub_set)#append to nesting list
        largest_size = len(sub_set)#replace largest size value
       
  for sub_set in nesting_list:#goes through and double checks the list    
    if len(sub_set) == largest_size:
      all_nesting_boxes.append(sub_set)#append the subset to all nesting boxes


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # open the file for reading
  in_file = open ("./boxes.txt", "r")

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # print (box_list)
  # print()

  # sort the box list
  box_list.sort()
  #print (box_list)
  #print()

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)
   
  # initialize the size of the largest sub-set of nesting boxes
  largest_size = 0

  # create a list to hold the largest subsets of nesting boxes
  all_nesting_boxes = []

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes)

  # print all the largest subset of boxes
  if len(all_nesting_boxes) != 0:
    print('Largest Subset of Nesting Boxes')
    for subset in all_nesting_boxes:
      for box in subset:
        print(box)
      print()
  else:
    print('No Nesting Boxes')

if __name__ == "__main__":
  main()
