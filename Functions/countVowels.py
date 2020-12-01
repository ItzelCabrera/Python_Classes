txt = input("Introduce un texto: ").upper()

vowels = {"A" : 0 , "E" : 0 , "I" : 0 , "O" : 0 , "U" : 0}

for char in txt:
	for key in vowels.keys():
		if (char == key):
			vowels[key] += 1  

print("Tu texto tiene ", vowels["A"] ," A's ")
print("Tu texto tiene ", vowels["E"] ," E's ")
print("Tu texto tiene ", vowels["I"] ," I's ")
print("Tu texto tiene ", vowels["O"] ," O's ")
print("Tu texto tiene ", vowels["U"] ," U's ")