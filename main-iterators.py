class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater1 = Repeater("Hello for")
count = 0
for item in repeater1:
    print(item)
    count += 1
    if count > 5:
        break

repeater2 = Repeater("Hello while")
iterator2 = repeater2.__iter__()
count = 0
while count < 5:
    item = iterator2.__next__()
    print(item)
    count += 1

iterator1 = repeater1.__iter__()
print(next(iterator1))
print(next(iterator2))
