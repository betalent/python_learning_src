def pair(x,y):
    return (x,y)

def diff(x):
    return x[0]!=x[1]
    
print "MAP ", map(pair, [1,'a',2,3], [1,3,4,5])

print "FILTER AND MAP ", filter(diff, map(pair, [1,'a',2,3], [1,3,4,5]))

print "LAMBDA ", filter(lambda x: x[0]!=x[1], map(lambda x,y: (x,y), [1,'a',2,3],[1,3,4,5]))