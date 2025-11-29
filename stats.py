
def get_words(text):
    return text.split()

def get_num_words(text_from_book):
    num_of_words = 0
    words_list = text_from_book.split()
    num_of_words = len(words_list)

    return num_of_words

def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
        return file_content

def sort_on(items):
    return items["num"]

def sorted_dict(dict):
    parsed_dict = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        parsed_dict.append(new_dict)
   
    parsed_dict.sort(
        reverse=True, 
        key=sort_on
    )
    return parsed_dict

def get_num_characters(text):
    num_of_characters = {}
    words = text.split()
    char_list = []
    unique_chars = []

    for word in words:
        for char in word.lower():
            char_list.append(char)

    for char in char_list:
        if char not in unique_chars:
            unique_chars.append(char)
            num_of_characters[char] = 1
        else:
            num_of_characters[char] +=1

    return num_of_characters
