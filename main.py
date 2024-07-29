import pdb

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_text)
    # print(f"The amount of words in this book are {word_count}")
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
    min1 = ""
    for key in dict:
        unsorted_keys.append(key)

    
    
    # pdb.set_trace()
    for key in range(0, len(unsorted_keys)):
        min1 = max(unsorted_keys)
        for character in range(0, len(unsorted_keys)):
            if unsorted_keys[character] < min1:
                min1 = unsorted_keys[character]
                min1_index = character
        sorted_keys.append(min1)
        print(f"list length is {len(unsorted_keys)}")
        print(f"key to pop is {unsorted_keys[min1_index]}")
        unsorted_keys.pop(min1_index)
        print (f"min index {min1_index}")
        
        print (f"min is {min1}")
        print(f"Unsorted Keys {unsorted_keys}")
        #print(sorted_keys)
    print (f"sorted list {sorted_keys}")
main()

'''
l(ist) - show current lines
n(ext) - run current line, move to next line
s(tep) - step into function called by current line
b(reak) - pause program at that line
c(ontinue) - continue running the program until breakpoint or until finish
CTRL+D - KILL
'''