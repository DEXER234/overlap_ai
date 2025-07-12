from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Replace with your valid OpenRouter API key
)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.get_json().get('message', '')
    try:
        completion = client.chat.completions.create(
            model="moonshotai/kimi-dev-72b:free",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = completion.choices[0].message.content
        return jsonify({'response': bot_reply})
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000) 

