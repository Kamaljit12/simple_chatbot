# GROQ Chatbot

A simple chatbot powered by GROQ's LLM API with a beautiful web interface.

## Features

- 🤖 Powered by GROQ's Llama 3 8B model
- 💬 Real-time chat interface
- 🎨 Modern, responsive UI
- ⚡ Fast API backend
- 🔒 Environment-based API key management

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get GROQ API Key

1. Visit [GROQ Console](https://console.groq.com/)
2. Sign up or log in
3. Create a new API key

### 3. Configure Environment

1. Copy the content from `env_template.txt`
2. Create a new file named `.env`
3. Replace `your_groq_api_key_here` with your actual API key

### 4. Run the Backend

```bash
python backend_api.py
```

The API will be available at `http://localhost:8000`

### 5. Open the Web Interface

Open `index.html` in your web browser or serve it using a local server:

```bash
# Using Python's built-in server
python -m http.server 3000
```

Then visit `http://localhost:3000`

## Usage

1. Start the backend server
2. Open the web interface
3. Type your message and press Enter or click Send
4. The chatbot will respond using GROQ's LLM

## API Endpoints

- `GET /` - Health check
- `POST /chat` - Send a message to the chatbot

### Example API Usage

```python
import requests

response = requests.post("http://localhost:8000/chat", 
                        json={"message": "Hello, how are you?"})
print(response.json()["response"])
```

## Configuration

You can modify the LLM parameters in `backend_api.py`:

- `model`: Change the GROQ model (e.g., "llama3-8b-8192", "mixtral-8x7b-32768")
- `temperature`: Control randomness (0.0 to 1.0)
- `max_tokens`: Maximum response length
- `top_p`: Nucleus sampling parameter

## Troubleshooting

- Make sure your GROQ API key is valid and has sufficient credits
- Ensure the backend server is running on port 8000
- Check browser console for any JavaScript errors
- Verify CORS settings if accessing from a different domain

## Requirements

- Python 3.7+
- GROQ API key
- Modern web browser
