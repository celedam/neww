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

    return args


# Function to verify if a file exists
def verify_file_existence(file_path):
    if not os.path.exists(file_path):
        return False
    return True


# Function to verify if a file has '.txt' suffix
def verify_file_suffix(file_path):
    if not file_path.endswith(".txt"):
        return False
    return True


# Function to verify all paths in arguments
def verify_paths(args):
    verify_file_existence(args.inputText)
    verify_file_existence(args.inputCommands)
    if not verify_file_suffix(args.inputText):
        print("Error: Input text file does not have '.txt' suffix.")
        sys.exit(1)
    if not verify_file_suffix(args.inputCommands):
        print("Error: Input commands file does not have '.txt' suffix.")
        sys.exit(1)
    if args.outputText and not verify_file_suffix(args.outputText):
        print("Error: Output file does not have '.txt' suffix.")
        sys.exit(1)
    return True


# Function to read all commands from the commands file
def reading_commands(args):
    with open(args.inputCommands, "r", encoding="utf-8") as file:
        commands = [command.strip() for command in file.readlines()]
    return commands


# Function to load input text into memory
def read_file_to_memory(args):
    with open(args.inputText, "r", encoding="utf-8") as file:
        content = file.read()
    return content


# Process 'addToEnd' command
def process_add_to_end(content, command_line):
    match = re.search(r'addToEnd\s+"(.+)"', command_line)
    if match:
        string_to_add = match.group(1)
        content += string_to_add + "\n"
    return content


# Process 'remove' command
def process_remove(content, command_line):
    match = re.search(r'remove\s+(\d+)\s+(\d+)', command_line)
    if match:
        try:
            start_index = int(match.group(1))
            num_to_remove = int(match.group(2))

            # Ensure indexes are valid
            if start_index >= 0 and start_index + num_to_remove <= len(content):
                content = content[:start_index] + content[start_index + num_to_remove:]
        except ValueError:
            pass  # Ignore invalid input commands
    return content


# process 'removeWord' command
def process_remove_word(content, command_line):
    # Match the command with the word to remove
    match = re.search(r'removeWord\s+"(.+)"', command_line)
    if match:
        removedWord = match.group(1)  # Extract the word from the command
        # Remove all occurrences of the word
        content = re.sub(r'\b{}\b'.format(re.escape(removedWord)), '', content)  # Use word boundaries
        # Clean up multiple spaces if needed
        content = re.sub(r'\s+', ' ', content).strip()
    return content


# process 'replace' command
def process_replace(content, command_line):
    match = re.search(r'replace\s+(\d+)\s+"(.+)"', command_line)  # Match the replace command with index and replacement string
    if match:
        try:
            # Parse index and string to replace
            startIndex = int(match.group(1))
            replacementText = match.group(2)

            # Ensure index is within bounds
            if 0 <= startIndex < len(content):
                # Replace part of the text starting at index with replacement string
                content = content[:startIndex] + replacementText + content[startIndex + len(replacementText):]
        except ValueError:
            pass  # If there are parsing issues, ignore the command
    return content


# process 'replaceWord' command
def process_replace_word(content, command_line):
    match = re.search(r'replace\s+"(.+)"\s+"(.+)"', command_line)  # Match the replace command with index and
    # replacement string
    if match:
        try:
            # Parse index and string to replace
            word = match.group(1)
            replacementText = match.group(2)

            # Ensure index is within bounds
            if word in content:
                # Replace part of the text starting at index with replacement string
                content = re.sub(r'\b{}\b'.format(re.escape(word)), replacementText, content)  # Use word boundaries for accuracy
        except Exception as e:
            pass  # If there are parsing issues, ignore the command
    return content


# process 'reverse'
def process_reverse(content, command_line):
    match = re.search(r'reverse\s+(\d+)', command_line)
    if match:
        try:
            line = int(match.group(1))
            if 0 <= line < len(content):
                content = content[:line: + 1][::-1]
        except ValueError:
            pass
    return content


# processing 'newLine' command
def process_new_line(content, command_line):
    match = re.search(r'newLine\s+(\d+)', command_line)  # Match the command with an index
    if match:
        try:
            line_index = int(match.group(1))  # Parse the index from regex
            # Split content into lines
            lines = content.split('\n')  # Split the text into individual lines
            if 0 <= line_index < len(lines):  # Ensure index is within bounds
                # Insert a new empty line after the specified line index
                lines.insert(line_index + 1, '')  # Add a blank line after the specified index
                # Join the lines back into a single string
                content = '\n'.join(lines)
        except ValueError:
            pass  # Ignore the command if parsing fails
    return content


