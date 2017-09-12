from random import randrange

def scramble(word):
    if (word == ""):
        return 'Please enter a word or a sting of words'
    else:
        scrambled = ''
        word_list = list(word)
        for i in range(len(word_list)):
            rand_index = randrange(0, len(word_list))            
            scrambled = scrambled + word_list[rand_index]            
            del word_list[rand_index]
            
    return scrambled
