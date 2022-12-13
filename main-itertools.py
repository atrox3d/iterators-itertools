# https://realpython.com/python-itertools/#what-is-itertools-and-why-should-you-use-it
import itertools as it


def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [
        tuple(
            inputs[
                i*n:(i+1)*n
            ]
        ) for i in range(num_groups)
    ]


def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)


def better_grouper_ext(inputs, n):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters)


for x, y  in zip(['a', 'b', 'c', 'd'], it.cycle([1, 2, 3])):
    print(x, y)

