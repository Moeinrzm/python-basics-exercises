# using safe method by using eval for a calculator
def safe_Calc(expression):
    allowed_chars = "0123456789+-*/().** %"
    for char in expression:
        if char not in allowed_chars:
            raise ValueError(f"not allowed chars used {char}")
        result = eval(expression)
        return result
    return eval(expression, {__builtins__: {}}, {})
try:
    user_input = input("enter your math expression : ")
    print(f"result is {safe_Calc(user_input)}")
except Exception:
    print("error at runnig",Exception)
