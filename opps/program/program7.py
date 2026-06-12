# decorators.py
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer
def compute(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(compute(1000000))





# iterator.py
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for x in ReverseIterator([1,2,3,4]):
    print(x)  # 4 3 2 1
