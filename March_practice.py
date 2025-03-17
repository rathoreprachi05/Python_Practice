
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
#-------------------------------------------------

def check_perf_no(n):
    sum1 = 0
    for i in range(1, n, 1):
        if(n % i == 0):
            sum1 += i
    if(sum1 == n):
        return True

n = int(input("Enter a number: "))

n1 = check_perf_no(n)
if(n1):
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")

            


 
