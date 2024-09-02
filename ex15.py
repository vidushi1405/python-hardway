#EXERCISE 15
#using argv to find the filename
from sys import argv
script,filename = argv
#using command OPEN which opens a file and returns it as a file obj.
txt=open(filename)

print(f"here is our file{filename}")
#calling a function on txt named read.
print(txt.read())

print("type the file name again:")
file_again=input(">")
txt_again= open(file_again)
# "." is used to give command to a file.
print(txt_again.read())
