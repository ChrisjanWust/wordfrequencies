import unittest
from wordfrequencies import get_part_of_speech, get_word_rank

class TestWordFrequency(unittest.TestCase):
    def test_word_frequency(self):
        self.assertLess(get_word_rank("the"), get_word_rank("man"))
        self.assertLess(get_word_rank("man"), get_word_rank("jumps"))
        self.assertEqual(get_part_of_speech("the"), "FUNCTION_WORD")
        self.assertEqual(get_part_of_speech("man"), "NOUN")
        self.assertEqual(get_part_of_speech("jumps"), "VERB")
        self.assertIsNone(get_part_of_speech("Chrisjan"))

if __name__ == "__main__":
    unittest.main()