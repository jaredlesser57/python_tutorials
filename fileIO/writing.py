with open("scratchpad.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")


""" 
File Modes:

'r' - open for reading (default)
'w' - open for writing, truncating the file first
'x' - open for exclusive creation, failing if the file already exists
'a' - open for writing, appending to the end of the file if it exists
'b' - binary mode
't' - text mode (default)
'+' - open a disk file for updating (reading and writing)
'U' - universal newlines mode (deprecated)
"""