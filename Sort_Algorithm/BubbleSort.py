"""Programa usando Bubble Sort"""
def changePos(lst,e):
	lst[e],lst[e+1] = lst[e+1],lst[e]
	return lst

lst = [6,5,3,1,8,7,2,4]

c = 1 	#c = limite para comparar
k = 1 	#k = cambios
j = -1	#j = índices por comparar


while(k > 0):
	k = 0
	for i in range(len(lst)-c): #num de comparaciones
		j +=1
		if (lst[j] > lst[j+1]):
			lst = changePos(lst,j)
			k +=1
			print(lst)
		
	j = -1
	c += 1

print(f"Lista ordenada: {lst}")