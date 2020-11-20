#1.2 Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()
def myfilter(func,num):
    x=[]
    for i in num:
        result=func(i)
        x.append(result)
    return x
l = [ 4, 4, 5, 98766, 45, 77, 89, 33, 22, 68, 100, 110]
def new_func(a):
    if a%2==0:
      return True
    else:
        return False
list(myfilter(new_func,l))



