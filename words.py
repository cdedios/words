import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def get_matching_words_from_file(filename, main_letter, secondary_letters):
    with open(filename, 'r', encoding='UTF-8') as file:
        return get_matching_words(file, main_letter, secondary_letters)


# The rules for a match are:
# - word needs to be >= 3 letters
# - word contains main_letter
# - all the other word letters need to be in secondary_letters
def get_matching_words(words, main_letter, secondary_letters):
    word_matches = []

    # Find all words that contain specified words
    for word in words:
        # if you use openOffice .dic dictionary files you need to remove extra characters
        word = word.split("/")[0].lower().strip()
        match = 0
        if main_letter in word.lower():
            for letter in word.lower():
                if letter in secondary_letters:
                    match += 1
        if match >= 2:
            word_matches.append(strip_accents(word))
            continue

    # Remove words with unwanted letters
    for w in list(word_matches):
        for l in w:
            if l not in secondary_letters and l != main_letter:
                word_matches.remove(w)
                break
    return word_matches


# To use with dictionary file

# filename = 'ca.dic'

# result = get_matching_words_from_file(filename, "n", ["p", "o", "r", "t", "a", "l"])
result = get_matching_words(["fofo/_F_V_Y", "tronar/_E", "fogallejar/52"], "n", ["p", "o", "r", "t", "a", "l"])
print(result)
