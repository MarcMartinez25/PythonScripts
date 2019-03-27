# this is a small script that reverses a string

def reverse(x):
    reversed_string = ''
    for c in x:
        reversed_string = c + reversed_string
        # print(reversed_string) 
        # Uncomment print statement above to see how it works in the terminal.
        # This is helpful for understanding how to function works

    return reversed_string


# s = 'Hello World'
# print(s)
# print(reverse(s))