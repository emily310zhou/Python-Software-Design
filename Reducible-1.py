#  File: Reducible.py

#  Description: This program finds the longest reducible word. 

#  Student Name: Emily Zhou

#  Student UT EID: ejz274

#  Partner Name: Jenna Zhang

#  Partner UT EID: jz22846

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 3/24/20

#  Date Last Modified: 3/30/20


# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):#checks first if n is 1
    return False

  limit = int (n ** 0.5) + 1#finding square root of number + 1
  div = 2 #starting value
  while (div < limit):
    if (n % div == 0):#if remainder is 0
      return False#not a prime num
    div += 1#increment div
  return True#else it is a prime num

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
  hash_idx = 0#initialize hash index
  for j in range (len(s)):#runs through given string
    letter = ord (s[j]) - 96 #changes character to unicode
    hash_idx = (hash_idx * 26 + letter) % size #calculates hash index
  return hash_idx #returns index to be hashed to


# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size (s, const):
  step_size = const - (hash_word(s,const) % const)#calculates step size double hashes the word 
  return step_size


# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):
  hash_index = hash_word(s,len(hash_table))#calls hash word function
  if hash_table[hash_index] == '':#if it's empty
    hash_table[hash_index] = s#put it in there
  else:
    hash_sum = hash_index
    step = step_size(s,13)#find the positioning
    while hash_table[hash_index] != '':#while it's empty
      hash_sum += step#increment
      hash_index = hash_sum % len(hash_table)
    hash_table[hash_index] = s#put it in there


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
  hash_index = hash_word(s,len(hash_table))#calls the hash word function

  if s == 'a' or s == 'i' or s == 'o':#base case
    return True
  if hash_table[hash_index] == s:#looks for s in hash table
    return True
  elif hash_table[hash_index] == '':#if it's empty
    return False 
  else:
    hash_sum = hash_index #initializes hash sum based on hash index
    step = step_size(s,13) #gets step size from step size function
    while hash_table[hash_index] != '':#while another string is at index
      hash_sum += step #increments hash sum
      hash_index = hash_sum % len(hash_table)
      if hash_table[hash_index] == s:#checks if s is in hash table
        return True
      if hash_table[hash_index] == '':
        return False


# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if s == 'a' or s == 'o' or s == 'i':#base case
    return True
  
  if find_word(s,hash_memo):#checks hash memo
    return True
  
  if not find_word(s,hash_table):#checks hash table
    return False
  
  for i in range(len(s)):#goes through the word
    s_list = list(s)#breaks characters into list
    s_list.pop(i)#pops out i
    new_s = ''.join(s_list) #rejoins the word                 
    if is_reducible(new_s,hash_table,hash_memo):#calls recursive function again
      if find_word(new_s, hash_table):#checks hash table 
        insert_word(new_s,hash_memo) #calls insert word function
        return True
  return False #if popping letter didn't create reducible word


# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
  longest_len = 0#initializes
  longest_words = []#initializes
  for i in string_list:#goes through list
    if len(i) > longest_len: #if finds longer word
      longest_len = len(i) #replace longest length
  for i in string_list:#goes through list again
    if len(i) == longest_len:
      longest_words.append(i)#finds longest word and put in list
  return longest_words#return the list

def main():
  # create an empty word_list
  word_list = []

  # open the file words.txt
  infile = open('words.txt','r')

  # read words from words.txt and append to word_list
  word = infile.readline().strip()
  word_list.append(word)
  while word != '':
      word = infile.readline().strip()
      word_list.append(word)

  # close file words.txt
  infile.close()

  # find length of word_list
  len_word_list = len(word_list)
 
  # determine prime number N that is greater than twice
  # the length of the word_list
  N = 2 * len_word_list
  while not is_prime(N):
      N += 1

  # create and empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  hash_list = [''] * N

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for word in word_list:
    insert_word(word,hash_list)
  
  # create an empty hash_memo
  hash_memo = []

  # populate the hash_memo with M blank strings
  M = 27000
  while not is_prime(M):
    M += 1

  hash_memo = [''] * M

  # create and empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  for word in word_list:
    if is_reducible(word, hash_list, hash_memo):
      reducible_words.append(word)
         
  # find words of the maximum length in reducible_words
  max_length_words = get_longest_words(reducible_words)

  # print the words of maximum length in alphabetical order
  # one word per line
  max_length_words.sort()
  for i in max_length_words:
    print(i)

# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
