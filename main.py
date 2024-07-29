def main():
    path = "./books/frankenstein.txt"
    book = get_book_text(path)
    print(count_words(book))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    words = str.split()
    
    return len(words)

main()