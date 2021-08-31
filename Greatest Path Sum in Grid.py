# counts all the possible paths in a grid recursively
# 
# The function is expected to return an INTEGER.
#
# The function accepts following parameters:
#  1. INTEGER n, the dimensions of the grid
#  2. INTEGER row, current row
#  3. INTEGER col, current col
#
def count_paths(n, row, col):
    # Write your code here
    
    pascal_grid = [[0] * n for i in range (n)]
    pascal_grid[0] = [1]*n
    
    for row_idx in range(n):
        pascal_grid[row_idx][0] = 1
        
    
    for col_idx in range (col+1,n):
        for row_idx in range(row+1,n):
            pascal_grid[row_idx][col_idx] = pascal_grid[row_idx][col_idx-1] + pascal_grid[row_idx-1][col_idx]

    return pascal_grid [n-1][n-1]



#
# recursively gets the greatest sum of all the paths in the grid
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D LIST grid, the grid itself
#  2. INTEGER n, the dimensions of the grid
#  3. INTEGER row, current row
#  4. INTEGER col, current col
#

def path_sum(grid, n, row, col):
    sum_grid = [[0] * n for i in range(n)]
    sum_grid[row][col] = grid [row][col]
        
    #top column sums
    for i in range (1,n):
        sum_grid[row][i] = grid[row][i] + sum_grid[row][i-1]
  
    for i in range (1,n):
        sum_grid[i][col] = grid[i][col] + sum_grid[i-1][col]

    for col_idx in range (col+1,n):
        for row_idx in range(row+1,n):
            if sum_grid[row_idx-1][col_idx] >= sum_grid[row_idx][col_idx-1]:
                sum_grid[row_idx][col_idx] = grid[row_idx][col_idx] + sum_grid[row_idx-1][col_idx]
            else:
                sum_grid[row_idx][col_idx] = grid[row_idx][col_idx] + sum_grid[row_idx][col_idx-1]

    for i in sum_grid:
        print(i)

    return sum_grid[n-1][n-1]

#
# Complete the 'main' function below.
#
# The function accepts following parameters:
#  1. INTEGER n, the dimensions of the grid
#  2. 2D LIST grid, the grid itself
#

def main(n, grid):
    # Write your code here
    pass



#
# Complete the 'get_max_path' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D LIST grid, the grid itself
#  2. INTEGER n, the dimensions of the grid
#  3. INTEGER row, current row
#  4. INTEGER col, current col
#

def sum_grid(grid, n, row, col):
    sum_grid = [[0] * n for i in range(n)]
    sum_grid[row][col] = grid [row][col]
        
    #top column sums
    for i in range (1,n):
        sum_grid[row][i] = grid[row][i] + sum_grid[row][i-1]
  
    for i in range (1,n):
        sum_grid[i][col] = grid[i][col] + sum_grid[i-1][col]

    for col_idx in range (col+1,n):
        for row_idx in range(row+1,n):
            if sum_grid[row_idx-1][col_idx] >= sum_grid[row_idx][col_idx-1]:
                sum_grid[row_idx][col_idx] = grid[row_idx][col_idx] + sum_grid[row_idx-1][col_idx]
            else:
                sum_grid[row_idx][col_idx] = grid[row_idx][col_idx] + sum_grid[row_idx][col_idx-1]
    
    return sum_grid

def get_max_path(grid, n, row, col):
    # Write your code here
    start_row = n-1
    start_col = n-1

    s_grid = sum_grid(grid,n,row,col)
    
    path_list = [grid[start_row][start_col]]
    
    comp_value = s_grid[start_row][start_col] - grid[start_row][start_col]

    row_idx = start_row
    col_idx = start_col 
    
    while comp_value != s_grid[row][col]:
        if comp_value == s_grid[row_idx][col_idx-1]:
            path_list.append(grid[row_idx][col_idx-1])
            comp_value = comp_value - grid[row_idx][col_idx-1]
            col_idx -= 1
        if comp_value == s_grid[row_idx-1][col_idx]:
            path_list.append(grid[row_idx-1][col_idx])
            comp_value = comp_value - grid[row_idx-1][col_idx]
            row_idx -= 1
    
    path_list.append(grid[row][col])
    path_list.reverse()
    return path_list


grid = [[1,2,3],[4,5,6],[7,8,9]]
#grid = [[8,5,22,97],[49,49,99,40],[81,49,31,73],[52,70,95,23]]
#grid = [[20,95,63],[26,97,17],[44,20,45]]
#grid = [[20,20,20],[20,20,20],[20,20,20]]
#for i in grid:
   # print(i)
print(count_paths(12,0,0))
print('max sum:',path_sum(grid,3,0,0))
print('path list:',get_max_path(grid,3,0,0))
