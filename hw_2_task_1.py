import random
import string

import pandas as pd
from flask import Flask
app = Flask(__name__)


@app.route("/generate_password")
def generate_password():
    """
    from 10 to 20 chars
    upper and lower case
    """
    letters_up = string.ascii_uppercase
    letters_low = string.ascii_lowercase
    digits = string.digits
    length = random.randint(10, 20)
    password = []

    for _ in range(length):
        password.append(random.choice(letters_up))
        password.append(random.choice(letters_low))
        password.append(random.choice(digits))

    password_result = ''.join(password)


@app.route('/average')
def average_params(filename="hw.csv"):
    """
    csv file with students
    1.calculate average high
    2.calculate average weight
      """
    data = pd.read_csv("hw.csv")
    df = pd.DataFrame(data, columns=[" Height(Inches)", " Weight(Pounds)"])
    average_high = df[" Height(Inches)"].mean()
    average_weight = df[" Weight(Pounds)"].mean()
    return f"<p>1. Average High: {average_high}<br>2. Average Weight: {average_weight}</p>"


app.run(port=5001, debug=False)
