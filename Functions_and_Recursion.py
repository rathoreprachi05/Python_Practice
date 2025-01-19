# Write a function to solve the Tower of Hanoi problem for `n` disks.

# Create a recursive function to generate all subsets of a given list (power set).

# Write a function to calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
#  Write a function to calculate the greatest common divisor (GCD) of two numbers.
def hcf_finder(a,b):
  hcf = 1
  if(a>b):
    mini = b
  else:
    mini = a
  for i in range(1, mini+1, 1):
    if(a % i == 0 and b % i == 0):
      if(i > hcf):
        hcf = i
  return hcf
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

ans = hcf_finder(a,b)
print(ans)
      
# Implement a recursive function to determine if a string matches a given pattern (basic regex matching).

# Write a recursive function to calculate the factorial of a number.
def fact(n):
  if(n == 0):
    return 1
  return ( n * fact(n-1))
a = int(input("Enter a number: "))
factorial = fact(a)
print(factorial)

# Create a function that calculates the nth Fibonacci number using recursion.
def fibonacci_series(n, a=1, b=1):
  if(n == 1 or n == 2):
      return 1
  if(n == 3):
    return a+b
  return fibonacci_series(n-1, b, a+b)
n = int(input("Enter a num: "))
ans = fibonacci_series(n)
print(ans)
  
  
# Write a function to find the sum of digits of a number.
def Sum(n):
   if(n / 10 == 0):
       return n%10
   r = n % 10
   q = n // 10
   return r + Sum(q)
n = int(input("enter a num: "))
ans = Sum(n)
print(ans)
# Implement a function to check if a number is a power of two.
