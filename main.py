import os
import tkinter as tk
from tkinter import filedialog

# list of commands
commandList = ["a", "rem", "remw", "rep", "repw", "rev", "nl", "d", "swnl", "swpl", "remws", "rnl", "wtcl"]

# function if user has problem with some command
def command_meaning():
    command = input("Enter the command that you don't understand, or type next if you understand all commands: ")

    if command not in commandList:
        return "Invalid command"
    else:
        with open("commandMeaning.txt", "r") as commandMeaningFile:
            lines = commandMeaningFile.readlines()
            index = (commandList.index(command) * 2) + 1
            meaning_line = lines[index].strip()
            return print(meaning_line)

# function to take file from user using tkinter dialog
def taking_file_from_user():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.deiconify()  # Show the Tkinter window briefly (necessary for some environments)

    # Open file dialog
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

    root.quit()  # Properly close the Tkinter window
    return file_path

# verification if the file exists
def verification_of_existence(file):
    if not os.path.exists(file):
        print("Your file does not exist")
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

# prompting the user to enter a name of created file where he wants to put output
def get_output_file():
    nameOfThecreatedFile = input("What will be the name of the file, where you will write the output(don't forget to write suffix .txt): ")
    return nameOfThecreatedFile

# prompting the user to enter a text document where he wants to put output
def f2():
    outputFile = input("If you want to put output to an existing file, type 'select', but if you want to put output in a file that doesn't exist, type 'create': ")
    return outputFile


# Main interaction with the user
def main():
    # Prompt for text file 1 and verify
    textFile = taking_file_from_user()

    while not verification_suffix(textFile):
        textFile = taking_file_from_user()

    while not verification_of_existence(textFile):
        textFile = taking_file_from_user()

    # reading commands from the file
    with open(textFile, "r", encoding="utf-8") as commandsR:
        commands = commandsR.read()
        commandsR.close()

    # prompt for output file
    outputFile = f2()

    if outputFile == "select":
        # Get the file path chosen by the user
        selected_file = taking_file_from_user()
        if selected_file:  # Ensure a file was selected
            print(f"You selected the file: {selected_file}")  # Display the selected file path
        else:
            print("No file selected.")

    elif outputFile == "create":
        nameOfThecreatedFile = get_output_file()
        placeOfTheOutputFile = input(
            "If you will press 'x' your output file will be created on desktop. If you want to put your output file somewhere else, type the absolute path: ")

        # Získání uživatelského jména pro Windows
        user_name = os.getlogin()

        # Určení cesty k ploše na Windows
        desktop_path = f"C:\\Users\\{user_name}\\Desktop\\{nameOfThecreatedFile}"
        print(f"Output will be saved to: {desktop_path}")

    else:
        while outputFile not in ["select", "create"]:
            print("Make sure you write everything right. ")


# Start the program
if __name__ == "__main__":
    main()
# pridat overeni na output file + vytvorit soubor pri select + vytvorit soubor pri create