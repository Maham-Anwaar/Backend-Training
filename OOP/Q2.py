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
        self.listOfBox = []
        self.counter = 0

    def count(self):
        return self.counter

class DictBox(Box):

    def __init__(self):
        self.dict = dict()
        self.counter = 0

    def add(self, item):
        self.dict[item.name] = item.value
        self.counter += 1

    def empty(self):
        self.dict = dict()
        self.counter = 0

    def count(self):
        return self.counter


x = ListBox()
y = Item("ball", 5)
x.add(y)
x.add(y)
x.empty()
x.add(y)
print(x.count())

a = DictBox()
a.add(y)
a.add(y)
a.add(y)
print(a.count())