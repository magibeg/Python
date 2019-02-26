#Will import the CSV library and manipulate some values

import csv

fileName = "GuestList.txt"

accessMode = "r"

#open the file as myCSVFile
with open(fileName, accessMode) as myCSVFile:

    #Read the file contents
    dataFromFile = csv.reader(myCSVFile)

    for currentRow in dataFromFile:
        print(','.join(currentRow))
        for currentWord in currentRow:
           print(currentWord)