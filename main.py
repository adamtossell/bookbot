from stats import get_num_words, get_num_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    print(f"{num_words} words found in the document")
    print(f"{num_characters}")

main()