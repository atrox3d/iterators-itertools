# https://dbader.org/blog/python-iterators

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


class BoundedRepeater(Repeater):
    def __init__(self, value, max):
        super().__init__(value)
        self.max = max
        self.count = 0

    # def __iter__(self):

    def __next__(self):
        if self.count >= self.max:
            raise StopIteration
        self.count += 1
        return self.value


repeater1 = BoundedRepeater("Hello for", 5)
# count = 0
for item in repeater1:
    print(item)
    # count += 1
    # if count > 5:
    #     break

repeater2 = BoundedRepeater("Hello while", 5)
iterator2 = repeater2.__iter__()
# count = 0
while True:
    try:
        item = iterator2.__next__()
        print(item)
        # count += 1
    except StopIteration:
        break


repeater1.count = 0
iterator1 = repeater1.__iter__()
repeater2.count = 0
print(next(iterator1))
print(next(iterator2))
