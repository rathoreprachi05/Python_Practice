'''
#-----------------------------------------------------------------

# Basic function to add 10 to the given integer and return it

def Add(n):
    print(n+10)
n = int(input("Enter a number: "))

Add(n)

#-----------------------------------------------------------------

# Basic function to print next 10 numbers after the given integer

def Add(n):
    for i in range(1, 11, 1):
        print(n+i)
n = int(input("Enter a number: "))

Add(n)

#-----------------------------------------------------------------

#Basic function to check is a given number is even or odd

def Add(n):
    if(n % 2 == 0):
        print(n,"is an even number")
    else:
        print(n,"is an odd number")
n = int(input("Enter a number: "))
Add(n)

#-----------------------------------------------------------------

# Function to return the number of odd and even elements in a list

def Add(n):
    evencount = 0
    oddcount = 0
    for i in n:
        if(i % 2 == 0):
            evencount += 1
        else:
            oddcount += 1
    return (evencount, oddcount)
n = list(map(int, input("Enter the elements of list: ").split(" ")))
a,b = Add(n)
print(a, b)

#---------------------------------------------------------------------------------

# Function to return the count of multiples if 3 and 7 in a given list

def multiples(n):
    countof3 = 0
    countof7 = 0
    for i in n:
        if(i % 3 == 0):
            countof3 += 1
        elif(i % 7 == 0):
            countof7 += 1
    return (countof3, countof7)
n = list(map(int, input("Enter the elements of the list: ").split(" ")))
a,b = multiples(n)
print(a, b)
'''
#------------------------------------------------------------------------------

# Function to print first n terms of a fibonacci series

def fibonacci_series(n):
    n1 = 0
    n2 = 1
    for i in range(1, n+1, 1):
         print(n1)
         n3 = n1 + n2
         n1 = n2
         n2 = n3
n = int(input("Enter a number: "))
fibonacci_series(n)

#------------------------------------------------------------------------------
