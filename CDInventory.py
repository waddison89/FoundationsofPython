#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Wes Addison, 20210114, Add 2D dictionary and other functions)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# Declare variables
strChoice = '' # User input

lstTbl = []
lstRow = []
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Does load = write???
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) +','
            strRow = strRow[:1] + '\n'
            objFile.write(strRow)
        objFile.close()
        pass
    
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter and ID: ')
        strTitle = input('Enter a Title: ')
        strArtist = input('Enter the Artist: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        for row in lstTbl:
            print('Current CD:', *row.values(),sep ='|')
            print()
            
    elif strChoice == 'd':
        print('ID\tCD Title (by: Artist)\n')
        for row in lstTbl:
            print('{}\t{} by {}'.format(*row.values()))
        print()
        intIDDEL = int(input('Which ID would you like to delete').strip())
        foundIt = False
        rowNr = -1
        for row in lstTbl:
            rowNr += 1
            if row['ID'] == intIDDEL:
                del lstTbl[rowNr]
                foundIt = True
                break
        if foundIt:
            print('deleted entry\n')
        else:
            print('Could not find this entry')
        pass             
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a+')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x!')

