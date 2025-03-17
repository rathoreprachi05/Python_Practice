
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

#---------------------------------------

def check_armstrong_no(n):
    sum1 = 0
    length = len(n)
    for i in n:
        sum1 += int(i) ** length
    if(sum1 == int(n)):
        return True
    else:
        return False

n = input("Enter a number: ")

n1 = check_armstrong_no(n)
if(n1):
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")

#--------

def find_fact(n):
    if(n == 0):
        return  1
    return (n * find_fact(n-1))
n = int(input("Enter a number: "))

n1 = find_fact(n)
print(n1)

#------

def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(1, n+1, 1):
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3

n = int(input("Enter a number: "))

fibonacci(n)
        
        
    





        

            


 
