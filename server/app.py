#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:example>')
def print_string(example):
    print(example)
    return f'{example}'

@app.route('/count/<int:some_number>')
def count(some_number):
    num_range = ''
    for num in range(some_number):
        num_range += f'{num}\n'
    return num_range

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    total = 0
    if operation == "+":
        total = int(num1) + int(num2)
    elif operation == "-":
        total = int(num1) - int(num2)
    elif operation == "*":
        total = int(num1) * int(num2)
    elif operation == "div":
        total = int(num1) / int(num2)
    elif operation == "%":
        total = int(num1) % int(num2)
    return str(total)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
