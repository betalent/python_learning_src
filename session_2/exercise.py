#PangramCheck
#
#-- About --
#
# A pangram is a sentence that contains all the letters of the English alphabet at least once.

# For example, the quick brown fox jumps over the lazy dog.

# -- Task --

# Write a function or method to check a sentence to see if it is a pangram (or not) and show its use. 


english_alphabet = 'qwerty'

def is_pangram(text):
    for lettera in english_alphabet:
        if lettera not in text.lower():
            return False
    return True

def start_test():
    rimani = True
    while rimani:
        testo = raw_input("Scrivi frase (0 to exit): ")
        if testo == '0':
            rimani = False
        else:
            result = is_pangram(testo)
            if result:
                print "La stringa " + testo + " e' un pangram"
            else:
                print "Ops, non e' un pangram"

start_test()
