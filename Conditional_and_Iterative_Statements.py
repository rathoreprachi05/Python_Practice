# Write a program to print all prime numbers between 1 and n.
def prime_checker(n):
  for j in range(2,n,1):
    for i in range(2, j, 1):
      if(j % i == 0):
        # print(j,"is not a prime number")
        break
    else:
      print(j)
n = int(input("Enter a number:"))
prime_checker(n)
# Create a program that displays the multiplication table for numbers from 1 to 10 using nested loops.
# Implement the Collatz Conjecture for a given positive integer input (reduce to 1 using `n = n/2` if even, and `n = 3*n + 1` if odd).
# Write a program to generate all possible permutations of a list of numbers
