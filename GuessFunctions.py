def load_words():
    with open('F:\Storage Files\Documents\GitHub\personal\words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words
