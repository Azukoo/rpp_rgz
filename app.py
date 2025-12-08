from flask import Flask, request, jsonify
from collections import Counter
import re

app = Flask(__name__)

def analyze_text(text: str):
    """Анализирует текст: общее число слов и топ-5 частотных."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    most_common = Counter(words).most_common(5)
    return {
        "total_words": total_words,
        "most_common_words": most_common
    }

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "JSON must contain 'text' field"}), 400
    try:
        result = analyze_text(data['text'])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)