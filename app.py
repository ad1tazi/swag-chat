from flask import Flask, render_template, request, jsonify
import json
from generate import generate

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    user_text = request.form['text']
    conversation = request.form.get('conversation', '[]')

    generated_text, updated_conversation = generate(user_text, conversation)
    
    return jsonify({
        'generated_text': generated_text,
        'updated_conversation': json.dumps(updated_conversation)
    })

if __name__ == '__main__':
    app.run(debug=True)
