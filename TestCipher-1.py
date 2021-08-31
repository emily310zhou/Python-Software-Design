#  File: TestCipher.py

#  Description: This program will decode and encrypt messages using the rail
#               fence cipher and vigenere cipher. 

#  Student's Name: Emily Zhou

#  Student's UT EID: ejz 274
 
#  Partner's Name: Jenna Zhang

#  Partner's UT EID: jz22846

#  Course Name: CS 313E 

#  Unique Number: 50305

#  Date Created: 2/2/20

#  Date Last Modified:2/7/20

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    #initializes all values
    row, col = -1,-1
    flag = 'top'
    two_dim_list = []
    strng_only_list = []
    strng_joined_list = []
    
    if key < 2 or key > len(strng):#if key is out of range
        key = 2 #default set it to 2
    two_dim_list = [['-' for col in range(len(strng))] for row in range(key)]#creates 2d list with dashes
    #To populate the 2D list with strng characters
    #inserts characters in the zigzag pattern
    for char in strng:
        if flag == 'top':#flag indicate when to switch zigzagging direction
            row += 1
            col += 1
            two_dim_list[row][col] = char#replaces dash with the character
            if row == key - 1:
                flag = 'bottom'
        else:#if it needs to go from bottom to top
           row -= 1
           col += 1
           two_dim_list[row][col] = char#replaces dash with the character
           if row == 0:
                flag = 'top'
    #To populate another 2D list with only strng characters
    #goes through 2d list and puts characters/non dashes into another list
    for row in range(key):
        for col in range(len(strng)):
            if two_dim_list[row][col] != '-':#if the character is not a dash aka it's a letter
                strng_only_list.append(two_dim_list[row][col])
    strng_joined_list = ''.join(strng_only_list)#puts all the encoded characters together into one string
    return strng_joined_list #completed encoded string
    
    
        

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    strng_list = list(strng)#separates the string into each character in a list
    #initialize all values!
    strng_list_index = -1
    row, col = -1,-1
    flag = 'top'
    read = 'top'
    decoded_list = []
    two_dim_list = []

    if key < 2 or key > len(strng):#if key is out of range
        key = 2#default set to 2
    two_dim_list = [['-' for col in range(len(strng))] for row in range(key)]#reconsrtuct the list 
    for char in strng:
        if flag == 'top':
            row += 1#moves rows one down
            col += 1#moves columns one to the right
            two_dim_list[row][col] = '!'#put exclamation where all the letters should be/marked where characters should be
            if row == key - 1:#when it hits the bottom
                flag = 'bottom'#change the flag
        else:#flag is not 'top'
            row -= 1#moves rows one up
            col += 1#moves rows one to the right
            two_dim_list[row][col] = '!'#marks where chracters should be
            if row == 0:#reverse direction when it hits the top
                 flag = 'top'
                
    for row in range(key):#going through 2d list to replace ! with letters
        for col in range(len(strng)):
            if two_dim_list[row][col] == '!':#if there's an exclamation mark
                strng_list_index += 1
                two_dim_list[row][col] = strng_list[strng_list_index]#puts letter in the same spot as exclamation
    
    row, col = 0,0#reset values from before

    for char in strng_list:#reading through the list with dashes and letters
        if read == 'top':
            if two_dim_list[row][col] != '-':#if the value in list is not a dash/there's a letter
                decoded_list.append(two_dim_list[row][col])#append it to decoded list
                row += 1#moves the row down one
                col += 1#Moves the row to the right one
            if row == key - 1:#switch directions
                read = 'bottom'
        else:
            if two_dim_list[row][col] != '-':#if the value in list is not a dash/there's a letter
                decoded_list.append(two_dim_list[row][col])#append the letter to the decoded list
                row -= 1#moves the row up one
                col += 1#moves the column to the right one
            if row == 0:#change directions
                read = 'top' 
 
    return ''.join(decoded_list)#sends back the decoded text in one string
    
    
