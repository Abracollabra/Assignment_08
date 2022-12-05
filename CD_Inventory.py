#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Deborah C, 2022-Dec-01, Began modifying code to complete Assignment 08
# Deborah C, 2022-Dec-02, Continued modifications - Added functions and classes
# Deborah C, 2022-Dec-03, Continued modifications - Added error handling & docstrings
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    Properties:
        cd_id: (int) The ID number of the CD
        cd_title: (string) The title of the CD
        cd_artist: (string) The artist of the CD
        
    Methods:
        __init__

    """
    # TODONE Add Code to the CD class
    def __init__(self, id, title, artist):
        """
        Constructs objects of the CD class
        
        Parameters:
            id (int)
            title (str)
            artist (str)
            
       Returns:
           None.
        
        """
        self.cd_id = id
        self.cd_title = title
        self.cd_artist = artist

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from a text file:

    Properties:  
        None

    Methods:
        load_inventory(file_name): A list of CD objects
        save_inventory(file_name, lst_Inventory): Saves data to a file           

    """
    # TODONE Add code to process data from a file
    
    @staticmethod
    def load_inventory(file_name):
        """
        Reads data from a text file.
        
        Parameters:
            file_name (str) Name of the data file
            
        Returns:
            None.
        
        """
        objFile = open(file_name, 'r')
        for row in objFile:
            lstRowData = row.strip().split(',')
            objCD = CD(lstRowData[0], lstRowData[1], lstRowData[2])
            lstOfCDObjects.append(objCD)
        objFile.close()
            
    # TODO Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_inventory):
        """
        Saves data to a text file.
        
        Parameters:
            file_name: (str) Name of the data file
            lst_inventory: List containing cd_id, cd_title, cd_artist
            
        Returns:
            None.
        
        """
        file_data = ''
        for cd in lst_inventory:
            file_data = file_data + f'{cd.cd_id}, {cd.cd_title}, {cd.cd_artist}\n'
        objFile = open(file_name, 'w') 
        objFile.write(file_data) 
        objFile.close()

    
# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODONE add docstring
    """Displays inforamtion to the user and gets input from the user.
    
    Properties: 
        None
        
    Methods:
        print_menu(): Prints the menu of options for the user
        get_user_input(): (string) Gets input from the the user
        display_current_inventory(lstOfCDs): Displays a 2D list of lists from local memory
        add_cd(lstOfCDs): Appends a new row to to 2D list of cds in local memory
        
    """       
    # TODO add code to show menu to user
    @staticmethod
    def print_menu():
        """
        Prints the menu of options ofr the user.
   
        Parameters:
            None

        Returns:
           None.

        """
        print('\nMenu of Options\n\n[ l ]  Load CD Inventory from File\n[ a ]  Add CD\n[ i ]  dIsplay Current Inventory')
        print('[ s ]  Save Inventory to File\n[ x ]  eXit the Program\n')   
    
    # TODO add code to captures user's choice
    @staticmethod
    def get_user_input():
        """
        Asks the user to choose an option from the menu.
        
        Parameters:
            None
            
        Returns:
            None.

        """
        return input('Choose an Option: ')
    
    # TODO add code to display the current data on screen
    @staticmethod
    def display_current_inventory(lstOfCDs):
        """
        Displays the data in local memory, the table of CDs
        
        Parameters:
            A list, known as lstOfCDs
            
        Returns:
            (str) 2D List of CDs in local memory      
        
        """
        print('\nID\tTitle\t\tArtist')
        print('____________________________\n')
        for cd in lstOfCDs:
            print(str(cd.cd_id) + '\t' + cd.cd_title + '\t' + cd.cd_artist)
    
    # TODO add code to get CD data from user
    @staticmethod
    def add_cd(lstOfCDs):
        """
        Adds a new row of data containing the three user inputs: id, title, and artist.

        Parameters:
            lstOfCDs (TYPE): DESCRIPTION

        Returns:
            None.

        """
        id = int(input('Enter ID: ').strip())
        title = input('Enter Title: ').strip()
        artist = input('Enter Artist/Band Name: ').strip()
        objCD = CD(id, title, artist)
        lstOfCDs.append(objCD)        

# -- Main Body of Script -- #
# TODONE Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName)

while True:
    # Display menu to user
    IO.print_menu()
    strUsrInput = IO.get_user_input()
    # let user add data to the inventory (local inventory)    
    if strUsrInput == 'a':
        IO.add_cd(lstOfCDObjects)
    # show user current inventory    
    elif strUsrInput == 'i':
        IO.display_current_inventory(lstOfCDObjects)
    # let user save inventory to file (to file inventory)
    elif strUsrInput == 's':
        while True:
            strYesNo = input('Save this inventory to file? [ y or n ] ').strip().lower()
            if strYesNo == 'y':
                FileIO.save_inventory(strFileName, lstOfCDObjects)
                print('\nSaved.\n')
                break
            elif strYesNo == 'n':
                input('\nThe inventory was NOT saved to file.\n\nPlease press [ENTER] to return to the menu.')
                break
            else:
                print('\nPlease type either the letter y or the letter n.\n')
                continue
        # FileIO.save_inventory(strFileName, lstOfCDObjects)
    # let user load inventory from file  (file inventory is local inventory and replaces old local inventory)
    elif strUsrInput == 'l':
        lstOfCDObjects = []
        FileIO.load_inventory(strFileName)
    # let user exit program
    elif strUsrInput == 'x':
        break