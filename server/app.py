#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    return string

@app.route('/add/<int:num1>/<int:num2>')    
def count(integer):
    result = ""
    for num in range (int):
        result += f"{num}\n"
    return str(result)

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        if num2 != 0:
            return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)




if __name__ == '__main__':
    app.run(port=5555, debug=True)
