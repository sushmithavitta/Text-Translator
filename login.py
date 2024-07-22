import logging
from flask import Flask, render_template, request
from google.cloud import translate_v2 as translate

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize the translate client
translate_client = translate.Client()

def translate_text(translate_client, text, target_language):
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_language = request.form['language']
    translated_text = translate_text(translate_client, text, target_language)
    app.logger.info(f'Translated text: {translated_text}')
    return render_template('result.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
