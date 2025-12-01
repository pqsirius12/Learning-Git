
print("Hello, world")
print("A new language a new day.")
def factorial(n):
	if n<0:
		return -1
	elif n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)
n = int(input("Enter a number:"))
print(factorial(n))
