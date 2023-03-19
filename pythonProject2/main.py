import re
# a python program to perform arithmetic on numbers

Type_in_your_expression = input("Type in the expression you want to perform: ")
print(Type_in_your_expression.split())

pattern_num = "[0-9]+"

def funt_cal():
    for c in Type_in_your_expression:
        num = (re.findall(pattern_num, Type_in_your_expression))
        # print(c)
        if c == '/':
          print("I shall divide")
          # print(int() / int())
        if c == "*":
          print("I shall multiply")
          # print(int() * int())
        if c == "+":
          print("I shall add")
          # print(int() + int())
        if c == "-":
            print("i shall subtract")
            # print(int() - int())
        print(num)

funt_cal()


