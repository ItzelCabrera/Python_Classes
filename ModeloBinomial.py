
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

def P_binomial(n,kS,kE,p):
	"""
	Obtiene la probabilidad de un modelo binomial
	n = numero de pruebas
	kS = numero de éxitos 
	kE = numero de éxitos
	OBS: para cuando se va a ser una sumatoria--> kS es el inicio y kE es el final
	p = probabilidad del éxito

	return float
	"""
	q = 1 - p #probabilidad del fail
	print(f"q = {q}")
	R = 0 #resultado
	c = 0 #contador

	if (kS == kE):
		R = (p**kS) * (combination(n,kS)) * (q**(n-kS))

	for i in range(kS,kE+1):
		c +=1
		R = R + ( (p**i) * (combination(n,i)) * (q**(n-i)) )
		print(f"{c} Resultado = {R}")

	print(f"Resultado = {R}")
	return R

print(f"\nb(16,0,2,0.5) = {P_binomial(15,10,15,0.2)}")

