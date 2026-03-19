from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "flask says: lis is cool!"

if __name__ == "__main__":
    app.run(debug=True)