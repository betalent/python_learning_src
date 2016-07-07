#List Comprehensions, Functional Programming Tools(filter,map,reduce)
import random
array = [1,2,3,4,5,6,7,8,9,0]
array_nano = [2,3,4]

def f(x):
    return True

def m(x):
    return random.randint(1,100)

def r(x,y):
    print x, " ", y
    return x*y

print filter(f,array)
print map(m,array)
print reduce(r,array_nano)


def square(x):
    return x**2

#print [x**2 for x in range(10)]
#print map(square,range(10))




def mp(x):
    return tuple(x[0],x[1])


#data = [(x, y) for x in a for y in b]

a = [1,'a',2,3]
b = [2,3,4,5]


# map(FUNCTION, SEQUENCE)

#PYTHON
a = []
for x in a:
    for y in b:
        if x!=y:
            a.append((x,y)) 

#LIST COMPREHENSION            
print [(x, y) for x in a for y in b if x != y]

a = [1,'a',2,3]
b = [2,3,4,5]


def fl(x):
    return x[0]!=x[1]
    
#MAP REDUCE
print filter(fl, map(lambda x,y:(x,y), a,b))

#PYTHON BIS
#map
vector = []
for x in a:
    for y in b:
        vector.append((x,y)) 
#filter
for key,value in enumerate(vector):
    if value[0]==value[1]:
        vector.pop(key)
        


print filter(lambda x:x[0]!=x[1], map(lambda x,y:(x,y), a,b))
 

###### map(lambda x,y:(x,y), a,b)

def mp2(x,y):
    return (x,y)
    

elem = lambda x,t,s: "HELLO"

print elem(1,2,3)


print filter(lambda x:x[0]!=x[1], map(mp2, a,b))
