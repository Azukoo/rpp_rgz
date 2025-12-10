import unittest
import json
from app import app

class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_analyze_success(self):
        payload = {'text': 'Привет мир! Привет всем. Привет снова.'}
        response = self.app.post('/analyze', data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('word_count', data)
        self.assertIn('top_words', data)
        self.assertEqual(data['word_count'], 6)
        self.assertEqual(data['top_words'][0]['word'], 'привет')
        self.assertEqual(data['top_words'][0]['count'], 3)

    def test_missing_text(self):
        payload = {'wrong_key': 'value'}
        response = self.app.post('/analyze', data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)

    def test_empty_text(self):
        payload = {'text': ''}
        response = self.app.post('/analyze', data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['word_count'], 0)
        self.assertEqual(data['top_words'], [])

if __name__ == '__main__':
    unittest.main()