def main():
    print("Starting main function...")
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text.strip())
    print(f"{num_words} words found in the document")

def get_book_text(path):
    print(f"Attempting to open file: {path}")
    with open(path, encoding="utf-8") as f:
        contents = f.read()
    print("File opened and read successfully.")
    return contents

def get_num_words(contents):
    words = contents.split()
    return len(words)

# Entry point
if __name__ == "__main__":
    main()
