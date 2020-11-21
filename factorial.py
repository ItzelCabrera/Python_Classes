
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

print(1- ( (364/365)**23) )