from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

model = pickle.load(open('milkpred.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

