from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='template')

@app.route('/')
def bosh_sahifa():
    return render_template('index.html')

@app.route('/buyurtma')
def buyurtma():
    return render_template('buyurtma.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
