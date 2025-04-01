def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_char(contents):
    full_text = contents.lower()
    words_dict = {}
    for char in full_text:
        words_dict[char] = words_dict.get(char, 0) + 1
    return words_dict

def get_lists(dictionary):
    char_list = []
    for char, count in dictionary.items():
        if char.isalpha():
            char_list.append({'char': char, 'count': count})

    char_list.sort(key=lambda x: x['count'], reverse=True)

    return char_list
