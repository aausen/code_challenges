"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
    # seperate each word
    # loop through list of words
    # determine if the word starts with vowel or not
    # if vowel, add yay to end
    # if not vowel, move first letter to end, then add ay
    # add words back together to create a string of the phrase
    # if empty raise error

    list_of_words = phrase.split(" ")
    pig_latin_phrase = []
    i = 0
    while i <= len(list_of_words) - 1:
        word = list_of_words[i]
        if word[0] in ["a", "e", "i", "o", "u"]:
            # pig_latin_phrase += (word + "yay" + " ")
            pig_latin_phrase.append(word + "yay")
        else:
            word = list(word)
            end_letter = word.pop(0)
            join_word = "".join(word)
            new_word = join_word + end_letter
            # pig_latin_phrase += (new_word + "ay" + " ")
            pig_latin_phrase.append(new_word + "ay")

        i += 1
    # return pig_latin_phrase.strip()
    return " ".join(pig_latin_phrase)
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. REATGAY OBJAY!\n")
