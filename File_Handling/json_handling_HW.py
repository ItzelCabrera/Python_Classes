
import json

data_as_json = [
    {'id': 1, 'student_name': 'Pablito Mix', 'birth_month': 'November', 'career': 'DJ'},
    {'student_name': 'JBalvin', 'birth_month': 'January', 'career': 'musician'},
    {'id':76, 'student_name': 'Toño', 'career': 'stalker'},
    {'student_name': 'Edgar'},
    {'id':76.0, 'student_name': 'Adal', 'career': 'stalker'},
    {'id': 8},
    {'id': 35, 'student_name': 'Santiaguito', 'birth_month': 'December'},
    {'id': 8.0, 'student_name': 'DieGOL Maradona', 'career': 'soccer player'},
    {'id': 1, 'student_name': 'Pelé'},
    {'id': 'hji', 'student_name': 'Brad Pitt', 'birth_month': 'May', 'career': 'actor'}
]

new_data = {
	'personitas':[]
}

ID_record = [

] 

for elem in data_as_json:
	if (('id' in elem) and ('student_name' in elem)):
		if((type(elem['id']) == int) or (type(elem['id']) == float)):
			#print(f"{elem['id']} --> {type(elem['id'])}")
			if (elem['id'] not in ID_record):
				ID_record.append(elem['id'])
				new_data['personitas'].append(elem)
			

#print(new_data)
#print(ID_record)

with open("personitas.json",mode = "w") as json_file:
	print("Opened file")
	json.dump(new_data,json_file,indent=4)
	print("Wrote file")

with open("personitas.json",mode = "r") as json_file:
	print("Opened file")
	data = json.load(json_file) #read the JSON file and create a dictionary named "data"
	for elem in data.values():
		for e in elem:
			for k in e.keys():
				print(f"{k}: {e[k]}",end = " / ")
			print("\n")

	print("Read file")


"""
SERIALIZATION: converting an object into a JSON string (dumps,dump)
DESERIALIZATION: converting a JSON string into an object (loads,load)
j = json.dumps(new_data,indent = <number>,sort_keys = <T/F>) --> <dumps> convert an object to a JSON string
json.loads(<JSON_string>) --> convert a string with the JSON format to a Python dictionary"""