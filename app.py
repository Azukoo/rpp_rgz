from flask import Flask, request, jsonify
from flasgger import Swagger
import re
from collections import Counter

app = Flask(__name__)
Swagger(app)

@app.route('/analyze', methods=['POST'])
def analyze_text():
    """
    Анализ текста: подсчёт слов и определение топ-5 частотных слов.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              example: "Привет мир! Привет всем."
    responses:
      200:
        description: Результат анализа
        schema:
          type: object
          properties:
            word_count:
              type: integer
            top_words:
              type: array
              items:
                type: object
                properties:
                  word:
                    type: string
                  count:
                    type: integer
    """
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400

    text = data['text']
    # Удаляем всё, кроме букв и пробелов (для поддержки русского и английского)
    words = re.findall(r'[а-яА-Яa-zA-Z]+', text.lower())
    word_count = len(words)
    word_freq = Counter(words).most_common(5)

    top_words = [{'word': word, 'count': count} for word, count in word_freq]

    return jsonify({
        'word_count': word_count,
        'top_words': top_words
    })

if __name__ == '__main__':
    app.run()