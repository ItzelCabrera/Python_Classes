"""FILE HANDLING
	Text file's mode:
		w - write
		r -read
		a - append
		r+ - read and write
		x - creation mode
	Binary file's mode:
		wb - write
		rb -read
		ab - append
		rb+ - read and write
"""

""" WORK WITHOUT WITH/AS
my_file = open("data.txt","r") 
print(my_file.read())
must close the source
"""

""" READ A TEXT FILE
with open("data.txt","r") as data:
	print(f"File name : {data}")
	print(data.read()) #->todas las líneas
	#print(data.read())--> lee solo una línea
	#print(data.readlines()) -> lista con todas las líneas que trae el texto(con \n)
	#for line in data:{} -> iteración de las lineas
"""

""" WRITE IN A TEXT FILE
lines = ["Line 6","Line 7","Line 8"] #lines to append

with open("data.txt","r+") as data: #create a list with the lines readed
	data_list= data.readlines()

data_list.insert(3,"Line between 3 and 4\n") #insert a new element in the list of lines

with open("data.txt","w+") as data: #overwrites the file
	data_string = "".join(data_list) #convert the list to a string
	data.write(data_string)			#write the string to the file

with open("data.txt","a+") as data:	#append lines
	for line in lines:
		data.write(line)	#append each line
		data.write("\n")

"""

"""WRITE / READ IN BINARY FILES """
lines = [b"Line 5",b"Line 6",b"Line 7"]

with open("data.docx","rb") as bData:
	data_list = bData.readlines() #create a list of lines readed

data_list.insert(1,b"Line between 1 and 2\n") #insert an element in the position [1]

with open("Data.docx","wb") as bData:
	for line in data_list:	
		bData.write(line)	#write each element of the list
	for line_element in lines:
		bData.write(line_element)	#write lines = [b"Line 5",b"Line 6",b"Line 7"]
		bData.write(b"\n")