# processing 'duplicate' command
def process_duplicate(content, command_line):
    match = re.search(r'duplicate\s+"(.+)"', command_line)  # Match the command and extract the string to duplicate
    if match:
        word_to_duplicate = re.escape(match.group(1))  # Escape regex special characters to avoid regex issues
        # Replace all occurrences of the word with its duplicate
        content = re.sub(word_to_duplicate, word_to_duplicate + word_to_duplicate, content)
    return content


# processing 'swapWithNextLine' command
def process_swap_with_next_line(content, command_line):
    match = re.search(r'swapWithNextLine\s+(\d+)', command_line)  # Match the command and extract index
    if match:
        try:
            line_index = int(match.group(1))  # Parse index
            # Split content into lines
            lines = content.splitlines()

            # Ensure the index is valid
            if 0 <= line_index < len(lines) - 1:
                # Swap the content of the line at line_index and line_index + 1
                lines[line_index], lines[line_index + 1] = lines[line_index + 1], lines[line_index]

                # Join the lines back into a single string
                content = "\n".join(lines)
        except ValueError:
            pass  # Ignore invalid input
    return content


# processing 'swapWithPreviousLine' command
def process_swap_with_previous_line(content, command_line):
    match = re.search(r'swapWithPreviousLine\s+(\d+)', command_line)
    if match:
        try:
            line_index = int(match.group(1))
            lines = content.splitlines()
            if 1 <= line_index < len(lines) - 1:
                lines[line_index], lines[line_index - 1] = lines[line_index - 1], lines[line_index]
                content = "\n".join(lines)
        except ValueError:
            pass
    return content


# processing 'removeWhiteSpaces' command
def process_remove_white_spaces(content, command_line):
    if "removeWhiteSpaces" in command_line:
        # Replace multiple spaces or tabs with a single space (anywhere in the content)
        content = re.sub(r'\s+', ' ', content).strip()
    return content


# processing 'readNextLine' command
def process_read_next_line(content, command_line, current_line_index):
    match = re.search(r'readNextLine', command_line)  # Check if the command exists
    if match:
        try:
            # Split content into a list of lines
            lines = content.split('\n')

            # Check if the index is within bounds
            if current_line_index + 1 < len(lines):
                # If there is a next line
                next_line = lines[current_line_index + 1]
                print(f"Next line exists: '{next_line}'")
                return next_line
            else:
                # No new line exists
                print("No new line available after the current index.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return None


# processing 'writeToConsole' command
def process_write_to_console(content, command_line):
    match = re.search(r'writeToConsole\s+(\d+)', command_line)
    if match:
        try:
            line_index = int(match.group(1))
            lines = content.split('\n')
            # Ověření, zda je index v bezpečném rozsahu
            if 0 <= line_index < len(lines):
                print(lines[line_index])
            else:
                print(f"Index {line_index} není v platném rozsahu. Celkový počet řádků: {len(lines)}")
        except ValueError:
            print("Chybný formát čísla v příkazu 'writeToConsole'")
    return content


# Process all commands in memory sequentially
def process_commands_in_memory(args, content, commands):
    for line in commands:
        if line.startswith("addToEnd"):  # Process 'addToEnd' commands
            content = process_add_to_end(content, line)
        elif line.startswith("remove"):  # Process 'remove' commands
            content = process_remove(content, line)
        elif line.startswith("removeWord"):
            content = process_remove_word(content, line)
        elif line.startswith("reverse"):
            content = process_reverse(content, line)
        elif line.startswith("newLine"):
            content = process_new_line(content, line)
        elif line.startswith("duplicate"):
            content = process_duplicate(content, line)
        elif line.startswith("swapWithNextLine"):
            content = process_swap_with_next_line(content, line)
        elif line.startswith("swapWithPreviousLine"):
            content = process_swap_with_previous_line(content, line)
        elif line.startswith("removeWhiteSpaces"):
            content = process_remove_white_spaces(content, line)
        elif line.startswith("readNextLine"):
            content = process_read_next_line(content, line, current_line_index=0)
        elif line.startswith("writeToConsoleLine"):
            content = process_write_to_console(content, line)


    return content


# Write the processed content back to an output file
def write_output_to_file(args, content):
    with open(args.outputText, "w", encoding="utf-8") as file:
        file.write(content)


# Main function to handle the program's execution flow
def main():
    args = arguments()  # Parse and handle arguments
    verify_paths(args)  # Verify file paths and existence

    commands = reading_commands(args)  # Read all commands
    content = read_file_to_memory(args)  # Load initial text into memory
    content = process_commands_in_memory(args, content, commands)  # Process commands sequentially
    write_output_to_file(args, content)  # Write the processed text back to a file

    print("Processing complete.")


# Entry point of the script
if __name__ == "__main__":
    main()