#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  lowercase_strng = []#initializes empty string
  strng = strng.lower()#makes all values lower case
  for char in strng:
      if char.isalpha():#checks if it's a letter
          lowercase_strng.append(char)#if it is, appends it to the list
  return ''.join(lowercase_strng)#returns the lowercase, alpha only string

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vignere algorithm. You may not use a 2-D list 
def encode_character (p, s):
  #initializes all values
  row = 0
  col = 0
  add_num = 0
  alpha = 0
  unicode_letter = 0
  letter = ''
  
  row = ord(p)#converts pass phrase character to its unicode
  col = ord(s)#converts plaintext character to its unicode
  add_num = row + col#takes the sum of the two values to find the encrypted character
  #from here, there are two possible options for finding the encrypted letter because in the vigenere table there are at least two diagonals for every letter except z
  if add_num < 220:#options one/diagonal 1
      alpha = add_num - 194#makes the unicode value correspond to the alphabet number
      unicode_letter = alpha + 97#converts the letter's spot in the alphabet to unicode
      letter = chr(unicode_letter)#unicode to character
      return letter
  else: #option 2/diagonal 2
      alpha = add_num - 220#makes the unicode value correspond to the alphabet number
      unicode_letter = alpha + 97#converts the letter's spot in the alphabet to unicode
      letter = chr(unicode_letter)#unicode to character
      return letter

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vignere algorithm. You may not use a 2-D list 
def decode_character (p, s):
   #initalize values 
   decoded_char = ''
   num = 0
   
   p = ord(p)#converts pass phrase character to its unicode
   s = ord(s)#converts plaintext character to its unicode 
   #finds the unicode value for the decoded letter/character
   #similarly there are two options/diagonals when decoding
   if s >= p:
       num = s - p#finding the difference
       num += 97 #converts the letter's spot in the alphabet to unicode
       decoded_char = chr(num) #unicode to character
   else:
       num = s - p#finding the difference
       num += 123#converts the letter's spot in the alphabet to unicode
       decoded_char = chr(num)#unicode to character
   return decoded_char

#  Input: strng is a string of characters and pass is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vignere algorithm
def vigenere_encode ( strng, phrase ):
    #initialize values
    i = 0
    phrase_list = []
    strng_list = []
    encoded_list = []
    repeat = 0
    remainder = 0
    
    strng = filter_string(strng)#removes non lowercase letters
    phrase_list = list(phrase)#turns string into list of separate characters
    strng_list = list(strng)#turns string into list of separate characters
    repeat = len(strng) // len(phrase)#this finds how many times the full pass phrase appears in the plain text
    phrase_list = phrase_list * repeat #replicates the list for the amount of times it fully appears in the plain text
    remainder = len(strng) % len(phrase)#finds the amount of remaining letters
    #this while loop appends the list with the remaining letters
    while i < remainder:
        phrase_list.append(phrase_list[i])
        i += 1
    for i in range(len(strng)):#adds encoded characters to a new list
        encoded_list.append(encode_character(phrase_list[i],strng_list[i]))
    return ''.join(encoded_list)

#  Input: strng is a string of characters and pass is a pass phrase
#  Output: function returns a single string that is decoded with
#          vignere algorithm
def vigenere_decode ( strng, phrase ):
    #initializes values
    i = 0
    phrase_list = []
    strng_list = []
    decoded_list = []
    repeat = 0
    remainder = 0
    strng = filter_string(strng)#removes non lowercase letters
    phrase_list = list(phrase)#turns string into list of separate characters
    strng_list = list(strng)#turns string into list of separate characters
    repeat = len(strng) // len(phrase)#this finds how many times the full pass phrase appears in the encoded text
    phrase_list = phrase_list * repeat#replicates the list for the amount of times it fully appears in the encoded text
    remainder = len(strng) % len(phrase)#finds the amount of remaining letters
    while i < remainder:#this while loop appends the list with the remaining letters
        phrase_list.append(phrase_list[i])
        i += 1
    for i in range(len(strng)):#adds decoded characters to new list
        decoded_list.append(decode_character(phrase_list[i],strng_list[i]))
    return ''.join(decoded_list)

def main(): 
  print('Rail Fence Cipher\n')
  
  plain_text_RF = input('Enter Plain Text to be Encoded: ')#prompt the user to enter plain text
  encrypt_key_RF = int(input('Enter Key: '))#prompt user for key
  print('Encoded Text:',rail_fence_encode(plain_text_RF,encrypt_key_RF),'\n')#returns the encoded text

  encoded_text_RF = input('Enter Encoded Text to be Decoded: ')#prompt user to enter encoded text
  decrypt_key_RF = int(input('Enter Key: '))#prompt user for key
  print('Decoded Plain Text:',rail_fence_decode(encoded_text_RF,decrypt_key_RF))#returns decoded plain text
  print()
  print('Vigenere Cipher\n')

  plain_text_vig = input('Enter Plain Text to be Encoded: ')#prompt user for plain text
  pass_phrase = input('Enter Pass Phrase (no spaces allowed): ')#prompt user for pass phrase
  print('Encoded Text:',vigenere_encode(plain_text_vig,pass_phrase))#returns the encoded text
  print()
  encoded_text_vig = input('Enter Encoded Text to be Decoded: ')#prompt user for encoded text
  pass_phrase = input('Enter Pass Phrase (no spaces allowed): ')#prompt for pass phrase
  print('Decoded Plain Text:', vigenere_decode(encoded_text_vig, pass_phrase))#return the plain text decoded


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
