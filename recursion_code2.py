# Print name n times 

def p(n):
    if n:
        p(n-1)
        print("shivam")
    return 


p(int(input()))



# OR

def name(n, i = 1):
    print("shivam")
    if i == n:
        return
    name(n-1)

i = int(input())
name(i)

