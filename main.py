def main():
    book_path = "books/frankenstein.txt"
    book_contents = open_file(book_path)
    words = split_string(book_contents)
    string_lower = lowercase_all(book_contents)
    word_count = len(words)
    # LETTER_COUNT FIRST TO CREATE A ROUGH DICT AND NEW_LETTER_COUNT TO SORT IT
    # ISALPHA TO CONSIDER ONLY LETTERS
    letter_count = {}
    new_letter_count = {}
    for char in string_lower:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    new_letter_count = sorted(letter_count.items(), key = lambda x: x[1], reverse = True) # KEY SET TO LAMBDA X: X[1] TO SORT IT BY NUMBER AND REVERSE TRUE TO GO FROM HIGHEST TO LOWEST
    # PRINT THE RESULTS
    print("--- Begin report of books ---")
    print(word_count, "words found in the document.")
    print("")
    print("Letter count from highest to lowest:")
    for letter in new_letter_count:
        print("Letter:", letter[0], "Count:", letter[1])
    print("")
    print("--- End of report ---")

# OPENS THE FILE
def open_file(book_path):
    with open(book_path) as f:
        contents = f.read()
        return contents
    
# SPLITS THE STRING INTO A LIST
def split_string(contents):
    return contents.split()

# LOWERCASES THE WHOLE STRING
def lowercase_all(string):
    return string.lower()

main()