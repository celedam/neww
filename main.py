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


# function to take file 1 from the user using tkinter dialog
def taking_file_from_user():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.deiconify()  # Show the Tkinter window briefly (necessary for some environments)

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select a file", filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

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
def get_output_file_name():
    nameOfThecreatedFile = input(
        "What will be the name of the file, where you will write the output (don't forget to write suffix .txt): ")
    return nameOfThecreatedFile


# prompting the user to enter a text document where he wants to put output
def f2():
    outputFile = input(
        "If you want to put output to an existing file, type 'select', but if you want to put output in a file that doesn't exist, type 'create': ")
    return outputFile


# Function for selecting or creating an output file and returning the same variable
def get_output_file():
    output_choice = f2()

    if output_choice == "create":
        return create_output_file()

    elif output_choice == "select":
        return path_of_output_file()

    else:
        print("Invalid choice. Try again.")
        return get_output_file()


# function to get path of output file
def path_of_output_file():
    print("If file explorer didn't open, you may have to check 'tk' from the taskbar.")
    selected_file = taking_file_from_user()

    while not verification_suffix(selected_file):
        print("Invalid file type. Please select a valid `.txt` file.")
        selected_file = taking_file_from_user()

    if not os.path.exists(selected_file):
        with open(selected_file, 'w') as file:
            file.write("")  # Create the file
        print(f"Created new file at: {selected_file}")
    else:
        print(f"Selected file exists at: {selected_file}")

    return selected_file


# function to create output file
def create_output_file():
    nameOfThecreatedFile = get_output_file_name()

    while not verification_suffix(nameOfThecreatedFile):
        print("Invalid file name. Ensure it ends with '.txt'.")
        nameOfThecreatedFile = get_output_file_name()

    save_path = input("Press Enter to save on the Desktop, or type an absolute path to save somewhere else: ")

    if not save_path.strip():  # Save to Desktop if nothing is specified
        user_name = os.environ.get("USERNAME")
        desktop_path = os.path.join(
            os.path.expanduser("~/OneDrive/Plocha"), nameOfThecreatedFile
        )

        save_path = desktop_path

    if not os.path.exists(save_path):
        with open(save_path, 'w') as file:
            file.write("")  # Create the file
        print(f"File created at: {save_path}")
    else:
        print(f"File already exists at: {save_path}")

    return save_path


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
    outputFilePath = get_output_file()

    print(f"Using output file at: {outputFilePath}")


# Start the program
if __name__ == "__main__":
    main()

# krok 1 vytvor funkce s prikazy
# krok 2 vytvorit soubor pri select + vytvorit soubor pri create