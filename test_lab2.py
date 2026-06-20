import unittest
from lab2 import TextOperations

class TestTextOperations(unittest.TestCase):

    def test_find_unique_word_success(self):
        text = "Один два три. Один дев'ять шість. Три п'ять сім."
        self.assertEqual(TextOperations.find_unique_word(text), "два")

    def test_find_unique_word_register(self):
        text = "Один два. Чотири один."
        self.assertEqual(TextOperations.find_unique_word(text), "два")

    def test_no_unique_word(self):
        text = "Один два. Два один три."
        self.assertEqual(TextOperations.find_unique_word(text), "Унікального слова не знайдено.")

    def test_empty_text(self):
        with self.assertRaises(ValueError):
            TextOperations.find_unique_word("   ")

    def test_single_sentence(self):
        with self.assertRaises(ValueError):
            TextOperations.find_unique_word("Одне речення.")

if __name__ == '__main__':
    unittest.main()