def is_pangram(word):
    my_list = []
    new_word = []
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for c in word.lower():
        if c != ' ': #elimino gli spazi
            new_word.append(c)
    
    new_word_sorted = sorted(new_word) #ordino la stringa

    for c in new_word_sorted:
        if c not in my_list:
            my_list.append(c)
    
    if list(english_alphabet) == my_list:
        return True
    else:
        return False
        

stringa_1 = is_pangram('the quick brown fox Jumps over the lazaaaaaaaaaaaa dog')
print "Prima stringa ", stringa_1

stringa_2 = is_pangram('davide')
print "Seconda stringa ", stringa_2
        