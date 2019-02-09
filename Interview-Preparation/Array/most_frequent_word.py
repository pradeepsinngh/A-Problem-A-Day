# Write a function, most_frequent_word, which has two arguments. The first argument is a
# string, the second argument is an integer, call it n. most_frequent_word returns the sequence
# word(s) of length n that occurs most in the string.

def most_frequent_word(string,n):
    '''
    Returns words of length n that occurs most in the string.

    Input: String, int
    Output: list (of words)
    '''

    str_len = len(string)
    # dict to store most freq words of lenght n
    counter = {}

    for i in range(str_len):
        if string[i:i+n] not in counter:
            counter[string[i:i+n]] = 1
        else:
            counter[string[i:i+n]] += 1

    # store most freq words only of lenght n, list comprehension.
    freq_word = [k for (k,v) in counter.items() if v == max(counter.values())]

    return (freq_word)
