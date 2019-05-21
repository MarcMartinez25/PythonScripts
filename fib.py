# this is a function that prints the first n number of the fibonacci sequence

def fib(n):
  a = 1
  b = 1
  for num in range(n):
    c = a + b
    print(c)
    a = b
    b = c

fib(10)
