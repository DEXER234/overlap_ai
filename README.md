# Overlap Chatbot

A modern, fast, and customizable AI chatbot web app built with Flask and JavaScript. Overlap provides detailed, structured answers and a beautiful UI, ready for local or cloud deployment.

## Features
- Fast, responsive chat UI with typewriter effect
- User authentication (Firebase)
- Customizable system prompt and model
- Professional, modern design with your own logo
- Real-time time queries, curated answers, and fallback to LLM

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

### 3. Run the Flask app
```bash
python app.py
```

- The app will be available at [http://localhost:8000](http://localhost:8000)

### 4. (Optional) Configure your LLM backend
- By default, the app expects a local LLM server at `http://localhost:4891/v1/chat/completions`.
- You can change the model or endpoint in `app.py`.

### 5. (Optional) Firebase Auth
- Update `auth.html` with your Firebase project credentials if you want to use authentication.

## Usage
- Open your browser and go to [http://localhost:8000](http://localhost:8000)
- Start chatting!

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT 