#This program will write to a file

#sets the file name to open/create
fileName = "WriteToFile.csv"

#'w' for write 'r' for read 'a' for append
WRITE = "w+"
READ = "r"
#WRITE is the value for access mode
myFile = open(fileName, WRITE)

#writes to the file, not that it will not put things onto a new line on its own
myFile.write("This, is, a, fake, way, to, CSV\n")
myFile.write("Make, sure, the, columns, line, up, properly\n")
myFile.write("Addning, one, more, line, to, fill, space")
print("File has been written to.")

#make sure to close the file after completing the task
myFile.close
print("File has been closed.")

#going to open and read the file now
myFile = open(fileName, READ)

#this loads the whole file into a single string
oneBigString = myFile.read()
print(oneBigString)

myFile.close
print("Closed the file.")