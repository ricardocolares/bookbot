from stats import get_book_text, get_num_characters, sorted_dict, get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])

        num_of_words = get_num_words(book_text)
        num_char = get_num_characters(book_text)
        print(num_char)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        for item in sorted_dict(num_char):
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()
