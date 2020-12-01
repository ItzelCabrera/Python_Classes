"""Function that counts bobs"""

def countBobs(txt):
	"""Function tha counts how many "bob" strings are in the sentence
	txt = string

	return: int
	"""
	c = 0
	txt = txt.upper()

	for i in range(len(txt)):
		k = i + 3
		if (txt.find("BOB",i,k) != (-1) ):
			c+=1

	return c

txt = "Bobob. Bob is a good person, I like Bo. bOb"

print(f"Your text has {countBobs(txt)} BOB´S")