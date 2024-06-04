def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_text_from_file(file_path) 
    word_count = count(file_contents)
    charected_count = count_characters(file_contents)
    list_of_dict = convert_dict_to_list(charected_count)
    sorted_list = sorted(list_of_dict, key=sort_on, reverse=True)
    print_report(word_count, sorted_list, file_path)


def count(text):
    return len(text.split())

def count_characters(text):
    new_dict = {}
    for i in text:
        i = i.lower()
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict

def get_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()
    
def convert_dict_to_list(dictionary):
    new_list = []
    for key in dictionary:
        if key.isalpha():
            new_list.append({"char": key, "num": dictionary[key]})
    return new_list

def sort_on(dict):
    return dict["num"]

def print_report(word_count, charactes, file_path):
    print(f"--- Begin report of ${file_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for char in charactes:
        print(f"The'{char['char']}' character was found {char['num']} times")
    print("--- End report ---")

main()