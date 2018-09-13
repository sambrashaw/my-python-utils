# Made by Sam Brashaw

# Will write to the database file making sure to format it so it can be read again.
def writeDatabase( file, recordList ):
    towrite = []
    for record in recordList:
        towrite.append( ",".join(record) )
        towrite.append( "\n" )
    with open( file, "w" ) as f:
        f.writelines( towrite )

# Will read the database file and convert it to a python list.
def readDatabase( file ):
    recordList = []
    with open( file, "r" ) as f:
        for record in f.readlines():
            recordList.append( record.replace( "\n", "" ).split( "," ) )
    return recordList

# Clears the console to make
def cls():
    from os import system
    system("cls")

# Sets up the general UI for the console and adds an input field to take user input.
def firstOptionInput():
    print("\n" + "*"*50)
    print("\n[A] ")
    print("\n[B] ")
    print("\n[C] ")
    print("\n[D] ")
    print("\n" + "*"*50 + "\n")
    optioninput = input(">> ")
