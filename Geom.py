#  File: Geom.py

#  Description: This program does geometric functions relating to points and line.

#  Student Name: Emily Zhou

#  Student UT EID: ejz274

#  Partner Name: Jenna Zhang

#  Partner UT EID: jz22846

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 2/10/2020

#  Date Last Modified: 2/14/2020

import math #imports math so we can use math functions

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):#initializes the point object
    self.x = x #creates point for x coordinate
    self.y = y #creates point for y coordinate

  # get the distance other which is another Point object
  def dist (self, other): #distance function
    return round(math.hypot (self.x - other.x, self.y - other.y),2) #uses pythagorean thereom and rounds value

  # create a string representation of a Point(x, y)
  def __str__ (self):#what is printed out
    return '(' + str(self.x) + ', ' + str(self.y) + ')'#returns formatted point

  # determine if two points are equal
  def is_equal (self,a, b):
    tol = 1.0e-6 #value of valid difference
    return (abs (a - b) < tol)

  # test for equality of two objects
  def __eq__ (self, other):
    tol = 1.0e-6
    return is_equal(self.x,other.x) and is_equal(self.y,other.y)


class Line (object):#creates class for Line
  # line is defined by two Point objects p1 and p2
  # constructor assign default values if user does not define
  # the coordinates of p1 and p2 or the two points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-6
    if abs(p1_x - p2_x) < tol and abs(p1_y - p2_y) < tol:#if the points are the same, set to these points
      self.p1 = Point(0,0)
      self.p2 = Point(1,1)
    else:#else the points are what are in the txt file
      self.p1 = Point(p1_x,p1_y)
      self.p2 = Point(p2_x,p2_y)
      

  # returns True if the line is parallel to the x axis 
  # and False otherwise
  def is_parallel_x (self):
    if self.p1.y == self.p2.y:
      return True
    else:
      return False
    
  # returns True if the line is parallel to the y axis
  # and False otherwise
  def is_parallel_y (self):
    if self.p1.x == self.p2.x:
      return True
    else:
      return False
  
  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    if self.is_parallel_y():#it's parallel to y/doesn't have a slop
      return float('inf')
    else:
      return round((self.p2.y - self.p1.y)/(self.p2.x - self.p1.x),2)#else find the slope by finding diff in y/diff in x
    
  # determine the y-intercept of the line
  # return None if line is parallel to the y axis
  def y_intercept (self):
    if self.is_parallel_y():#if it's parallel to the y axis there is none
      return None
    if self.is_parallel_x():#if it's parallel to the x axis it's just be the y value
      return self.p1.y
    else:
      return round(self.p1.y - self.slope() * self.p1.x,2)#else plug in and return value
      

  # determine the x-intercept of the line
  # return None if line is parallel to the x axis
  def x_intercept (self):
    if self.is_parallel_x():#if it's parallel to the x axis there is none
      return None
    if self.is_parallel_y():#if it's parallel to the y axis it's just be the x value
      return self.p1.x
    else:
      return round((0 - self.y_intercept()) / self.slope(),2)#else calculate it using slope/intercepts
      
      
  # returns True if line is parallel to other and False otherwise
  def is_parallel (self, other):
    if self.slope()== other.slope():#if the slopes are the same!
      return True
    else:
      return False

  # returns True if line is perpendicular to other and False otherwise
  def is_perpendicular (self, other):
    if self.slope() * other.slope() == -1:#if the slopes multiplied together is -1
      return True
    elif (self.slope() == float('inf') and other.slope()==0) or (self.slope() == 0 and other.slope() == float('inf')):#unless they're parallel to y or x axis at the same time
      return True
    else:#if none of the above cases
      return False

  # returns True if Point p is on the line or an extension of it
  # and False otherwise
  def is_on_line (self, p):
    #checks point if line is parallel to y 
    if self.is_parallel_y():
      if self.p1.x == p.x:
        return True
      else:
        return False
    #checks the point if line is parallel to x
    elif self.is_parallel_x():
      if self.p1.y == p.y:
        return True
      else:
        return False
    #checks p for all non parallel lines
    else:
      if p.y == (self.slope() * p.x) + self.y_intercept():
        return True
      else:
        return False
    

  # returns a Point object which is the intersection point of line
  # and other or None if they are parallel
  def intersection_point (self, other):
    #initialize variables
    y_coordinate = 0
    x_intersection = 0
    y_intersection = 0
    if self.is_parallel(other):
      return None
    #find intersection if self line if parallel to y
    elif self.is_parallel_y():
      y_coordinate = round(other.slope() * self.p1.x + other.y_intercept(),2)
      intersection_obj = Point(self.p1.x, y_coordinate)
      return intersection_obj
    #find intersection if other line is parallel to y
    elif other.is_parallel_y():
      y_coordinate = round(self.slope() * other.p1.x + self.y_intercept(),2)
      intersection_obj = Point(other.p1.x,y_coordinate)
      return intersection_obj
    #for 'normal' lines and any parallel lines to x
    else:
      x_intersection = round((self.y_intercept() - other.y_intercept()) / (other.slope() - self.slope()),2)
      y_intersection = round((self.slope() * x_intersection) + self.y_intercept(),2)
      intersection_obj = Point(x_intersection, y_intersection)
      return intersection_obj


  # determine the perpendicular distance of Point p to the line
  # return 0 if p is on the line
  def perp_dist (self, p):
    #initialize variables
    intersection_object = ''
    neg_slope = 0
    perp_slope = 0
    p_y_intercept = 0
    x_intersection = 0
    y_intersection = 0
    if self.is_on_line(p):
      return 0
    else:
      #calculate line if the line is parallel to x - axis
      if self.is_parallel_x():
        intersection_obj = Point(p.x,self.p1.y)
        return p.dist(intersection_obj)
      #calculate distance if line is parallel to y- axis
      elif self.is_parallel_y():
        intersection_obj = Point(self.p1.x,p.y)
        return p.dist(intersection_obj)
      #calculate distance if line is not parallel to any axis
      else:
        neg_slope = self.slope()* -1
        perp_slope = 1 / neg_slope
        p_y_intercept = p.y - perp_slope * p.x
        x_intersection = (self.y_intercept() - p_y_intercept) / (perp_slope - self.slope())
        y_intersection = (self.slope() * x_intersection) + self.y_intercept()
        intersection_obj = Point(x_intersection, y_intersection)
        return p.dist(intersection_obj)
      

      
  # return True if two points are on the same side of the line
  # and neither points are on the line
  # return False if one or both points are on the line or both 
  # are on the opposite side of the line
  def on_same_side (self, p1, p2):
    y1_line = 0
    y2_line = 0
    #checks if points are on same side if line is parallel to y 
    if self.is_parallel_y():
      #returns true if both points are strictly on one side
      if p1.x < self.p1.x and p2.x < self.p1.x:
        return True
      elif p1.x > self.p1.x and p2.x > self.p1.x:
        return True
      #returns false if one or both points are on line
      else:
        return False
    #checks if points are on same side for all non-parallel y lines
    else:
      y1_line = (self.slope() * p1.x) + self.y_intercept()
      y2_line = (self.slope() * p2.x) + self.y_intercept()
      #returns true if both points are strictly on one side
      if y1_line < p1.y and y2_line < p2.y:
        return True
      elif y1_line > p1.y and y2_line > p2.y:
        return True
      #returns false if either points on line
      elif y1_line == p1.y or y2_line == p2.y:
        return False
      #returns false if points are on opposite sides
      else:
        return False
    

  # string representation of the line - one of three cases
  # y = c if parallel to the x axis
  # x = c if parallel to the y axis
  # y = m * x + b
  def __str__ (self):
    if self.is_parallel_y():
      return 'x = '+ str(self.p1.x)
    elif self.is_parallel_x():
      return 'y = ' + str(self.p1.y)
    else:
      return 'y = ' + str(self.slope()) + ' * x + ' + str(self.y_intercept())
      

