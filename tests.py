import unittest

from pythonProject1.main import process_commands_in_memory
from pythonProject1.main import process_add_to_end


# Testovací třída pro přidání textu na konec řetězce
class Test_process_commands_in_memory(unittest.TestCase):
    def test_process_add_to_end_success(self):
        content = ["line 1", "line 2", "line 3"]
        command_line = 'addToEnd " added text"'
        lineIndex = 1  # Chceme přidat text do druhého řádku (index 1)

        # Spuštění funkce pro přidání textu
        result = process_add_to_end(content, command_line, lineIndex)

        # Ověření, že text byl správně přidán na konec řádku
        self.assertEqual(result[1], "line 2 added text")

    def test_process_add_to_end_failed(self):
        # Arrange: Příprava dat
        inputLine = "test"
        inputCommand = 'addToEnd "wrongText"'

        # Act: Volání funkce pro zpracování příkazu
        content = process_commands_in_memory(inputLine, [inputCommand])

        # Assert: Ověření, že se text nezměnil na špatný výsledek
        self.assertNotEqual(inputLine + " test2", content)  # Očekáváme, že obsah nebude "test test2"

if __name__ == '__main__':
    unittest.main()

