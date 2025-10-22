import sys

from stats import count_words, count_letters, sort_letter_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    # --- kontrola argumentů z příkazové řádky ---
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]  # druhý argument z CLI
    text = get_book_text(path_to_file)

    # výpočty
    word_count = count_words(text)
    letter_counts = count_letters(text)
    sorted_letters = sort_letter_counts(letter_counts)

    # výstup
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_letters:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

main()
