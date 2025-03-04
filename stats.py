def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    # Create empty dictionary to store character counts
    num_characters = {}
    # Iterate over each character in the book text
    for char in book_text:
        # Convert each character to lowercase
        char = char.lower()
        if char not in num_characters:
            num_characters[char] = 1
        else:
            num_characters[char] += 1
    return num_characters

def sort_on(d):
    return d["count"]

def sort_list(num_characters):
    sorted_list = []
    for char, count in num_characters.items():
        sorted_list.append({"char": char, "count": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list