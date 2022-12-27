import csv
from http import HTTPStatus
import requests
from faker import Faker
from flask import Flask, request, Response
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)

URL = 'https://bitpay.com/api/rates/{}'
CURRENCY = 'https://bitpay.com/currencies'


@app.route("/generate_students")
@use_kwargs(
    {
        "count":fields.Int(
            missing=10,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location="query"
)
def generate_students(count):
    faker = Faker()
    students_data = []
    for i in range(count):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()
        birthday = faker.birthday()
        students_data.append([first_name, last_name, email, password, birthday])
    with open("students.csv", "w") as file:
        writer = csv.writer(file)
            for row in students_data:
                writer.writerow(row)
    return students_data


@app.route("/bitcoin")
@use_kwargs(
    {
        "curency":fields.Str(
            missing="USD",
        ),
    },
    location="query"
)
def get_bitcoin_value(currency, count):
    response = request.get(URL.format(currency))
    currency_data = requests.get(CURRENCY)
    if response.status_code not in (HTTPStatus.OK, ) or currency_data.status_code not in (HTTPStatus.OK, ):
        return Response(
            "ERROR: Something went wrong.",
            status=response.status_code
        )
    rates = response.json()
    currency_info = currency_data.json()
    symbol = currency_info["data"]
    for info in symbol:
        if currency == info["code"]:
            symbol == info["symbol"]

    result = rates["rate"] * count

    return f"The Bitcoin rate is {currency_info}{symbol}"



app.run(port=5005, debug=True)

