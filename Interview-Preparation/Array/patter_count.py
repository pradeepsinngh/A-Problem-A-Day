# Write a function, pattern_count with two arguments. The first arguments is a string,
# lets call it text, and the second argument is also a string, call it pattern.
# The function pattern_count returns the number of times the pattern occurs in the text.

def pattern_count(text, pattern):
    '''
    Returns the number of times the pattern occurs in the given text.

    Input: String1 (text), String2 (pattern)
    Output: int
    '''

    text_len = len(text)
    str_len = len(pattern)
    count = 0

    for i in range(text_len):
        if text[i:i+str_len] == pattern:
            count += 1

    return count
