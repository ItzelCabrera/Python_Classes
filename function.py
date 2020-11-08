"""Function class"""

def hello(name = "person", lastname = "exposito"):
	"""Function that prints "hello world!"""
	"""print("Hello world!")"""
	return f"Hello {name} {lastname}!"

variable1 = input("Ingresa tu nombre___")

string = hello(variable1)
print(string)