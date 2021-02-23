# You are given a string and two markers (the initial and final).
# You have to find a substring enclosed between these two markers. But there are a few important conditions:
#
# https://py.checkio.org/en/mission/between-markers/

def between_markers(text: str, begin: str, end: str) -> str:
    first_index = text.find(begin)  # Finds the first index of the slice
    second_index = text.find(end)  # Finds the second index of the slice
    if first_index != -1:  # Checks if the "begin" in the "text"
        first_index += len(begin)  # Makes a step of the length, in order to print the correct output
    else:
        first_index = 0  # If the first index is not found, begin from 0
    if second_index == -1:  # Checks if the "end" in the "text"
        second_index = len(text)  # If it is not in the text, then prints everything till the end
    return text[first_index:second_index]  # Make slice "Between markers"


print(between_markers('What is >apple<', '>', '<'))
