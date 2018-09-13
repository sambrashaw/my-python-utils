# my-python-utils
Python utilities for reading, writing and formatting data into files


# The writeDatabase() function
The writeDatabase() function constructs the database.txt file for long term data storage instead of stopring the information as variables. This allows for cross session saving of information. It simply takes a file to dump the database to and a list of lists containing the records for the database. It will then format them by seperating each of the values in the records using commas. It will also seperate each record on to a line so that the readDatabase() function can work properly.

The format:
```Value1,Value2,Value3,Value4,Value5
   Value1,Value2,Value3,Value4,Value5 ```
