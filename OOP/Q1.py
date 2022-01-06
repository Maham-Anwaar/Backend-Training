import re

my_list = [
    ("Maham", "mahamgmail.com", -23),
    ("Alex", "alex.pleb.com", 16),
    ("Hitler", "nazi@germany.com", 3),
    ("Stalin", "mahamgmail.com", 23),
    ("Maham", "duplicate@gmail.com", 23),
    ("Pewds", "notduplicate@gmail.com", 23),
]

# adds each user to a directory if the user is at least 16 years old. You do not need to store the age


def validateEmail(email):
    x = re.findall("\w+@\w+.com", email)
    if not x:
        return False
    return True


def insertUserName(dict, name, email):
    try:
        dict[name] = email
    except KeyError:
        return False
    return True

# Think about where else it would be a good idea to use a custom class, and
# what kind of collection type would be most appropriate for your directory.


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"Name {self.name}"


# I didnot feel the need to make multiple Exception Classes :)
class CustomException(BaseException):
    message = "Found Invalid "

    def __init__(self, var):
        message = self.message + var
        print(message)


dict = dict()
myUserList = []

for tuple in my_list:
    try:
        if tuple[-1] < 16:
            raise CustomException("Age " + str(tuple[-1]))
        if not validateEmail(tuple[1]):
            raise CustomException("Email " + tuple[1])
        if tuple[0] in dict:
            raise CustomException("Username - it already exists")
    except CustomException:
        continue
    dict[tuple[0]] = tuple[1]
    myUserList.append(User(tuple[0], tuple[1]))


print("\n\n===> VALID USERS ARE: \n")
for user in myUserList:
    print(user)
