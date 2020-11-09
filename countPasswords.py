"""Program that counts the possible distribution of characters for a password"""
from itertools import combinations
import constantes

def combinate(lst,n):
	"""
	Combinate a list
	lst = list
	n = int

	return tuple
	"""
	c = combinations(lst,n)
	return c

def getCombinationsIntoList(t,n_char_to_d):
	"""
	Get combinations into a list
	t = tuple

	return list
	"""
	c = 0

	lst = []

	for e in list(t):
		c+=1
		#print(e)
		lst.append(list(e))
	print(f"There are {c} possible ways to distribute the other {n_char_to_d } characters")

	return lst

def getColumns(lst):
	"""
	Counts how many cols are on the matrix
	lst = list

	return int
	"""
	c = 0

	for e in lst:
		c+=1

	return c

def printList(l):
	"""
	Prints a list
	l = list

	return None
	"""
	c = 0

	for e in l:
		c+=1
		print(f"{c} .- {e}")

def getDistributions(lst,n_elem):
	"""
	Determines the distribution of each type (M,m,d,c)
	lst = list

	return list
	"""
	#create a second list to save the real distributions
	l = [ [0 for i in range(4)] for j in range(getColumns(lst)) ]

	counter = 0
	k = 0
	j = 0
	z = 0

	for r in lst:
		for c in range(len(r)):
			if (c == 0):
				l[counter][c] = r[c]
			elif (c == 1):
				k = c - 1
				l[counter][c] = r[c] - r[k]
			else:
				j = c - 1
				l[counter][c] = r[c] - r[j]
				z = c + 1
				l[counter][z] = n_elem - (l[counter][0] + l[counter][1] + l[counter][2])

		counter += 1	
	return l

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

def P(N,X,Y,Z,T):
	"""
	Get a permutation of dufferent type of objects
	n = int
	X = int
	Y = int
	Z = int
	T = int

	return int
	"""
	i = 0
	n = factorial(N)
	x = factorial(X)
	y = factorial(Y)
	z = factorial(Z)
	t = factorial(T)

	mayus = factorial(constantes.N_MAYUS) / factorial(constantes.N_MAYUS - X)
	minus = factorial(constantes.N_MINUS) / factorial(constantes.N_MINUS - Y)
	dig = factorial(constantes.N_DIG) / factorial(constantes.N_DIG - Z)
	characters = factorial(constantes.N_CHAR) / factorial(constantes.N_CHAR - T)

	w = x*y*z*t
	i = (n/w) * mayus * minus * dig * characters

	return i

def listOfPermutations(n,l,col):
	"""
	Get a list of the permutations of n objects that are different between them
	n = int
	l = list
	c = int

	return list
	"""
	X = 0
	Y = 0
	Z = 0
	T = 0

	i = 0
	counter = 0
	lst = [0 for j in range(col)]

	for elem in l:
		for c in range(len(elem)):
			if (c == 0):
				X = elem[c]
			elif (c == 1):
				Y = elem[c]
			elif (c == 2):
				Z = elem[c]
			else:
				T = elem[c]
		i = P(n,X,Y,Z,T)
		lst[counter] = i	
		counter += 1
	return lst

def result(l):
	"""
	Sum elements of a list
	l = list

	return int
	"""
	c = 0.0
	for elem in l:
		c += elem

	return c

def resultL(lst_0and1,n_elem,n_char_to_d):
	"""
	Sum possible ways to build a password with n_elems characters 
	lst_0and1 = list
	n_char_to_d = int
	n_elem = int

	return int
	"""
	#Encuentran el numero de formas de acomodar los caracteres restantes (Sin cosiderar los 4 obligatorios [1M,1m,1d,1c])
	comb = combinate(lst_0and1,constantes.N)

	#Convierte las tuplas a una matriz para su fácil manejo
	lst = getCombinationsIntoList(comb,n_char_to_d)

	#number of columns
	j = getColumns(lst)

	#Cambia la lista para que indique el no. de "M", de "m", de "d" y de "c"
	lst = getDistributions(lst,n_elem)

	#printList(lst)

	#genera una lista con los resultados de las permutaciones individuales
	lst = listOfPermutations(n_elem,lst,j)

	#printList(lst)

	return result(lst)

"""
Main

LST_0AND1 =  list of posible positions to accomodate the one´s
N_CHAR_TO_D = characters to know what type of classification they are
N_ELEM_1 = lenght of the password

"""
print("\n\n")

#For passwords with 8 characters
LST_0AND1_1 = [1,2,3,4,5,6,7] 
N_CHAR_TO_D_1 = 4 #characters left to know what type they are
N_ELEM_1 = 8 #lenght of the password
P1 = resultL(LST_0AND1_1,N_ELEM_1,N_CHAR_TO_D_1)
print(f"Possible passwords with {N_ELEM_1} characters = {P1}")

print("\n\n")

#For passwords with 9 characters
LST_0AND1_2 = [1,2,3,4,5,6,7,8] 
N_CHAR_TO_D_2 = 5 #characters left to know what type they are
N_ELEM_2 = 9 #lenght of the password
P2 = resultL(LST_0AND1_2,N_ELEM_2,N_CHAR_TO_D_2)
print(f"Possible passwords with {N_ELEM_2} characters = {P2} ")

print("\n\n")

#For passwords with 10 characters
LST_0AND1_3 = [1,2,3,4,5,6,7,8,9] 
N_CHAR_TO_D_3 = 6 #characters left to know what type they are
N_ELEM_3 = 10 #lenght of the password
P3 = resultL(LST_0AND1_3,N_ELEM_3,N_CHAR_TO_D_3)
print(f"Possible passwords with {N_ELEM_3} characters = {P3} ")

print("\n\n")


P = P1 + P2 + P3
print(f"Total = {P} possible ways to build a password")

print("\n\n")

Time = P * (1/1000000) * (1/60) * (1/60) * (1/24) * (1/365)
print(f"Total of time to check all passwords = {Time} years!")