# Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number
# of times they appear in elements. If two elements have the same frequency, they should end up in the same
# order as the first appearance in the iterable.

def frequency_sort(items):
    # Sorting by index first:
    sorted_by_index = sorted(items, key=lambda i: items.index(i))

    # Sorting by frequency (descending):
    sorted_by_frequency = sorted(sorted_by_index, key=lambda i: sorted_by_index.count(i), reverse=True)
    return sorted_by_frequency


print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))
print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
