print(">>> Welcome to the birthday disctionay. We know the birthdays of : ")
file = open("birthdays.txt", "r")
data = file.readlines()

my_dict = dict()


for item in data:
    partitions = item.rpartition(" ")
    my_dict[partitions[0]] = partitions[-1]
    # 0th index will always have the name, and -1 will always have the date.
    print(partitions[0])

name = raw_input("\n>>> Who's birthday do you want to look up?\n")
try:
    print(name + "'s birthday is " + my_dict[name])
except KeyError:
    print("Name not found in data base. :O ")