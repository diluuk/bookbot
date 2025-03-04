def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_char(contents):
    full_text = contents.lower()
    words_dict = {}
    for char in full_text:
        words_dict[char] = words_dict.get(char, 0) + 1
    return words_dict
