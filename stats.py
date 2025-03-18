def get_num_words(file_contents):
        words = file_contents.split()
        return len(words)

def get_num_characters(file_contents):
        char_count = {}
        for char in file_contents:
            lowercase_char = char.lower()
            if lowercase_char in char_count:
                char_count[lowercase_char] += 1
            else:
                char_count[lowercase_char] = 1
        return char_count

def get_sorted_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list
    char_list.sort(reverse=True, key=sort_on)
    return char_list

         