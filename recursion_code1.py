
#recursion code 1 

class rec:
    def __init__(self,count):
        self.count = count  
        self.t =  count + 4

    def f(self):
        if self.count == self.t:
            return 
        print(self.count)
        self.count += 1 
        self.f()

c = int(input("Enter a number "))
p = rec(c)
print(p.f())


# OR

# backtracking

def linear(n) :
    if n:
        linear(n-1)
        print(n, end = ' ')
    return 
n = int(input())
linear(n)