from stats import get_num_words, get_char_dict, dict_sorted_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_dict = get_char_dict(book_text)
    char_list = dict_sorted_list(char_dict)
    return print_report(filepath, num_words, char_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    


def print_report(filepath, num_words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in  char_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()