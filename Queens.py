#  Description: This program generates all unique solutions where no queen
#               can capture each another in a game of chess for a given board size. 

#  Student Name: Emily Zhou

#  Student UT EID: ejz274

#  Partner Name: Jenna Zhang

#  Partner UT EID: jz22846

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 3/12/2020

#  Date Last Modified: 3/13/2020


class Queens (object):
  # initialize the board
  def __init__ (self, n):
    self.board = []#initializes
    self.n = n#initializes
    self.solutionCount = 0#initializes
    for i in range (self.n):#loops through and fills board with *
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)#appaends formatted row to the board

  # print the board and formats
  def print_board (self):
    for i in range (self.n):#iterate through rows and columns
      for j in range (self.n):
        print (self.board[i][j], end = ' ')#formats the board
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n): #checking rows and columns
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):#check horizontal and vertical
        return False
    for i in range (self.n):#checking diagonals
      for j in range (self.n):
        row_diff = abs (row - i)    #incrementing rows
        col_diff = abs (col - j)    #incrementing cols
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):#check if Q in horizontal
          return False
    return True                     #else return true


  # do a recursive backtracking solution
  def recursive_solve (self, col):
    if (col == self.n):
      self.solutionCount += 1#increments the count value
      print()
      self.print_board()#prints out board
      print()#space for formatting
    else:
      for i in range (self.n):  #for loop increments rows
        if (self.is_valid(i, col)):#checks if placement is valid
          self.board[i][col] = 'Q'#puts in a queen in spot
          self.recursive_solve (col + 1)#increments column number and calls the function
          self.board[i][col] = '*'#clears previous placement of Q and replaced with *

  # if the problem has a solution print the board
  def solve (self):
      self.recursive_solve(0)#calls the recursive solve starting at 0
      return self.solutionCount#returns solution count

    
def main():
  size = int(input("Enter the size of board: "))#gets user input for dimensions
  while size > 8 or size < 1:#runs loop to make sure it's within bounds      
      size = int(input("Enter the size of board: "))#keep prompting
      
  # create a regular chess board
  game = Queens (size)

  # place the queens on the board
  print("There are",game.solve(),"solutions for a",size,"x",size,"board.")#number of solutions for selected board
  
             

main()
