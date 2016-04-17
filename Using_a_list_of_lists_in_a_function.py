# Let's concatenate lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]


def flatten(lists):
    results = []
    for numbers in lists:
        for numb in numbers:
            results.append(numb)
    print results


print flatten(n)
