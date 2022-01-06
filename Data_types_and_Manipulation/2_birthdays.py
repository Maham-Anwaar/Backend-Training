import json

file = open('birthdays.json', 'r+')  # r+ is used because i would like to read and write.
data = json.load(file)
print("\n\nExisitng Birthday Data")

for k, v in data.items():
    print(k + " : " + v)

var = raw_input("Enter the name of the person whos birthday you want to save ")
DOB = raw_input("Enter the persons date of birth now (date/month/year) ")
data[var] = DOB
file.seek(0)  # start writing from begining of file.
json.dump(data, file, indent=2)

file.close()
