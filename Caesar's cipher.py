def is_palindrome(word, word2):
    p = len(word2)
    c = -1
    for i in range(p):
        if word[::i+1] != word2[::c]:
            return False
        c -= 1
    return True 
        
print(is_palindrome('pots', 'varv'))