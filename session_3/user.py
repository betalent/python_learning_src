from classroom import ClassePadre

c = ClassePadre()
print c
c.modifica_var_init()

print hasattr(c, "variabile_esterna")

c.variabile_init = "davide"
print "Var_init: " + c.variabile_init

c.creo_new_variabile()
c.leggo_new_variabile()
c.nuova_var = "modificata"
print "Var_init: " + c.nuova_var
c.leggo_new_variabile()

