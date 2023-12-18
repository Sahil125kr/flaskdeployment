
from flask import Flask
 

app = Flask(__name__)
 

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello Sahil'
 
