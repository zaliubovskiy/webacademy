# In this mission you should check if all elements in the given list are equal.
# Input: List.
# Output: Bool.

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    for i in elements:
        for j in elements[1:]:  # Checks all the elements except the first one
            if i != j:
                return False  # If not the same, "False" and quit
    return True


print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same([]))
print(all_the_same([1]))
