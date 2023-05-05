# You are given a list of strings. Write a function that takes in the list and returns a dictionary that maps each string to its length.
# Example:
# Input: [‘hello’, ‘world’, ‘python’]
# Output: {‘hello’: 5, ‘world’: 5, ‘python’: 6}


def compiler(string_list):
    my_dict = {}
    for word in string_list:
        my_dict[word] = len(word)
    return (my_dict)


my_list = ['hello', 'world', 'python', 'goodbye']

print(compiler(my_list))
