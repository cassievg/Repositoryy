input1 = int(input("Insert number = "))
input2 = int(input("Insert another number = "))
input_op = input("Pick one: add, substract, multiply, divide = ")

if input_op == "add":
    print(int(input1 + input2))
elif input_op == "substract":
    print(int(input1 - input2))
elif input_op == "multiply":
    print(int(input1 * input2))
else:
    print(int(input1 / input2))