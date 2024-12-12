def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print("Select Operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = int(input("Select Operations form 1,2,3,4:"))

number_1 = int(input("Enter first Number: "))
number_2 = int(input("Enter second Number: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=", division(number_1, number_2))
else:
    print("Invalid Input")