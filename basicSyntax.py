class Classy(object):
    def __init__(self):
        self.items = []

    def add_item(self, input):
        self.items.append(input)

    def get_classiness(self):
        return self.items.__len__()


me = Classy()

print(me.get_classiness())

me.add_item("tophat")

print(me.get_classiness())

me.add_item("bowtie")
me.add_item("jacket")
me.add_item("monocle")

print(me.get_classiness())

me.add_item("bowtie")

print(me.get_classiness())
