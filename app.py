from flask import Flask
from markov_chain import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = main()
    return text