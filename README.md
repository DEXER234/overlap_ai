# Overlap Chatbot

A modern, fast, and customizable AI chatbot web app built with Flask and JavaScript. Overlap provides detailed, structured answers and a beautiful UI, ready for local or cloud deployment.

## Features
- Fast, responsive chat UI with typewriter effect
- User authentication (Firebase)
- Customizable system prompt and model
- Professional, modern design with your own logo
- Real-time time queries, curated answers, and fallback to LLM (via OpenRouter)

## Demo
![screenshot](mylogo.png)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/overlap-chatbot.git
cd overlap-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

**Note:** The backend now uses the [OpenAI Python SDK](https://pypi.org/project/openai/) to connect to [OpenRouter](https://openrouter.ai/). The `openai` package is required and included in `requirements.txt`.

### 3. Run the Flask app
```bash
python app.py
```

- The app will be available at [http://localhost:8000](http://localhost:8000)

### 4. Configure your LLM backend (OpenRouter)
- By default, the app uses OpenRouter as the LLM backend via the OpenAI SDK.
- You can change the model or endpoint in `app.py`.
- Make sure to set your OpenRouter API key in `app.py`.

### 5. (Optional) Firebase Auth
- Update `auth.html` with your Firebase project credentials if you want to use authentication.

## Usage
- Open your browser and go to [http://localhost:8000](http://localhost:8000)
- Start chatting!

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
