from stats import get_num_words, get_num_characters, get_sorted_list
import sys

# Check if the user provided a book path
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Exit with error code 1

# Get the book path from command-line arguments
book_path = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")
    character_count = get_num_characters(book_text)
    print("--------- Character Count -------")
    sort_count = get_sorted_list(character_count)
    for char_dict in sort_count:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()