def word_count(filepath):
    with open(filepath) as f:
        word_string = f.read()
    
    word_count = len(word_string.split())

    return word_count

def char_count(text_string):
    char_dict = {}

    word_string = text_string.lower()

    for char in word_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def sort_string(dict_list):
    char_list = []
    for char, count in dict_list.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=lambda item: item["num"])

    return char_list