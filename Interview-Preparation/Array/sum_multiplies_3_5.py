# Write a function, sum_multiples_3_5, that returns the sum of the multiples of 3 and 5 less than N.

def sum_multiplies_3_5(N):
    '''
    Returns the sum of the multiples of 3 and 5 less than N.

    Input: int (N)
    Output: int
    '''

    num = 1
    total_sum = 0

    # check if sum is less than N
    while (total_sum + num) < N:

        # If num multiples with 3 and 5, add it to sum
        if num % 3 == 0 and num % 5 == 0:
            num += 1
            continue
        elif num % 3 == 0 or num % 5 == 0:
            total_sum = total_sum + num

        num += 1

    return total_sum
