#  File: Spiral.py

#  Description: This program prints out a spiral (matrix) of numbers based
#               on the user's specified dimensions and starting number.

#  Student's Name: Emily Zhou

#  Student's UT EID: ejz274

#  Partner's Name: Jenna Zhang

#  Partner's UT EID: jz22846

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 2/15/2020

#  Date Last Modified: 2/17/2020


#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged
#          in a spiral
def create_spiral (dim):
    #initialize variables
    col_start = 0
    row = 0
    b_start = dim - 1
    b_stop = -1
    c_row_start = 1
    c_end_row = dim
    d_next_start = 1
    d_end = dim
    d_row = dim - 1
    e_row_start = dim - 2
    e_row_stop = 0
    e_col = dim - 1

    dim_squared = 0 #initializes the dimension that user will input
    two_dim_list = [[0]* dim for i in range(dim)] #creates a 2d list based on given dimensions

    for i in range(dim,2,-2):
        dim_squared = i **2 #squares the value for dimension
        for b in range(b_start,b_stop,-1): #prints top line row
            two_dim_list[row][b] = dim_squared
            dim_squared -= 1#resets value for dimension
            
        for c in range(c_row_start,c_end_row): #a is column // prints right column column
            two_dim_list[c][col_start] = dim_squared
            dim_squared -= 1#resets value for dimension
                 
        for d in range(d_next_start,d_end):
            two_dim_list[d_row][d] = dim_squared #prints botoom line
            dim_squared -= 1#resets value for dimension
        for e in range(e_row_start,e_row_stop,-1):
            two_dim_list[e][e_col] = dim_squared #prints left column
            dim_squared -= 1#resets value for dimension
            
        #adjusts values after section of grid is created
        row += 1
        b_start-= 1
        b_stop += 1
        col_start += 1
        c_row_start += 1
        c_end_row -= 1
        d_next_start += 1
        d_end -= 1
        d_row -= 1
        e_row_start -= 1
        e_row_stop += 1
        e_col -= 1

    #sets the center value
    for row in range(dim):
        for col in range(dim):#searches through the 2d list
            if two_dim_list[row][col] == 0:#where the value is 0
                two_dim_list[row][col] = 1#replace it with 1
                
    return two_dim_list#return the completed full grid
    
#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number withing the range of numbers in
#         the grid
#  Output: sub-grid surrounding the parameter val in the grid
#          sub-grid could be 1-D or 2-D list
def sub_grid (grid, val):
    #initializes the 2d lists -- 4 different sizes
    sub_grid_3x3 = [[0] * 3 for i in range(3)]
    sub_grid_2x3 = [[0] * 3 for i in range(2)]
    sub_grid_2x2 = [[0] * 2 for i in range(2)]
    sub_grid_3x2 = [[0] * 2 for i in range(3)]
    
    #find value in list and return coordinates
    for row, grid_list in enumerate(grid):#goes through the grid
        for num in grid_list:
            if num == val:#if it matches val
                val_row = row #find the row of the location
                val_col = grid_list.index(num) #find the column of location

    #determine if value is edge piece
    if len(grid) == 1 and val == 1:#if it happens to be a one by one list
        return grid
    elif val_row == 0 and val_col == 0: #top left corner piece
        for row in range(2):
            for col in range(2):#go through the 2x2 surrounding numbers
                sub_grid_2x2[row][col] = grid[val_row][val_col]#put values from grid into the sub grid
                val_col += 1#add one to location of col
            val_col -= 2#reset location of col
            val_row += 1 #add one to location of row
        return sub_grid_2x2#return filled sub grid
    elif val_row == len(grid) - 1 and val_col == 0: #bottom left corner
        for row in range(2):
            for col in range(2):#go through the 2x2 surrounding numbers
                sub_grid_2x2[row][col] = grid[val_row-1][val_col]#put values from grid into the sub grid
                val_col += 1#add one to location of col
            val_col -= 2#reset location of col
            val_row += 1#add one to location of row
        return sub_grid_2x2#return filled sub grid
    elif val_row == 0 and val_col == len(grid) - 1: #top right corner
        for row in range(2):
            for col in range(2):#go through the 2x2 surrounding numbers
                sub_grid_2x2[row][col] = grid[val_row][val_col-1]#put values from grid into the sub grid
                val_col += 1
            val_col -= 2#reset location of col
            val_row += 1
        return sub_grid_2x2#return filled sub grid
    elif val_row == len(grid) - 1 and val_col == len(grid) - 1: #bottom right corner
        for row in range(2):
            for col in range(2):#go through the 2x2 surrounding numbers
                sub_grid_2x2[row][col] = grid[val_row-1][val_col-1]#put values from grid into the sub grid
                val_col += 1
            val_col -= 2#reset location of columns
            val_row += 1
        return sub_grid_2x2#return filled sub grid
    elif val_row == 0: #top row
        for row in range(2):
            for col in range(3):#go through the 2x3 surrounding numbers
                sub_grid_2x3[row][col] = grid[val_row][val_col-1]#put values from grid into the sub grid
                val_col += 1
            val_col -= 3#reset location of columns
            val_row += 1
        return sub_grid_2x3#return filled sub grid
    elif val_row == len(grid) - 1: #bottom row
        for row in range(2):
            for col in range(3):#go through the 2x3 surrounding numbers
                sub_grid_2x3[row][col] = grid[val_row-1][val_col-1]#put values from grid into the sub grid
                val_col += 1
            val_col -= 3#reset location of columns
            val_row += 1
        return sub_grid_2x3#return filled sub grid
    elif val_col == 0: #left column
        for row in range(3):
            for col in range(2):#go through the 3x2 surrounding numbers
                sub_grid_3x2[row][col] = grid[val_row-1][val_col]#put values from grid into the sub grid
                val_col += 1
            val_col -= 2#reset location of columns
            val_row += 1
        return sub_grid_3x2
    elif val_col == len(grid) - 1: #right column
        for row in range(3):
            for col in range(2):#go through the 3x2 surrounding numbers
                sub_grid_3x2[row][col] = grid[val_row-1][val_col-1]#put values from grid into the sub grid
                val_col += 1
            val_col -= 2#reset location of columns
            val_row += 1
        return sub_grid_3x2#return filled sub grid
    else: #normal 3 by 3 case
        for row in range(3):
            for col in range(3):#go through the 3x3 surrounding numbers
                sub_grid_3x3[row][col] = grid[val_row-1][val_col-1]#put values from grid into the sub grid
                val_col += 1
            val_col -= 3#reset location of columns
            val_row += 1
        return sub_grid_3x3#return filled sub grid

def main():
  # prompt user to enter dimension of grid
  dimension = int(input('Enter dimension: '))
  if dimension % 2 == 0:#if it's even
      dimension += 1#add one
      
  # prompt user to enter value in grid
  value = int(input('Enter number in spiral: '))

  # print subgrid surrounding the value
  if  1 <= value <= (dimension**2):#checks that value is in range
      full_grid = create_spiral(dimension)#creates spiral
      small_grid = sub_grid(full_grid,value)#calls sub grid function

      num_row = len(small_grid)#finds dimension of small grid
      num_column = len(small_grid[0])#finds dimension of small grid
      for row in range(num_row):
          for col in range(num_column):#prints it/formats it through the for loop
              print(small_grid[row][col], end = ' ')
          print()#separate line for formatting
  else:
      print('Number not in Range')#else prints not in range.


if __name__ == "__main__":
  main()
