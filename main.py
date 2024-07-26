
def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_text)
    print(f"The amount of words in this book are {word_count}")
    character_counter_fast(book_text)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(file_contents):
    return len(file_contents.split())

def character_counter(string):
    character_dict = {}
    for character in string:
        character_dict[character] = 1
    for letter in string:
        temp = character_dict[letter]
        temp += 1
        character_dict[letter] = temp
    
    print(character_dict)

def character_counter_fast(string):
    character_dict = {}
    for character in string:
        character_dict[character] = 1 
    print(character_dict)
    
main()