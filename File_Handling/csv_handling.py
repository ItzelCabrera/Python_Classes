import csv

with open("persons_data.csv",mode = "w") as csv_file:
	fieldnames_lst = ["id","name","birthday_month","career"]

	#writer es un objeto que se deberá trabajar con diccionarios (debido al DictWriter)
	writer = csv.DictWriter(csv_file,fieldnames = fieldnames_lst) 
	writer.writeheader()

	writer.writerow({"id":1, "name":"Itzel","birthday_month":"October","career":"telemathics"})
	writer.writerow({"name":"Adal","career":"mecatronics"})

with open("persons_data.csv",mode = "r") as csv_file:
	"""
	reader es un objeto que se forma de una lista de diccionarios (cada renglón es un diccionario)
	donde cada key es un elemento del header
	"""
	reader = csv.DictReader(csv_file) 
	line_counter = 0

	for row in reader: 
		if line_counter == 0:
			print(f'Columns are {",".join(row)}')	#mis keys del row los junto
			
		print(f'\nName = {row["name"]}\tID = {row["career"]}\tBirthday = {row["birthday_month"]}')
		line_counter += 1

	print(f"\nProcessed {line_counter} lines")







