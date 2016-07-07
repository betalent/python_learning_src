class ClassePadre:
    
    __variabile_esterna = "ESTERNA"
    
    def __init__(self):
        "Costruttore"
        self.variabile_init = "variabile in init"
        print "istanzio"
        
    def __del__(self):
        "Distruttore"
#        print ' '
#        print "DESTROY INIT: " + self.variabile_init
#        print "DESTROY esterna: " + self.variabile_esterna
        
    def modifica_var_init(self):
        print ' '
        print "Var INIT: " + self.variabile_init
        self.variabile_init = 'VAR_INIT_modificata'
        print "Var INIT: " + self.variabile_init
        
    def modifica_var_esterna(self):
        print ' '
        print "Var esterna: " + self.__variabile_esterna
        self.variabile_esterna = 'ESTERNA_MODIFICATA'
        print "Var esterna: " + self.__variabile_esterna
        
    def creo_new_variabile(self):
        print ' '
        self.nuova_var = 'nuova_var'
        
    def leggo_new_variabile(self):
        print ' '
        print self.nuova_var
        

class ClasseFiglio(ClassePadre):
    
    def print_figlio(self):
        print "Ciao sono il figlio"
        
c = ClassePadre()
c.modifica_var_esterna()
c.__variabile_esterna = "NUMERO"
print c.__variabile_esterna
print c._ClassePadre__variabile_esterna
c._ClassePadre__variabile_esterna = "Sei un"
print c._ClassePadre__variabile_esterna

# obj = ClassePadre()
# obj.modifica_var_init()
# obj.modifica_var_esterna()
# obj.creo_new_variabile()
# print "DA FUORI: " + obj.nuova_var
# print "DA FUORI: " + obj.nuova_var
# obj.nuova_var2 = "ciao fuorissimo"
# print "DA FUORI: " + obj.nuova_var2

# print "CON GETATTR: " + getattr(obj, "nuova_var")