# Program to sort given n numbers
import random


def n_sort(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            array[i], array[j] = (array[i], array[j]) if (array[i] <= array[j]) else (array[j], array[i])
    return array


if __name__ == "__main__":
    random.seed(1)
    array = [random.randrange(20) for i in range(100)]
    print(array)
    print(n_sort(array))
