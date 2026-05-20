#First Solution
def two_sort(array):
    array.sort()
    first = array[0]
    word = list(first)
    joined_word = "***".join(word)
    return joined_word  

Refactored Final Solution
def two_sort(array):
    array.sort(0)
    return "***".join(array[0])