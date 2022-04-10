# Calculate sum of first n integers

# paramterized method - changing the parameter to calculate 
# def summation(i, sum_):
#     if i < 1:
#         print(sum_)
#         return 
#     summation(i-1, sum_+ i)

# summation(5,0)


# functional method - using the functions to calculate 
def summation(n):
    if n == 0:
        return 0 
    sum_ = n + summation(n-1)
    
    return sum_

print(summation(5))



# factorial of n 

# functional method 
# def fact(n):
#     if n == 1 :
#         return 1 
#     return n * fact(n-1)

# print(fact(5))
# # o/p = 120 


# parameterized method
def factorial(i, fact):
    if i < 1:
        print(fact)
        return 
    factorial(i-1, fact*i)

factorial(5,1)

