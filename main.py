from stats import count_words, count_chars, create_chars_report
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    words_count = count_words(file_contents)
    chars_count_dict = count_chars(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    chars_report = create_chars_report(chars_count_dict)
    for report_item in chars_report:
        print(f"{report_item["char"]}: {report_item["num"]}")
    print("============= END ===============")

main()