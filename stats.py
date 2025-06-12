def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    results = {}
    for char in text:
        char = char.lower()
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
    return results

def sort_on(dict):
    return dict["num"]

def get_sorted_char_count(counts):
    result = []
    for k,v in counts.items():
        new_dict = {}
        new_dict["char"] = k
        new_dict["num"] = v
        result.append(new_dict)
    result.sort(reverse=True, key=sort_on)
    return result