from collections import Counter
import json
import re

file = open('birthdays.json', 'r+')  # r+ is used because i would like to read and write.
data = json.load(file)
print("\n\n===>Exisitng Birthday Data\n")

my_list = []

for k, v in data.items():
    print(k + " : " + v)
    x = re.findall("/\d\d/", v)[0]
    #  need to do [0] because the answer is retuerned in the form of a list.
    my_list.append(x)

print(Counter(my_list))
file.close()
