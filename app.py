from flask import Flask, send_from_directory, request, jsonify
import requests
import re
import pytz
from datetime import datetime
# Add SerpAPI import
try:
    from serpapi import GoogleSearch
except ImportError:
    GoogleSearch = None
import os

app = Flask(__name__)

# Set your SerpAPI key here
SERPAPI_KEY = '7e75e8033f5fb975b046bd6c693c50b049da3f3328ec6425edadc827cd260416'

# Curated answers for popular questions
CURATED_ANSWERS = {
    'top 10 best place to visit in india': (
        "<h3>Top 10 Places to Visit in India</h3>"
        "<ul>"
        "<li><b>Taj Mahal</b>, Agra</li>"
        "<li>Jaipur (The Pink City)</li>"
        "<li>Kerala Backwaters</li>"
        "<li>Goa Beaches</li>"
        "<li>Varanasi</li>"
        "<li>Ladakh</li>"
        "<li>Rishikesh</li>"
        "<li>Andaman & Nicobar Islands</li>"
        "<li>Darjeeling</li>"
        "<li>Ranthambore National Park</li>"
        "</ul>"
        "<p>Each of these destinations offers a unique experience, from history and culture to nature and adventure.</p>"
    ),
    # Add more curated Q&A pairs here
}

def format_answer(answer):
    # If already contains HTML, return as is
    if any(tag in answer for tag in ['<ul', '<ol', '<h', '<p', '<b', '<strong']):
        return answer
    # Format numbered or bulleted lists
    if re.search(r'\n\d+\. ', answer):
        # Convert numbered list to <ul><li>...</li></ul>
        items = re.split(r'\n\d+\. ', answer)
        heading = items[0].strip()
        list_items = [f'<li>{item.strip()}</li>' for item in items[1:] if item.strip()]
        html = ''
        if heading:
            html += f'<h3>{heading}</h3>'
        if list_items:
            html += '<ul>' + ''.join(list_items) + '</ul>'
        return html
    # Format paragraphs
    if '\n' in answer:
        paras = [f'<p>{p.strip()}</p>' for p in answer.split('\n') if p.strip()]
        return ''.join(paras)
    # Default: wrap in <p>
    return f'<p>{answer.strip()}</p>'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.get_json().get('message', '').lower()
    # Real-time: Time in India
    if "time in india" in user_message or "current time india" in user_message:
        india_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%I:%M %p, %A, %d %B %Y')
        return jsonify({'response': f"The current time in India is {india_time}."})
    # Rule-based: Capital of India
    if "capital of india" in user_message:
        return jsonify({'response': '<span style="color:#06B6D4;font-weight:bold;">The capital of India is New Delhi.</span>'})
    # Rule-based responses for greetings and bot info
    if any(phrase in user_message for phrase in ["how are you", "how r u", "how are u"]):
        return jsonify({'response': "I'm doing great! I'm OVERLAP, your helpful chatbot assistant. How can I help you today?"})
    if any(phrase in user_message for phrase in [
        "who made you", "who created you", "your creator", "who is your creator", "who developed you", "who build you", "who built you", "who is your developer", "who is your maker"]):
        return jsonify({'response': "I was made by Debanjan."})
    if any(phrase in user_message for phrase in ["your name", "who are you", "what is your name", "about this chatbot", "what are you"]):
        return jsonify({'response': "My name is OVERLAP. I'm your AI chatbot assistant, here to help you with anything you need!"})
    # Curated answers
    for q, a in CURATED_ANSWERS.items():
        if q in user_message:
            return jsonify({'response': a})
    # Fallback: OpenRouter LLM API
    OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
    if not OPENROUTER_API_KEY:
        return jsonify({'response': "Sorry, no answer found and no LLM API key is set."})
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    openrouter_payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are OVERLAP, a super-fast, highly knowledgeable, and professional AI assistant. Always provide detailed, comprehensive, and well-structured answers. Use headings, bullet points, and paragraphs for clarity and readability. Start with a concise summary or main point in bold or highlighted text. Ensure your responses are easy to scan and visually appealing. Respond as quickly as possible while maintaining depth and accuracy."},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.3,
        "max_tokens": 128,
        "top_p": 0.9
    }
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=openrouter_payload
        )
        data = response.json()
        bot_reply = data['choices'][0]['message']['content']
        return jsonify({'response': bot_reply})
    except Exception as e:
        return jsonify({'response': "Sorry, there was an error connecting to the free LLM API. Please try again later."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000) 

