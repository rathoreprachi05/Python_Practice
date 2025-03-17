
def calculate(n1, n2, s):
    if(s == "+"):
        return (n1 + n2)
    if(s == "-"):
        return (n1 - n2)
    if(s == "*"):
        return (n1 * n2)
    if(s == "/"):
        return (n1 / n2)
    if(s == "//"):
        return (n1 // n2)
    if(s == "%"):
        return (n1 % n2)
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
s = input("Enter a symbol: ")

cal1 = calculate(n1, n2, s)
print(cal1)


 
