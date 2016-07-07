try:
   '''Tentativo di esecuzione senza scollo'''
   fh = open('testfile.txt', 'r')
   fh.write("This is my test file for exception handling!!")
except IOError, ex:
   '''eseguito solo se c\'e\' eccezione'''
   print "Message: " + ex.message
   print "Error: can\'t find file or read data"
else:
   '''Eseguita solo se non c'\' eccezione'''
   print "Written content in the file successfully"
finally:
   '''Tentativo di esecuzione con scollo'''
   print "Alla Fine: ciao ciao sempre e comunque"