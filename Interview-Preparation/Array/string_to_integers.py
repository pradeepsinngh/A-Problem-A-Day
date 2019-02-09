# Write a function that receives a collection of strings and a map from strings to integers.
# Return a collection of integers that are values of the map corresponding to one of the strings
# in the collection.

def string_to_integers(s,t):
    '''
    Return a list of integers that are values of the map corresponding to
    one of the strings in the collection.

    Input: List (of strings), dict{strings:integers)
    Output: List (of integers)
    '''

    # To store integers that are values of the strings in the array.
    lst = []
    len_str = len(s)

    # If string in dict (key) is in list, add corresponding dict value to list
    for i in range(0,len_str):
        j = t.get(s[i])

        if j != None:
            lst.append(j)

    return lst
