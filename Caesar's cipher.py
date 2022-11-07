# rotate de letter by a number, spaces makes the program goes crazy

def rotate_word(word, number):
    nword = []
    variable = 0
    word = word.lower()
    
    for i in range(len(word)):
        
        if ord(word[i]) + number < 97:
            variable = 26
        elif ord(word[i]) + number >= 123:
            variable = -26
        else:
            variable = 0 
        
        letra = ord(word[i]) + number + variable
        nword.append(chr(letra))
        
    print(''.join(nword).capitalize())

rotate_word('Jõao', 3)
