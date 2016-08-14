print 'Welcome to the Pig Latin Translator!'

original = raw_input("Enter a word:")

pyg = "ay"

def val(original):

    if len (original) > 0  :
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[1:len(new_word)]
        return new_word
        
    else:
        return "Empty"
        
print val(original)
