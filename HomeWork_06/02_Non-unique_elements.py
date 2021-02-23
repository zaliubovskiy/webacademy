# You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the
# non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained
# in a given list only once). When solving this task, do not change the order of the list.
# Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
# https://py.checkio.org/en/mission/non-unique-elements/

def checkio(data: list) -> list:
    non_unique = []
    for i in data:
        if data.count(i) != 1:  # Checks if the element is unique. If not, appends it to the empty list
            non_unique.append(i)
    return non_unique


print(checkio([1, 2, 3, 1, 3]))