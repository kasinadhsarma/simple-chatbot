# Friendly Business Chat Bot

A simple, interactive web-based chatbot built with Flask and JavaScript. This chatbot provides a clean interface for basic conversations and can be easily extended for business development purposes.

## Features

- 💬 Real-time chat interface
- 🎨 Clean, modern UI design
- ⚡ Instant responses
- 📱 Responsive design for all devices
- 🔄 Easy to extend and customize

## Tech Stack

- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- No database required (stateless)

## Project Structure

```
chatbot/
├── venv/                  # Python virtual environment
├── app.py                 # Flask application
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── chat.js       # Chat functionality
├── templates/
│   └── index.html        # Main chat interface
└── README.md             # This file
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

4. Run the application:
   ```bash
   export FLASK_APP=app.py
   python -m flask run
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Current Chat Responses

The chatbot currently responds to:
- "hi" or "hello" → Greeting message
- "how are you" → Friendly response
- "bye" → Farewell message
- Any other input → Default helpful response

## Customization

To customize the chatbot's responses, modify the response logic in `app.py`. The current implementation uses simple string matching, but you can extend it to include:
- Natural Language Processing
- API integrations
- Database connections
- Business logic implementation

## Contributing

Feel free to fork this project and customize it for your needs. Pull requests are welcome!

## License

This project is open source and available under the MIT License.
