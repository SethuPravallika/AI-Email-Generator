from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from ai_utils import generate_email_with_ai
from email_utils import send_email

load_dotenv()
# Verify Groq API key is loaded
groq_key = os.getenv("GROQ_API_KEY")
print("Groq API Key loaded:", "✅" if groq_key else "❌")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-email', methods=['POST'])
def generate_email():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
            
        email_text = generate_email_with_ai(prompt)
        return jsonify({'email': email_text})
    except Exception as e:
        print(f"Error in generate_email: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/send-email', methods=['POST'])
def send():
    try:
        data = request.get_json()
        recipients = data.get('recipients', '')
        content = data.get('emailContent', '')
        
        if not recipients or not content:
            return jsonify({'error': 'Recipients and email content are required'}), 400
            
        success = send_email(recipients, content)
        return jsonify({'success': success})
    except Exception as e:
        print(f"Error in send_email: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)