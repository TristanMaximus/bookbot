def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lowercase_text = text.lower()
    result = dict()
    for c in lowercase_text:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def sort_on(items):
    return items["num"]

def create_chars_report(chars_count_dictionary):
    result = []
    for character in chars_count_dictionary:
        if character.isalpha():
            result.append(dict(char=character, num=chars_count_dictionary[character]))
    result.sort(reverse=True, key=sort_on)
    return result
