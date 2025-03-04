def main():
    print("Starting main function...")
    text = get_book_text("books/frankenstein.txt")
    print(text.strip())  # Full output

def get_book_text(path):
    print(f"Attempting to open file: {path}")
    with open(path, encoding="utf-8") as f:
        contents = f.read()
    print("File opened and read successfully.")
    return contents

# Entry point
if __name__ == "__main__":
    main()
