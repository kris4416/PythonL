# importing futures
from concurrent import futures

data = range(100)


def func(value):
    return value**value


with futures.ProcessPoolExecutor as executor:
    result = executor.map(func, data)

for i in result:
    print(i)
