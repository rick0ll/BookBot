import sys
from stats import *

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_txt(path)
    words_count = get_words_count(text)

    chars_count = count_chars(text)
    formatted:str = ""
    for element in chars_count:
        formatted += f'{element["char"]}: {element["count"]}\n '

    print(f"\n============ BOOKBOT ============\n"
          f"Analyzing book found at {path}...\n"
          f"---------- Word Count ----------\n"
          f"Found {words_count} total words\n"
          f"--------- Character Count -------\n"
          f"{formatted}\n"
          f"============= END ===============")



if __name__ == "__main__":
    main()