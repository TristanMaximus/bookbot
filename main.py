from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    words_count = count_words(file_contents)
    print(f"{words_count} words found in the document")
    chars_count_dict = count_chars(file_contents)
    print(chars_count_dict)

main()