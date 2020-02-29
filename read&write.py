'''
Created on Feb 29, 2020

@author: ITAUser
'''
#open file - open()

file1 = "fileName.text", "mode"

#mode r: read, w: write, a: append r+: special case read & write

#read - read(), readLine() - stores value as a string
#write - write()

#Create a new file
    file1 = open("hello.txt", "a")
    file1.close()
    
#write to the file
    string= "hello my name is Chokyi"
    file1.writeLines(line)
    file1.close()
    
#write multiple lines
    line = ["dogs", "are", "cool"]
    file1.writeline(line)
    file1.close()
    
#read file
    file1.open("hello.txt", "r")
    text = file1.close()
    
    print(text)
    