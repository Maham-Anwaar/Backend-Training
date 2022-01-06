def repack_boxes(*args):
    list_of_items = []
    total_count = 0
    for boxes in args:
        total_count += boxes.count()
        list_of_items.append(boxes.empty())

    one_list = []
    for list in list_of_items:
        for item in list:
            one_list.append(item)

    while (True):
        for box in args:
            if total_count == 0:
                return args
            box.add(one_list.pop())
            total_count -= 1


class Item:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box:

    def add():
        raise NotImplementedError()

    def empty():
        raise NotImplementedError()

    def count():
        raise NotImplementedError()

class ListBox(Box):

    def __init__(self):
        self.listOfBox = []
        self.counter = 0

    def add(self, item):
        self.listOfBox.append(item)
        self.counter += 1

    def empty(self):
        items = []
        for i in range(self.counter, 0, -1):
            items.append(self.listOfBox.pop())
        self.listOfBox = []
        self.counter = 0
        return items

    def count(self):
        return self.counter

class DictBox(Box):

    def __init__(self):
        self.dict = dict()
        self.counter = 0

    def add(self, item):
        self.dict[self.counter] = item
        self.counter += 1

    def empty(self):
        items = []
        for i in range(self.counter, 0, -1):
            items.append(self.dict.popitem())
        self.counter = 0
        return items

    def count(self):
        return self.counter


x = ListBox()
y = ListBox()
a = DictBox()
for i in range(1, 21):
    x.add(Item(str(i), i))

for i in range(1, 10):
    y.add(Item(str(i), i))

for i in range(1, 6):
    a.add(Item(str(i), i))

print("\n--> Before Distribution")
print(x.count())
print(y.count())
print(a.count())


x, y, a = repack_boxes(x, y, a)

print("\n--> After Distribution")
print(x.count())
print(y.count())
print(a.count())
