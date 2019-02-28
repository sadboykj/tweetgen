from flask import Flask
# from sample import sample, test, sentence
# import shortext.txt

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = "Hello World!"
    return text