import unicodedata

MAIN_LETTER = "g"
SECONDARY_LETTERS = ["c", "a", "r", "i", "m", "l"]

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
        word = strip_accents(word.split("/")[0].lower().strip())
        match = 0
        if main_letter in word.lower():
            for letter in word.lower():
                if letter in secondary_letters:
                    match += 1
            if match >= 2:
                word_matches.append(word)
                continue

    # Remove words with unwanted letters
    for word in list(word_matches):
        for letter in word:
            if letter not in secondary_letters and letter != main_letter:
                word_matches.remove(word)
                break
    return word_matches


if __name__ == "__main__":
    # To use with dictionary file
    filename = 'catalan_dictionary.txt'

    words = get_matching_words_from_file(filename, MAIN_LETTER, SECONDARY_LETTERS)
    print("You found " + str(len(words)) + " words!")
    print(words)
