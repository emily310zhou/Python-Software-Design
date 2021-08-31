#  File: Work.py 

#  Description:  This program finds the minimum lines of code to write
#                before drinking the first cup of coffee.

#  Student Name:  Emily Zhou

#  Student UT EID:  ejz274

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 2/22/2020

#  Date Last Modified: 2/24/2020

import time

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here
  for i in range(n + 1):
      total_lines = calculate_lines(i,k)
      if total_lines >= n:
          min_lines = i
          break
        
  return min_lines #return the minimum number of lines to write before first cup of coffee

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
  lo = 0
  hi = n
 
  #iterates until the minimun lines needed before first cup is found by comparing its total
  #lines calculation and n 
  while lo <= hi:
    mid = (lo + hi) // 2
    total_lines = calculate_lines(mid,k)
    if total_lines < n:     
      lo = mid + 1  
    elif total_lines > n:
      hi = mid - 1  
    else:
      return mid  #return mid if its total lines = n
    
  return lo     #return the minimum v


#Helper function to calculate total lines written
#before falling asleep give a particular v
def calculate_lines(n,k):
    written_lines = 0
    lines = 1
    cups = 0
    while lines != 0:
        lines = n // k ** cups
        written_lines += lines
        cups += 1

    return written_lines  #return the total lines written before crashing
        
        
      
# main has been completed for you
# do NOT change anything below this line
def main():
  #read from file
  in_file = open("work.txt", "r")
  num_cases = int((in_file.readline()).strip())
  
  for i in range(num_cases):
    inp = (in_file.readline()).split()
    n = int(inp[0])
    k = int(inp[1])
    
    #conduct binary search and time it 
    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    #conduct linear search and time it
    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
