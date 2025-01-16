import unittest
from unittest.mock import patch
from io import StringIO
from pythonProject1.main import process_add_to_end
from pythonProject1.main import process_remove
from pythonProject1.main import process_remove_word
from pythonProject1.main import process_replace
from pythonProject1.main import process_replace_word
from pythonProject1.main import process_reverse
from pythonProject1.main import process_add_new_line
from pythonProject1.main import process_duplicate
from pythonProject1.main import process_swap_with_next_line
from pythonProject1.main import process_swap_with_previous_line
from pythonProject1.main import process_remove_white_spaces
from pythonProject1.main import process_write_to_console

import re

from unittest.mock import patch
import sys

class TestProcessAddToEnd(unittest.TestCase):
    def test_add_to_end(self):
        # Vstupní data
        content = ["This is the first line", "This is the second line"]
        command_line = 'addToEnd "added text"'
        lineIndex = 0

        # Očekávaný výstup
        expected_output = ["This is the first line added text", "This is the second line"]

        # Zavolání testované funkce
        result = process_add_to_end(content, command_line, lineIndex)

        # Ověření, že výstup odpovídá očekávanému výsledku
        self.assertEqual(result, expected_output)


class TestProcessremove(unittest.TestCase):
    def test_remove(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('remove 0 5')
        lineIndex = 0


        expected_output = ["is the first line", "This is the second line"]


        result = process_remove(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestProcessRemoveWord(unittest.TestCase):
    def test_remove_word(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('removeWord "is"')
        lineIndex = 0

        expected_output = ["This the first line", "This is the second line"]

        result = process_remove_word(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestProcessReplace(unittest.TestCase):
    def test_replace(self):
        content = ["This is the first line", "This is the second"]
        command_line = ('replace 4 "arent"')
        lineIndex = 0

        expected_output = ["This arnt fisrt line", "This is the second line"]

        result = process_replace(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)

class TestProcessReplaceWord(unittest.TestCase):
    def test_replace_word(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('replaceWord "first" "last"')
        lineIndex = 0

        expected_output = ["This is the last line", "This is the second line"]

        result = process_replace_word(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestprocessReverse(unittest.TestCase):
    def test_reverse(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('reverse 3')
        lineIndex = 0

        expected_output = ["This is the tsrif line", "This is the second line"]

        result = process_reverse(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestprocessAddNewLine(unittest.TestCase):
    def test_add_new_line(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('addNewLine')
        lineIndex = 0

        expected_output = ["This is the first line", "", "This is the second line"]

        result = process_add_new_line(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestprocessDuplicate(unittest.TestCase):
    def test_duplicate(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('duplicate "This"')
        lineIndex = 0

        expected_output = ["ThisThis is the first line", "This is the second line"]

        result = process_duplicate(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestprocessSwapWithNextLine(unittest.TestCase):
    def test_swap_with_next_line(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('swapWithNextLine')
        lineIndex = 0

        expected_output = ["This is the second line", "This is the first line"]

        result = process_swap_with_next_line(content, command_line , lineIndex)

        self.assertEqual(result, expected_output)


class TestprocessSwapWithPreviousLine(unittest.TestCase):
    def test_swap_with_previous_line(self):
        content = ["This is the first line", "This is the second line"]
        command_line = ('swapWithPreviousLine')
        lineIndex = 1

        expected_output = ["This is the second line", "This is the first line"]

        result = process_swap_with_previous_line(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestprocessRemoveWhiteSpaces(unittest.TestCase):
    def test_remove_white_spaces(self):
        content = ["This is the first line", "This is the second         line"]
        command_line = ('removeWhiteSpaces')
        lineIndex = 1

        expected_output = ["This is the first line", "This is the second line"]

        result = process_remove_white_spaces(content, command_line, lineIndex)

        self.assertEqual(result, expected_output)


class TestProcessWriteToConsole(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_process_write_to_console(self, mock_stdout):
        # Vstupní data pro funkci
        content = ["This is the first line", "This is the second line"]
        command_line = "writeToConsole"
        lineIndex = 1

        # Zavoláme funkci
        process_write_to_console(content, command_line, lineIndex)

        self.assertEqual(mock_stdout.getvalue(), "This is the second line\n")


if __name__ == "__main__":
    unittest.main()
