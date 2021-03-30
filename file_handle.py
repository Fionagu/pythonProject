''' open() function

'r' - Read - Default value, opens a file for reading, error if the files does not exists
'a' - Append - opens file for appending, creates the file if not exists
'w' - Write - opens file for writing, creates the file if not exists
'x' - Create - create the specified file, return an error if not exists

't' - Text
'b' - Binary

'''


# delete files
import os
os.remove('demofile.txt')