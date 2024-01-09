from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # input data and generate prediction
        pass
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)