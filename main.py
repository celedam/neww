import argparse
import os
import re
import sys


# Function to open the command meaning file if it exists
def command_meaning():
    if os.path.exists("commandMeaning.txt"):
        os.startfile("commandMeaning.txt")
    else:
        print("Error: commandMeaning.txt was not found.")
        sys.exit(1)


# Function to verify if a file exists
def verify_files(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        exit(1)

    if not file_path.endswith('.txt'):
        print(f"Error: File '{file_path}' does not have the correct '.txt' extension.")
        exit(1)


# Function to parse arguments
def arguments():
    parser = argparse.ArgumentParser(description="Process input commands on text.")
    parser.add_argument("-hCom", "--helpCommands", action="store_true",
                        help="Open a file with commands list and their meanings.")
    parser.add_argument("-f1", "--inputText", type=str, required=True,
                        help="Enter the path to the input text file.")
    parser.add_argument("-f2", "--inputCommands", type=str, required=True,
                        help="Enter the path to the commands text file.")
    parser.add_argument("-toFile", "--outputText", type=str, required=True,
                        help="Enter the path to the output text file.")

    args = parser.parse_args()

    # If user wants to open the help file
    if args.helpCommands:
        command_meaning()

    # Log parsed arguments for debugging
    print("Arguments values:")
    print(f"- Input Text: {args.inputText}")
    print(f"- Input Commands: {args.inputCommands}")
    print(f"- To File: {args.outputText}")

    # verify suffix and existence of files
    filesToVerify = [args.inputCommands, args.outputText, args.inputText]

    for file in filesToVerify:
        verify_files(file)

    return args


# Function to read all commands from the commands file
def reading_commands(args):
    with open(args.inputCommands, "r", encoding="utf-8") as file:
        commands = [command.strip() for command in file.readlines()]
    return commands


# Function to load input text into memory
def read_file_to_memory(args):
    with open(args.inputText, "r", encoding="utf-8") as file:
        content = file.readlines()
    return content


# Process 'addToEnd' command
def process_add_to_end(content, command_line, lineIndex):
    match = re.search(r'addToEnd\s+"(.+)"', command_line)
    if match:
        string_to_add = match.group(1)  # Extract the string properly
        content[lineIndex] += string_to_add  # Ensure no reversed logic interferes
    return content


# Process 'remove' command
def process_remove(content, command_line, lineIndex):
    match = re.search(r'remove\s+(\d+)\s+(\d+)', command_line)
    if match:
        try:
            start_index = int(match.group(1))
            num_to_remove = int(match.group(2))

            line = content[lineIndex]

            # Ensure indexes are valid
            if start_index >= 0 and start_index + num_to_remove <= len(line):
                content[lineIndex] = line[:start_index] + line[start_index + num_to_remove:]
        except ValueError:
            pass  # Ignore invalid input commands
    return content


# process 'removeWord' command
def process_remove_word(content, command_line, lineIndex):
    # Ladicí výstup pro ověření, že funkce je volána
    print(f"Processing command: {command_line}")  # Tento výstup nám ukáže, zda je příkaz vůbec předán

    match = re.search(r'removeWord\s+"(.+)"', command_line)
    if match:
        line = content[lineIndex]
        wordToRemove = match.group(1)  # Extrahujeme slovo k odstranění

        # Ladicí výstup pro ověření, že jsme správně extrahovali slovo
        print(
            f"Removing word: '{wordToRemove}' from line: '{line}'")  # Tento výstup zkontroluje, zda máme správné slovo

        # Použijeme re.escape pro bezpečné odstranění slova
        pattern = r'\b{}\b'.format(re.escape(wordToRemove))

        # Odstraníme všechna výskyt slova
        new_line = re.sub(pattern, '', line)

        # Ladicí výstup pro ověření odstranění
        print(f"After removal: '{new_line}'")  # Tento výstup ukáže, jak vypadá řádek po odstranění slova

        # Odstraníme více mezer a zbavíme se nadbytečných mezer
        content[lineIndex] = re.sub(r'\s+', ' ', new_line).strip()

        # Ladicí výstup pro finální řádek
        print(f"Final line after cleaning spaces: '{content[lineIndex]}'")  # Tento výstup ukáže finální upravený řádek

    return content


# process 'replace' command
def process_replace(content, command_line, lineIndex):
    match = re.search(r'replace\s+(\d+)\s+"(.+)"', command_line)  # Pro hledání číselného indexu a náhrady
    if match:
        index = int(match.group(1))  # Získání čísla indexu pro náhradu
        replacement = match.group(2)  # Slovo pro náhradu
        line = content[lineIndex]

        print(f"Replacing word at index {index} with '{replacement}' in line: {line}")

        words = line.split()  # Rozdělení na slova podle mezer
        if 0 <= index < len(words):
            words[index] = replacement  # Náhrada slova na konkrétním indexu
            content[lineIndex] = ' '.join(words)  # Spojení zpět do řádku

        print(f"After replacement: {content[lineIndex]}")  # Ladění pro zobrazení výsledku

    return content



# process 'replaceWord' command
def process_replace_word(content, command_line, lineIndex):
    # Regex pro hledání příkazu pro náhradu slova
    match = re.search(r'replaceWord\s+"(.+)"\s+"(.+)"', command_line)
    if match:
        word = match.group(1)
        replacement = match.group(2)
        line = content[lineIndex]

        print(f"Word to replace: '{word}' with '{replacement}'")
        print(f"Before replacement: {line}")

        # Používáme regulární výraz pro náhradu celého slova
        pattern = r'\b{}\b'.format(re.escape(word))  # Tento regex zajistí náhradu pouze celého slova
        content[lineIndex] = re.sub(pattern, replacement, line)

        print(f"After replacement: {content[lineIndex]}")  # Ladění pro zobrazení výsledku

    return content


# process 'reverse'
def process_reverse(content, command_line, lineIndex):
    match = re.search(r'reverse\s+(\d+)', command_line)
    if match:
        try:
            word_index = int(match.group(1))

            line = content[lineIndex]
            words = line.split()

            if 0 <= word_index < len(words):
                words[word_index] = words[word_index][::-1]

                content[lineIndex] = ' '.join(words)

        except ValueError:
            pass
    return content


# processing 'newLine' command
def process_add_new_line(content, command_line, lineIndex):
    match = re.search(r'addNewLine', command_line)  # Match the command with an index
    if match:
        try:
            content.insert(lineIndex + 1, '')  # Add a blank line after the specified index
        except ValueError:
            pass  # Ignore the command if parsing fails
    return content


# processing 'duplicate' command
def process_duplicate(content, command_line, lineIndex):
    match = re.search(r'duplicate\s+"(.+)"', command_line)  # Match the command and extract the string to duplicate
    if match:
        word_to_duplicate = match.group(1)
        line = content[lineIndex]
        # Replace all occurrences of the word with its duplicate
        content[lineIndex] = re.sub(r'\b' + re.escape(word_to_duplicate) + r'\b', word_to_duplicate + word_to_duplicate, line)
    return content


# processing 'swapWithNextLine' command
def process_swap_with_next_line(content, command_line, lineIndex):
    match = re.search(r'swapWithNextLine', command_line)  # Match the command and extract index
    if match:
        # Ensure the index is valid
        if 0 <= lineIndex < len(content) - 1:
            # Swap the content of the line at line_index and line_index + 1
            content[lineIndex], content[lineIndex + 1] = content[lineIndex + 1], content[lineIndex]
    return content


# processing 'swapWithPreviousLine' command
def process_swap_with_previous_line(content, command_line, lineIndex):
    match = re.search(r'swapWithPreviousLine', command_line)
    if match:
        # Ensure the index is valid
        if 1 <= lineIndex < len(content):
            # Swap the content of the line at line_index and line_index - 1
            content[lineIndex], content[lineIndex - 1] = content[lineIndex - 1], content[lineIndex]
    return content


# processing 'removeWhiteSpaces' command
def process_remove_white_spaces(content, command_line,lineIndex):
    if "removeWhiteSpaces" in command_line:
        # Replace multiple spaces or tabs with a single space (anywhere in the content)
        content[lineIndex] = re.sub(r'\s+', ' ', content[lineIndex]).strip()
    return content


# processing 'writeToConsole' command
def process_write_to_console(content, command_line, lineIndex):
    match = re.search(r'writeToConsole', command_line)
    if match:
        # Ensure index is in bounds
        if 0 <= lineIndex < len(content):
            line = content[lineIndex]
            print(line)
    return content

# Process all commands in memory sequentially
def process_commands_in_memory(content, commands):
    lineIndex = 0

    for line in commands:
        print(f"Processing command: {line}")  # Zobrazení příkazu, který se právě zpracovává

        if line.startswith("removeWord"):
            print(f"Found removeWord command: {line}")  # Zobrazení, pokud je nalezen příkaz 'removeWord'
            content = process_remove_word(content, line, lineIndex)
        elif line.startswith("addToEnd"):
            print(f"Found addToEnd command: {line}")  # Zobrazení, pokud je nalezen příkaz 'addToEnd'
            content = process_add_to_end(content, line, lineIndex)
        elif line.startswith("remove"):
            print(f"Found remove command: {line}")  # Zobrazení, pokud je nalezen příkaz 'remove'
            content = process_remove(content, line, lineIndex)
        elif line.startswith("reverse"):
            print(f"Found reverse command: {line}")  # Zobrazení, pokud je nalezen příkaz 'reverse'
            content = process_reverse(content, line, lineIndex)
        elif line.startswith("newLine"):
            print(f"Found newLine command: {line}")  # Zobrazení, pokud je nalezen příkaz 'newLine'
            lineIndex += 1
        elif line.startswith("duplicate"):
            print(f"Found duplicate command: {line}")  # Zobrazení, pokud je nalezen příkaz 'duplicate'
            content = process_duplicate(content, line, lineIndex)
        elif line.startswith("swapWithNextLine"):
            print(f"Found swapWithNextLine command: {line}")  # Zobrazení, pokud je nalezen příkaz 'swapWithNextLine'
            content = process_swap_with_next_line(content, line, lineIndex)
        elif line.startswith("swapWithPreviousLine"):
            print(f"Found swapWithPreviousLine command: {line}")  # Zobrazení, pokud je nalezen příkaz 'swapWithPreviousLine'
            content = process_swap_with_previous_line(content, line, lineIndex)
        elif line.startswith("removeWhiteSpaces"):
            print(f"Found removeWhiteSpaces command: {line}")  # Zobrazení, pokud je nalezen příkaz 'removeWhiteSpaces'
            content = process_remove_white_spaces(content, line, lineIndex)
        elif line.startswith("addNewLine"):
            print(f"Found addNewLine command: {line}")  # Zobrazení, pokud je nalezen příkaz 'addNextLine'
            content = process_add_new_line(content, line, lineIndex)
        elif line.startswith("writeToConsoleLine"):
            print(f"Found writeToConsoleLine command: {line}")  # Zobrazení, pokud je nalezen příkaz 'writeToConsoleLine'
            content = process_write_to_console(content, line, lineIndex)
        elif line.startswith("replaceWord"):
            print(f"Found replaceWord command: {line}")  # Zobrazení, pokud je nalezen příkaz 'writeToConsoleLine'
            content = process_replace_word(content, line, lineIndex)
        elif line.startswith("replace"):
            print(f"Found replace command: {line}")  # Zobrazení, pokud je nalezen příkaz 'writeToConsoleLine'
            content = process_replace(content, line, lineIndex)
        else:
            print(f"Unknown command: {line}")  # Zobrazení neznámého příkazu, pokud neodpovídá žádnému z výše uvedených

    return content



# Write the processed content back to an output file
def write_output_to_file(args, content):
    with open(args.outputText, "w", encoding="utf-8") as file:
        content = [item.replace('\n', '') for item in content]
        output = '\n'.join(content)
        file.write(output)



# Main function to handle the program's execution flow
def main():
    args = arguments()  # Parse and handle arguments

    commands = reading_commands(args)  # Read all commands
    content = read_file_to_memory(args)  # Load initial text into memory
    content = process_commands_in_memory(content, commands)  # Process commands sequentially
    write_output_to_file(args, content)  # Write the processed text back to a file

    print("Processing complete.")


# Entry point of the script
if __name__ == "__main__":
    main()
