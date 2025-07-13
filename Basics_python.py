# Create a program to solve a quadratic equation given coefficients a, b, and c.
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
x1 = (b * -1 + (b * b - 4 * a * c) ** 0.5) / 2 * a
x2 = (b * -1 - (b * b - 4 * a * c) ** 0.5) / 2 *  a
print(x1, x2) 

#--------------------------------------------------------------------------------------------------------------
# Write a Python program to validate variable names based on Python's naming conventions.

def checker(variable):
  
  valid = True
  if(variable[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"):
    valid = False
  for i in variable :
     if(i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789"):
       valid = False
  return valid
variable = input("Enter variable's name: ")
answer = checker(variable)
print(answer)

#-----------------------------------------------------------------------------------------

# Write a program that evaluates a mathematical expression entered by the user as a string.
# "12+23*4-21/3"
def math(math_exp):
  init = 0
  answer = 0
  operator = ""
  for i in range(0, len(math_exp), 1):
    if(math_exp[i] in "+-*/%"):
      num = int(math_exp[init:i])
      init = i + 1
      if(operator == ""):
        answer = num
      elif(operator == "+"):
        answer = num + answer
      elif(operator == "-"):
        answer = answer - num
      elif(operator == "*"):
        answer = num * answer
      elif(operator == "/"):
        answer /= num
      operator = math_exp[i]
  num = int(math_exp[init:])
  init = i + 1
  if(operator == ""):
    answer = num
  elif(operator == "+"):
    answer = num + answer
  elif(operator == "-"):
    answer = answer - num
  elif(operator == "*"):
    answer = num * answer
  elif(operator == "/"):
    answer /= num
  return answer
math_exp = input("Enter the mathematical expression: ")
ans = math(math_exp)
print(ans)

#---------------------------------------------------------------------------



