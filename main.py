import sys
from stats import count_words,sorted_char

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
        with open (filepath) as f:
                return f.read()
def main():
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        word_count = count_words(book_text)
        char_c = sorted_char(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for char, count in char_c:
            print(f"{char}: {count}")
        print("============= END ===============")

if __name__ == "__main__":
    main()



