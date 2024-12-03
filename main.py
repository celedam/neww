import os
#list of commands
commandList = ["a", "rem", "remw", "rep", "repw", "rev", "nl", "d", "swnl", "swpl", "remws", "rnl", "wtcl"]
command = input("Enter the command that you dont understand, or type next if you understand all commands: ")

# function for helping with commands
def commandMeaning(InputCommand):
    with open ("commandMeaning.txt", "r") as commandMeaningFile:
        index = (commandList.index(InputCommand) + 1) * 2
        lines = file.readlines
        meaning = commandMeaningFile.readlines(index)
        return lines

print (commandMeaning(command))


"""
# prompting the user to enter if he wants to help with some command
command = input("Enter the command that you dont understand, or type next if you understand all commands: ")
while command.lower() in commandList:








# prompting the user to enter a text document they want to work with
def f1():
    return input("Enter a name of file (with .txt extension) from which you want to take commands: ")

# verification if the file is .txt
def verificationSuffix(file):
    if file.endswith(".txt"):  # verification if the file ends with ".txt"
        return True
    else:
        print("Your file does not have suffix .txt.")
        return False

# Calling a function and checking the filename until it is correct
textFile = f1()

while not verificationSuffix(textFile):
    textFile = f1()


# overovani jestli textovy soubor existuje
def verificationOfExistence(file):
    if not os.path.exists(file):
        print ("Your file does not exist")
        return False

    else:
        return True

# Calling a function and checking the filename until it is correct
while not verificationOfExistence(textFile):
    textFile = f1()

# reading commands from the file
with open (textFile, "r", encoding="utf-8") as commandsR:
    commands = commandsR.read()
    commandsR.close()
"""

