from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#run the application
port = 5000
app.run(host="0.0.0.0", port=port, debug=True)
