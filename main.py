"""
def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        book_words = file_contents.split()
        print (f"The amount of words in this book is {len(book_words)}")



main()
"""


def main():
    book_text = get_book_text(books/frankenstein.txt)
    word_count = word_counter(book_text)
    print(f"The amount of words in this book are {word_count}")
    


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(file_contents):
    return len(file_contents.split())

main()