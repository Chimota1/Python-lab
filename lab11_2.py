class ItCountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        else:
            value = self.start
            self.start -= 1
            return value

c = ItCountDown(5)
for i in c:
    print(i)
print(list(ItCountDown(3)))
print(list(ItCountDown(0)))
print(list(ItCountDown(-2)))