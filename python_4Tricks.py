
x = [1,2,3]
y=[4,5]
x.append(y) # append add the argument as single element to the end of given list
print(x) 


x = [1,2,3]
y=[4,5]
x.extend(y)
print(x) #extend iterates over the argument and adds each element to the list


def gen_yield():
    yield "hel"
    yield "lo"
    yield "worl"
    yield "d!!"
    
def func_return():
    return "hel"
    return "lo"
    return "worl"
    return "d!!"  
   
"""
yield sends value back to the caller, but maintains function state, next time function is called it continues
from the point it finished

"""
for value in gen_yield():
    print(value, end="")
    
for value in func_return():
    print(value, end="")
    
    
generator = (x for x in [1,2,3])

for _ in generator:
    print(_,end=" ")

    
    
results = [(0.1,0.2),(0.3,0.4),(0.2,0.4)]
print(list(map(lambda x: x[0], results)))