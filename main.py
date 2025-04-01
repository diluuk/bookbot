from stats import get_num_words, get_num_char, get_lists
import sys

def main():
    print("All arguments:", sys.argv)
    if len(sys.argv) > 1:
        print("First argument:", sys.argv[1])
    else:
        print("No arguments provided except the script name!")
    print("============ BOOKBOT ============")
    if len(sys.argv) > 1:
        text = get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    num_words = get_num_words(text.strip())
    print(f"Found {num_words} total words ")
    num_chars = get_num_char(text.strip())
    print("--------- Character Count -------")
#    for char, count in sorted(num_chars.items()):
#        print(f"'{char}': {count}")
    sorted_char_list = get_lists(num_chars)
    for item in sorted_char_list:
        print(f"{item['char']}: {item['count']}")

def get_book_text(path):
    try:
        with open(path, encoding="utf-8") as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'. Please check the path and try again.")
        sys.exit(1)

# Entry point
if __name__ == "__main__":
    main()
