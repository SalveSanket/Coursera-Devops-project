# app.py
from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "🚀 Welcome to the Simple Flask App! Ready to build something amazing? 🌟"

if __name__ == '__main__':
    app.run(debug=True)