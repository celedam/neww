import os
import tkinter as tk
from tkinter import filedialog

# list of commands
commandList = ["a", "rem", "remw", "rep", "repw", "rev", "nl", "d", "swnl", "swpl", "remws", "rnl", "wtcl"]

# function if user has problem with some command
def command_meaning():
    command = input("Enter the command that you dont understand, or type next if you understand all commands: ")

    if command not in commandList:
        return "Invalid command"

    else:
        with open ("commandMeaning.txt", "r") as commandMeaningFile:
            lines = commandMeaningFile.readlines()
            index = (commandList.index(command) * 2) + 1
            meaning_line = lines[index].strip()
            return print(meaning_line)

# function to take file 1 from the user
def f1():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a file",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    return file_path

# verification if the file exists
def verification_of_existence(file):
    if not os.path.exists(file):
        print ("Your file does not exist")
        return False

    else:
        return True

# verification if the file is .txt
def verification_suffix(file):
    if file.endswith(".txt"):  # verification if the file ends with ".txt"
        return True
    else:
        print("Your file does not have suffix .txt.")
        return False

# Main interaction with the user
def main():
    # Prompt for text file 1 and verify
    textFile = f1()
    while not verification_suffix(textFile):
        textFile = f1()
    while not verification_of_existence(textFile):
        textFile = f1()

    # reading commands from the file
    with open(textFile, "r", encoding="utf-8") as commandsR:
        commands = commandsR.read()
        commandsR.close()

# prompting the user to enter a text document where he wants to put outcome
def f2():
    f2 = input("Enter a name of file (with .txt extension) where u want to write changed file 1 (if your file doesn't exist write 'x'): ")

# Start the program
if __name__ == "__main__":
    main()


