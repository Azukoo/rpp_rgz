import unittest
from app import analyze_text

class TestTextAnalyzer(unittest.TestCase):

    def test_empty_text(self):
        result = analyze_text("")
        self.assertEqual(result['total_words'], 0)
        self.assertEqual(result['most_common_words'], [])

    def test_simple_text(self):
        result = analyze_text("Hello world hello")
        self.assertEqual(result['total_words'], 3)
        self.assertEqual(result['most_common_words'][0][0], 'hello')
        self.assertEqual(result['most_common_words'][0][1], 2)

    def test_punctuation(self):
        result = analyze_text("Hello, world! Hello?")
        self.assertEqual(result['total_words'], 3)
        self.assertEqual(result['most_common_words'][0][0], 'hello')

if __name__ == '__main__':
    unittest.main()