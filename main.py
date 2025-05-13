import sys
from stats import char_count
from stats import word_count
from stats import sort_string



def get_book_text(filepath):
    with open(filepath) as f:
        franken_string = f.read()
    
    return franken_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_txt = sys.argv[1]
    full_txt = get_book_text(book_txt)

    wc = word_count(book_txt)
    character_count = char_count(full_txt)
    sorted_char_count = sort_string(character_count)
    
    print(f"{character_count}")
    print()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_txt}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_char_count:
       char = char_dict["char"]
       count = char_dict["num"]
       if char.isalpha():
           print(f"{char}: {count}")

    print("============= END ===============")

main()
