# Made by Sam Brashaw

def writeDatabase( file, recordList ):
    towrite = []
    for record in recordList:
        towrite.append( ",".join(record) )
        towrite.append( "\n" )
    with open( file, "w" ) as f:
        f.writelines( towrite )

# Will read the database file and
def readDatabase( file ):
    recordList = []
    with open( file, "r" ) as f:
        for record in f.readlines():
            recordList.append( record.replace( "\n", "" ).split( "," ) )
    return recordList
