# calculator.py

class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def clear_expression(self):
        self.expression = ""

    def evaluate_expression(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "Error"
