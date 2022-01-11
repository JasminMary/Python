def vowelCounter(name):
    vowelCount = 0
    for x in name:
        if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            vowelCount = vowelCount + 1
    return vowelCount


def calculateCompatibility(fname, oname):
    name1l = len(fname)
    name2l = len(oname)
    name1v = vowelCounter(fname)
    name2v = vowelCounter(oname)
    percentage = name1l*name2l + name1v*name2v
    if(percentage > 100):
        percentage = 99
    return percentage


def getCompatibility(firstname, othername):
    if firstname.isnumeric() or othername.isnumeric():
        return print("Invalid input")
    else:
        return print("Compatibility is " + str(calculateCompatibility(firstname, othername)) + "%")


name1 = (input("Please enter your name:"))
name2 = (input("Please enter other name:"))
getCompatibility(name1, name2)