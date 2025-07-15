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