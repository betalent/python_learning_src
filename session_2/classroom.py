from inspect import isfunction
import types

def stampa (a,b=21,c=22):
    print "c" + str(c)
    return "True"
    
valore = stampa ("ciao")
valore = stampa ("c",c=24)
valore = stampa ("sucaiao",23,24)


def superstampa (var1, *others):
    print var1
    for i in others:
        print i
        
superstampa ("a", "b", "c", "d", 2)

def fun_1():
    return "fun1"
    
def fun_2():
    return "fun2"
    
def pass_function (var1, *func):
    print var1
    for i in func:
        if isinstance(i, types.FunctionType):
            print "qua siamo"
        if isfunction(i):
            print i()
        else:
            print i
        
pass_function ("ciao", fun_1, fun_2, "c")
    
### ###
    
total = 1
def esegui (total):
    total+=1
    print "CON " + str(total)

def esegui_senza_arg():
    global total
    total = 0
    print "SENZA " + str(total)
    

print ""
print total
esegui(total)
print total
esegui_senza_arg()
print total


lista = ['a']
#pass by reference   
def printlista(lista):
    lista = ['b'] # This would assign new reference in mylist
    print 'IN ', lista

#pass by reference   
def printlista_bis(lista):
    lista.append('b')
    print 'IN ', lista
    
printlista(lista)
print 'OUT ', lista
print " "
printlista_bis(lista)
print 'OUT ', lista
