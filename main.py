
def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_text)
    print(f"The amount of words in this book are {word_count}")
    dict_sorter(character_counter_fast(book_text))


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(file_contents):
    return len(file_contents.split())


def character_counter_fast(string):
    low_string = string.lower()
    character_dict = {}
    for character in low_string:
        if character in character_dict:
            temp = character_dict[character]
            temp += 1
            character_dict[character] = temp
        else:
            character_dict[character] = 1
    return character_dict

def dict_sorter(dict):
    unsorted_keys = []
    sorted_keys = []
    min = ""
    for key in dict:
        unsorted_keys.append(key)
    high = max(unsorted_keys)
    for key in range(0, len(unsorted_keys)):
        for character in range(0, len(unsorted_keys)):
            if unsorted_keys[key] < high:
                min = unsorted_keys[key]
        sorted_keys.append(unsorted_keys[key])
        print(sorted_keys)
main()