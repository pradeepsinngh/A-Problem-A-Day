def print_full_name(a, b):
    print (("Hello %s %s! You just delved into python.") % (a, b))
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
