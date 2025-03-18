# These are the functions we will use to assess book documents

def word_count(book_text):
    # This function returns word count for the text in question
    words = book_text.split()
    return len(words)

def character_count(words):
    # This functions will reduce all characters to lowercase and return a dictionary with the character and the number of times it occurs
    lowercase = words.lower()
    return lowercase

