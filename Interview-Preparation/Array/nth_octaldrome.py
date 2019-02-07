def nth_octaldrome(n):
    '''
    Returns the nth positive palindrome in it's octal representation.

    Input: n (a positive number)
    Output:
    '''

    # list to store palindrome in it's octal form.
    octaldrome = []
    num = 1

    def isPalindrome(m):
        '''
        Given a list of numbers, check if it is palindrome or not.
        If given list is palindrome return True, else False.
        '''

        for i in range(0,int(len(m)/2)):
            if m[i] != m[len(m)-i-1]:
                return False
        return True

    while len(octaldrome) <= n:

        # To store individual digits
        octal = []
        number = num

        # Traversing all digits.
        # Convert into octal and append in octal list.
        while (number != 0):
            octal.append(number % 8)
            number = int(number / 8)

        # checking if octal no is palindrome.
        # If true, append it's orginal number into octaldrome.
        if isPalindrome(octal) == True:
            octaldrome.append(num)

        num += 1

    return octaldrome[n-1]
