🌱 EcoBot AI – Green Hydrogen Chatbot

EcoBot AI is an interactive web-based chatbot designed to educate users about green hydrogen, energy storage technologies, and the net-zero transition. It uses Natural Language Processing (NLP) to understand user queries and respond intelligently.

🚀 Features

💬 Interactive chatbot interface
🌍 Focus on Green Hydrogen & Sustainability
🧠 NLP-based intent recognition using NLTK
🎨 Modern glassmorphism UI with animated background
📊 Supports HTML tables for technical comparisons
💾 Export chat history as a text file

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
NLP: NLTK (tokenization + stemming)
Data: JSON-based intent system

📂 Project Structure
├── app.py                # Flask backend server
├── chatbot_logic.py      # NLP + response logic
├── intents.json          # Chatbot training data
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   └── style.css         # Styling

⚙️ How It Works
1. Backend Server

The Flask app handles routing and communication between frontend and chatbot logic.

/ → Loads chatbot UI
/get_response → Processes user input and returns response

2. Chatbot Logic

The chatbot processes text using:

Tokenization
Stemming
Keyword matching

It selects the best matching intent based on word overlap.

3. Intents System

All chatbot knowledge is stored in a structured JSON file:

patterns → user inputs
responses → bot replies

4. Frontend UI

The UI provides:

Animated chat interface
Typing indicator
Save chat feature
Smooth messaging experience

5. Styling

Modern UI design using:

Gradient backgrounds
Glassmorphism
Floating hydrogen bubble animations

▶️ Installation & Setup
1. Clone the Repository
git clone <your-repo-url>
cd <project-folder>

2. Install Dependencies
pip install flask nltk

3. Run the Application
python app.py

4. Open in Browser
http://127.0.0.1:5000

💡 Example Questions You Can Ask

What is green hydrogen?
How is hydrogen produced?
Compare batteries and hydrogen
What are electrolyzers?
What are the challenges?

🔮 Future Improvements
🤖 Use machine learning models instead of rule-based matching
🌐 Deploy online (Heroku / Render / AWS)
📱 Mobile responsiveness improvements
🧩 Add voice input/output
📊 Integrate real-time energy data

🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

📜 License

This project is open-source and available under the MIT License.




