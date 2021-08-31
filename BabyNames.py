#  File: BabyNames.py 

#  Description:  This program displays the 1000 most popular baby names
#                per decade for the past 11 decades.

#  Student Name:  Emily Zhou

#  Student UT EID:  ejz274

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 2/7/20

# Date Last Modified: 2/10/20

class BabyNames(object):
        """Class to store all the baby names"""
        # Initializes the dictionary that will hold all the baby names
        def __init__(self):
                # key: name
                # value: list of ranks
                self.names = {}
                
        # Reads in the file and adds to the dictionary
        def fill_data(self, file_name):
                #create empty string
                value_list = []
                #open file for reading
                infile = open('names.txt','r')
                for line in infile:
                        line = line.rstrip().split()
                        value_list = line[1:]
                        #Converts the rank #0 to rank #1001
                        for index in range(11):
                                if int(value_list[index]) == 0:
                                        value_list[index] = 1001
                                else:
                                        value_list[index] = int(value_list[index])
                        #add record to dictionary
                        self.names[line[0]] = value_list
                infile.close()
                
        # True if a name exists in the dictionary and False otherwise.
        def contains_name (self, name):
                return name in self.names            
        
        # Returns all the rankings for a given name. Assume the name exists
        def find_ranking(self, name):
                #replace all occurrences or rank #1001 with rank #0
                for index, rank in enumerate(self.names[name]):
                        if rank == 1001:
                             self.names[name][index] = 0                   
                return self.names[name]
                

        # Returns a list of names that have a rank in all the decades in sorted order by name.
        def ranks_of_all_decades(self):
                #create empty list
                names_only = []
                #iterate through names to find which names have a rank within the top 1000 for all decades
                for name, rank_list in self.names.items():
                        if all(rank < 1001 for rank in rank_list):
                                names_only.append(name)
                #sort names alphabetically
                names_only.sort()
                return names_only
               
        # Returns a list of all the names that have a rank in a given decade in order of rank.
        def ranks_of_a_decade(self, decade):
                #create lists
                decade_list = [1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]
                name_rank = []
                name_rank_list = []
                ordered_names = []
                decade_index = decade_list.index(decade)
                #iterate through names to find which name ranks within top 1000 in given decade
                for name , rank_list in self.names.items():
                        if rank_list[decade_index] != 1001:
                                name_rank = [rank_list[decade_index],name]
                                name_rank_list.append(name_rank)
                name_rank_list.sort()
                #selects only the names to return
                for rank in name_rank_list:
                        ordered_names.append(rank[1])
                return ordered_names

        # Return all names that are getting more popular in every decade. The list must be sorted by name.
        def getting_popular(self):
                #create empty list
                names_popular = []
                #iterate through dictionary values to see if all elements in the list values are strictly increasing
                for name, rank_list in self.names.items():
                        if all(rank1 > rank2 for rank1,rank2 in zip(rank_list,rank_list[1:])):
                                names_popular.append(name)
                #sort popular names alphabetically
                names_popular.sort()
                return names_popular

        # Return all names that are getting less popular in every decade. The list must be sorted by name.
        def less_popular(self):
                #create empty list
                names_lesspop = []
                #iterate through dictionary values to see if all elements in the list values are strictly decreasing
                for name, rank_list in self.names.items():
                        if all(rank1 < rank2 for rank1,rank2 in zip(rank_list,rank_list[1:])):
                                names_lesspop.append(name)
                #sort less popular names in alphabetically
                names_lesspop.sort()
                return names_lesspop
                

#prints the menu options
def display_menu():
        print()
        print('Options:')
        print('Enter 1 to search for names.')
        print('Enter 2 to display data for one name.')
        print('Enter 3 to display all names that appear in only one decade.')
        print('Enter 4 to display all names that appear in all decades.')
        print('Enter 5 to display all names that are more popular in every decade.')
        print('Enter 6 to display all names that are less popular in every decade.')
        print('Enter 7 to quit.\n')
        
def main():
        #Initilize variables and create list
        loop_again = 'Yes'
        user_choice = ''
        user_name = ''
        user_decade = 0
        rank_list = ''
        rank_list_zero = []
        highest_rank_list =[]
        with_no_zero = []
        decade_list = [1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]

        #instantiate baby name object 
        names_object = BabyNames()
        names_object.fill_data('names.txt')

        #loop to display menu options and process user input
        while loop_again != '7':
                display_menu()
                #get user choice
                user_choice = input('Enter choice: ')
                
                #Searches for baby name in dictionary
                if user_choice == '1':
                        #get baby name from user
                        user_name = input('Enter a name: ')
                        #if name exists, continue to find highest ranking decade
                        if names_object.contains_name(user_name):
                                rank_list = names_object.find_ranking(user_name)
                                #Finds which decade had the highest rank for given name
                                if 0 not in rank_list:
                                        highest_rank_index = rank_list.index(min(rank_list))
                                else:
                                        with_no_zero = [rank for rank in rank_list if rank != 0]
                                        highest_rank_index = rank_list.index(min(with_no_zero))
                                #print the highest ranking decade
                                print('\nThe matches with their highest ranking decade are:')
                                print(user_name,decade_list[highest_rank_index])
                        #Error message if name does not exist
                        else:
                                print()
                                print(user_name,'does not appear in any decade.')

                #display all data for given name if choose option 2
                elif user_choice =='2':
                        #get baby name from user
                        user_name = input('Enter a name: ')
                        #Print ranks per decade from returned list if given name exists
                        if names_object.contains_name(user_name):
                                rank_list = names_object.find_ranking(user_name)
                                rank_list_zero = [str(rank) for rank in rank_list]
                                print()
                                print(user_name+': '+' '.join(rank_list_zero))
                                for index in range(11):
                                        print(str(decade_list[index])+':'+' '+ rank_list_zero[index])
                        #Error message if given name does not exist
                        else:
                            print()
                            print(user_name,'does not appear in any decade.')

                #display all names that appear in a particular decade
                elif user_choice == '3':
                        #get decade from user
                        user_decade = int(input('Enter decade: '))
                        print('The names are in order or rank:')
                        #print names in returned list that has names ordered by rank in given decade
                        for name in names_object.ranks_of_a_decade(user_decade):
                                print(name,end=': ')
                                print(names_object.find_ranking(name)[decade_list.index(user_decade)])
                                
                #display names in all decades
                elif user_choice == '4':
                        print(len(names_object.ranks_of_all_decades()),'names appear in every decade. The names are:')
                        #print names from returned list of all names that appear in all decades
                        for name in names_object.ranks_of_all_decades():
                                print(name)
                                
                #display all names that are more popular in every decade
                elif user_choice == '5':
                        print('2 names are more popular in every decade.')
                        #print names from returned list of increasingly popular names
                        for name in names_object.getting_popular():
                                print(name)

                #display all names that are less popular in every decade
                elif user_choice == '6':
                        print(len(names_object.less_popular()),'names are less popular in every decade.')
                        #print names from returned list of decreasingly popular names 
                        for name in names_object.less_popular():
                                print(name)

                #quit loop
                else:
                        loop_again = '7'

        #Exit message
        print()
        print()
        print('Goodbye.')



if __name__ == '__main__':
        main()
