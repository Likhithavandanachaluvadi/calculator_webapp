from flask import Flask, render_template, request
import calculator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            operation = request.form.get('operation')

            if operation == 'add':
                result = calculator.add(num1, num2)
            elif operation == 'subtract':
                result = calculator.subtract(num1, num2)
            elif operation == 'multiply':
                result = calculator.multiply(num1, num2)
            elif operation == 'divide':
                result = calculator.divide(num1, num2)
            elif operation == 'percentage':
                percent = float(request.form.get('percent', 0))
                result = calculator.percentage(num1, percent)
            elif operation == 'factorial':
                result = calculator.factorial(int(num1))

        except ValueError:
            result = "Invalid input. Please enter valid numbers."
        except Exception as e:
            result = f"Error: {e}"  # Shows the exact error for debugging

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