#read file and return the coordinates of the line
def read_coordinate(file):
  file = file.readline().strip()
  file = file.split()
  return float(file[0]),float(file[1])

def main(): 
  # open file "geom.txt" for reading
  infile = open('geom.txt','r')

  # read the coordinates of the first Point P
  p_x,p_y = read_coordinate(infile)
  p_object = Point(p_x,p_y)

  # read the coordinates of the second Point Q
  q_x,q_y = read_coordinate(infile)
  q_object = Point(q_x,q_y)
  
  # print the coordinates of points P and Q
  print('Coordinates of P:',p_object)
  print('Coordinates of Q:',q_object)

  # print distance between P and Q
  print('Distance between P and Q:',p_object.dist(q_object))

  # print the slope of the line PQ
  pq_line_object = Line(p_x, p_y, q_x, q_y)
  print('Slope of PQ:',pq_line_object.slope())

  #print the y-intercept of the line PQ
  print('Y-Intercept of PQ:',pq_line_object.y_intercept())

  # print the x-intercept of the line PQ
  print('X-Intercept of PQ:',pq_line_object.x_intercept())

  # read the coordinates of the third Point A
  a_x,a_y = read_coordinate(infile)

  # read the coordinates of the fourth Point B
  b_x,b_y = read_coordinate(infile)

  # print the string representation of the line AB
  ab_line_object = Line(a_x, a_y, b_x, b_y)
  print('Line AB:',ab_line_object)

  # print if the lines PQ and AB are parallel or not
  if ab_line_object.is_parallel(pq_line_object):
    print('PQ is parallel to AB')
  else:
    print('PQ is not parallel to AB')

  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if ab_line_object.is_perpendicular(pq_line_object):
    print('PQ is perpendicular to AB')
  else:
    print('PQ is not perpendicular to AB')

  # print coordinates of the intersection point of PQ and AB if not parallel
  if not ab_line_object.is_parallel(pq_line_object):
    print('Intersection point of PQ and AB: ',pq_line_object.intersection_point(ab_line_object))

  # read the coordinates of the fifth Point G
  g_x,g_y = read_coordinate(infile)
  g_object = Point(g_x,g_y)
  
  # read the coordinates of the sixth Point H
  h_x,h_y = read_coordinate(infile)
  h_object = Point(h_x,h_y)

  # print if the the points G and H are on the same side of PQ
  if pq_line_object.on_same_side(g_object,h_object):
    print('G and H are on the same side of PQ')
  else:
    print('G and H are not on the same side of PQ')

  # print if the the points G and H are on the same side of AB
  if ab_line_object.on_same_side(g_object,h_object):
    print('G and H are on the same side of AB')
  else:
    print('G and H are not on the same side of AB')

  # close file "geom.txt"
  infile.close()

if __name__ == "__main__":
  main()
