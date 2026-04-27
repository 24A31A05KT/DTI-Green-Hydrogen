from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_message = request.get_json().get("message")
    if not user_message:
        return jsonify({"reply": "I didn't catch that."})
    return jsonify({"reply": get_response(user_message)})

if __name__ == "__main__":
    print("Server running! Go to http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, port=5000)