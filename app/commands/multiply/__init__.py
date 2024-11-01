import sys 
from app.commands import Command


class MultiplyCommand(Command):
    def execute(self, params=None):
        if len(params) >= 2:
            try:
                a, b = map(float, params)  # Convert both to float to support decimals
                print(a * b)
            except valueError:
                print("please input valid numbers")
        else:
            print("please input 2 numbers")
        print(params)