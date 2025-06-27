def get_num_words(book_text):
    return len(book_text.split())

def get_char_dict(book_text):
    char_count = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in char_count:
            char_count[lower_char] = 0
        char_count[lower_char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def dict_sorted_list(dict):
    dict_list = []
    for char in dict:
        dict_list.append({"char": char, "num": dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list