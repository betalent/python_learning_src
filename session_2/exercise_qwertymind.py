#PangramCheck
#
#-- About --
#
#A pangram is a sentence that contains all the letters of the English alphabet at least once.
#
#For example, the quick brown fox jumps over the lazy dog.
#
#-- Task --
#
#Write a function or method to check a sentence to see if it is a pangram (or not) and show its use. 

def is_pangram_simple(stringa):
    alfabeto = 'qwertyuiopasdfghjklzxcvbnm'
    
    for lettera in alfabeto:
        if lettera in stringa.lower():
            continue
        else:
            print "La stringa non e' un pangram"
            return
            
    print "La stringa " + stringa + "e' un pangram"



# print "\n-1-\n"
    
# is_pangram_simple('ciao')

# print "-----"

# is_pangram_simple('azWsxEdcRfvTgbYhnujmikolp')

# print "-----"

# is_pangram_simple('QazWsxEd cRfvTgbY hnujmikolp')

# print "-----"

# is_pangram_simple('QazWsxEdcRfvTgbYhnujmikolp')

# print "-----"

# is_pangram_simple('QazWsxEdcRfvTg bYhnujmikolp')
