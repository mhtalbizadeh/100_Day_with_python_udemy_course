
while True:

    first_number = int(input("what is the first number? "))
    input_operator = input("+ \n- \n* \n/ \npick an operator: ")
    second_number = int(input("what is the second number? "))

    while True:
        def calculate(first_number, second_number, input_operator):
            if input_operator == "+":
                return plus(first_number, second_number)
            elif input_operator == "-":
                return minus(first_number, second_number)
            elif input_operator == "*":
                return multiply(first_number, second_number)
            elif input_operator == "/":
                return divide(first_number, second_number)

        def plus(a,b):
            return a+b
        def minus(a,b):
            return a-b
        def multiply(a,b):
            return a*b
        def divide(a,b):
            if b == 0:
                return "infinity"
            return a/b

        print(f"type 'y' to continue calculation with {calculate(first_number, second_number, input_operator)} or type 'n' to exit")
        if input() == "y":
            first_number = calculate(first_number, second_number, input_operator)
            input_operator = input("+ \n- \n* \n/ \npick an operator: ")
            second_number = int(input("what is the second number? "))
        else:
            break    
