from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Must return only this exact string inside h1
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    # Print to console
    print(param)
    # Return plain string, not wrapped in <p>
    return param

@app.route('/count/<int:param>')
def count(param):
    # Return numbers separated by newlines
    numbers = "\n".join(str(i) for i in range(param))
    return numbers + "\n"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # must use "div" not "/"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'

    # Tests expect plain number, not wrapped in HTML
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
