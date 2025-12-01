
print("Hello, world")
print("A new language a new day.")
c = int(input("Choose a function 1. is_even 2. factorial :"))

def is_even(n):
	if n%2==0:
		return 1
	else:
		return 0

def factorial(n):
	if n<0:
		return -1
	elif n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)
  
if c == 1: 
  n = int(input("Enter a number:"))
  print(is_even(n)==1)
elif c == 2:
  n = int(input("Enter a number:"))
  print(factorial(n))
else:
  print("Invalid choice")
