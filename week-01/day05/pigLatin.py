def get_words():
    """
        Return a list of words from the user.
    """
    #TODO: Return something
    words = raw_input("Enter a word or phrase: ")
    words_list = words.split(" ")
    return words_list

def first_vowel(word):
    """
        Find the index of the first vowel
        Return none if there are no vowels
    """
    #TODO: Return something
    vowels = ['a','e','i','o','u']
    for i in range(len(word)):
        if word[i].lower() in vowels:
            return i
#words = get_words()
#print words

def rotate(word):
    """
        Return a version of word that
        is in pig latin. Empty string is not allowed
    """
    #TODO: Return something
    new_word = ""
    letters = list(word)
    if first_vowel(word) != 0:
        letters.append(letters[0].lower())
        letters.remove(letters[0])
        letters.append("ay")
    else:
        letters.extend("yay")
    for i in range(0, len(letters)):
        new_word += letters[i]
    return new_word


def combine_words(word_list):
    """
        Combine a list of words into a phrase that
    """
    #TODO: Return something
    phrase = ""
    for i in word_list:
        phrase = phrase + str(i) + " "
        #strip removes space at end
    return phrase.strip()


words = get_words()
pig_phrase = []
for word in words:
    pig_word = rotate(word)
    pig_phrase.append(pig_word)

print combine_words(pig_phrase)
