from flask import Flask, render_template
from flask import send_from_directory
import os

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    #Testing Comment section


