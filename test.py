from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<p>yuh</p>"
print("Yo what's up gamers")
