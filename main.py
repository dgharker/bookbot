def main():
    file_path = "books/frankenstein.txt"
    
    book = open_book_as_string(file_path)
    words = count_num_words(book)
    #print (words)
    letters = count_characters(book)
    #print(letters)
    charList = []
    for key in letters:
        if key.isalpha():
            charList.append({"letter": key, "count": letters[key]})

    charList.sort(reverse=True,key=sort_on)
    
    print(f"----Begin report of {file_path}----")
    print(f"{words} words found in the document")
    print("\n")
    for c in charList:
        ch = c["letter"]
        num = c["count"]
        print(f"The {ch} character was found {num} times.")
    
    print("--report complete--")


def open_book_as_string(path):
    with open(path) as f:
        book = f.read()
    return book.lower()

def count_num_words(book):
    return len((book.lower()).split())

def count_characters(string):
    chars = {}
    for c in string:
        if chars.get(c) is None:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sort_on(dict):
    return dict["count"]

main()