from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/convert/<celsius>')
def convert_temperature(celsius):
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f"The temperature {celsius}°C in Fahrenheit is {fahrenheit}°F"
    except ValueError:
        return "Invalid input. Please enter a valid temperature in Celsius."


if __name__ == '__main__':
    app.run()
