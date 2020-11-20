#Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()
def myreduce(func,num) :#The function reduce(function, sequence)
        result = num[0]
        for i in num[1:]:
            result = func(result, i)
        return result
def fuc(a, b):
    return a + b
l = [2, 5, 6, 1, 8, 3, 10]
z=(myreduce(fuc, l))
print("My Reduce Output is:",z)

