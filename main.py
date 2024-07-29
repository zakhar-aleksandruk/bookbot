def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    print(count_words(book))
    print(count_characters(book))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    
    return len(words)

def count_characters(text):
    chars = {}

    for char in text:
        if char in chars:
            chars[char] += 1
            continue

        chars[char] = 1
    
    return chars

main()