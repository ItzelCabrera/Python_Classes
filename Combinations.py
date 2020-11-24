#Program that returns the number of combinations 

def factorial(n):
	"""
	Get factorial of a number
	n = int

	return int
	"""
	f = 1
	if (n < 0):
		return None
	elif (n == 0):
		return 1
	else:
		for i in range(1,n+1):
			f = f * i
		return f

def combination(d1,d2):
	"""
	Get combination of two numbers
	d1,d2 = int

	return int
	"""
	f1 = factorial(d1)
	f2 = factorial(d2)
	f3 = factorial(d1-d2)
	result = f1/(f2*f3)
	return result

print(f"5C0 = {combination(5,0)}")