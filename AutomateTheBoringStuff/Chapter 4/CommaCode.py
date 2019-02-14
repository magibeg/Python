#Contains a function that takes a list and outputs CSV values

def toCommaCode(theList):
    for i in theList:
        print(i)
    return "{}, and {}".format(", ".join(theList[:-1]), theList[-1])


spam = ["apples", "bananas", "tofu", "cats"]
newList = toCommaCode(spam)
print(newList)