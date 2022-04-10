
# print numbers from N to 1 

def linear(n):
    if n :
        print(n)
        linear(n-1)

linear((int(input())))
# linear(5), o/p = 5 4 3 2 1 

# order matters, it will print from 1 to N as first it will reach base condition, then move to the next line(print statement)

def linear(n):
    if n :
        linear(n-1)
        print(n)

linear((int(input())))
# linear(5), o/p = 1 2 3 4 5