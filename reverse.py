# this is a small script that reverses a string

def reverse(x):
    reversed_string = ''
    for c in x:
        reversed_string = c + reversed_string
        print(reversed_string)

    return reversed_string


# s = 'Hello World'
# print(s)
# print(reverse(s))