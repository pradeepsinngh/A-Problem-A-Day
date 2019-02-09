# Write a function g_content(s) with input a DNA-string and returns the GC-content of the string.

def gc_content(string):
    '''
    Returns the percentage of GC content in DNA-string.

    Input: String (eg: GTAGCTAGTGTGCA)
    Output: Float (eg: 0.5)
    '''
    # To count 'GC' content
    count = 0

    # count 'GC' content
    # if item = 'G' or 'C', add 1 to count
    for item in string:
        if item == 'C' or item == 'G':
            count += 1
        else:
            count = count

    str_len = len(string)

    # calculate proportion of GC content
    gc_content = count/ str_len

    return gc_content
