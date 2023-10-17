import string
import re

import PyPDF2


def remove_character(sentence, char_to_remove, replace_char=''):
    sentence_without_char = sentence.replace(char_to_remove, replace_char)
    return sentence_without_char


def remove_punctuation(sentence):
    # Create a translation table to remove punctuation
    sentence_without_punctuation = remove_character(sentence, '—')
    for punc in ['>', '<', '=', '+', '-', '*', '/', '\\', '|', '[', ']', '{', '}', '(', ')', ':', ';', ',', '.', '?']:
        sentence_without_punctuation = remove_character(sentence_without_punctuation, punc, ' ')
    sentence_without_punctuation = remove_character(sentence_without_punctuation, '“')
    sentence_without_punctuation = remove_character(sentence_without_punctuation, '”')
    sentence_without_punctuation = remove_character(sentence_without_punctuation, '»')
    sentence_without_punctuation = remove_character(sentence_without_punctuation, '«')
    sentence_without_punctuation = remove_character(sentence_without_punctuation, "’", " ")
    sentence_without_punctuation = remove_character(sentence_without_punctuation, "‘", " ")
    sentence_without_punctuation = remove_character(sentence_without_punctuation, "'", " ")

    return sentence_without_punctuation


def pdf_to_text(pdf_file):
    try:
        pdf_text = ""
        with open(pdf_file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page in pdf_reader.pages:
                pdf_text += page.extract_text()

        return pdf_text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def contains_number(input_string):
    # Use a regular expression to find any digit in the string
    pattern = r'\d'
    if re.search(pattern, input_string):
        return True
    else:
        return False


def is_roman_numeral(word):
    # Regular expression pattern to match Roman numerals
    pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    return bool(re.match(pattern, word))


def get_unique_words_from_string(text):
    unique_words = set()

    # Split the input text into words and remove punctuation
    lines = text.split('\n')
    for line in lines:
        words = line.strip().split()
        words = [word.strip(string.punctuation) for word in words]
        words = [word for word in words if not contains_number(word)]
        words = [word.lower() for word in words if word != '']
        words = [word for word in words if len(word) > 1]
        words = [word for word in words if not is_roman_numeral(word.upper())]


        # Add unique words to the set
        unique_words.update(words)

    return list(unique_words)


def getWord(file):
    text = pdf_to_text(file)
    text = remove_punctuation(text)

def addWordsToNew(words):
    knownWordsFile = open("EnglishTradToFrench.txt", "r")
    f = open("newWordsEnglish.txt", "r")
    knownWords = []
    for line in f:
        knownWords.append(line.split("\n")[0])
    f.close()
    for line in knownWordsFile:
        knownWords.append(line.split("|")[0])
    knownWordsFile.close()
    f = open("newWords2.txt", "a")
    for word in words:
        if word not in knownWords:
            print("|" + word + "|")
            f.write(word + "\n")
    f.close()

def addWordsToNew2(words):
    f = open("newWordsFrench.txt", "r")
    knownWords = []
    for line in f:
        knownWords.append(line.split("\n")[0])
    f.close()
    f = open("newWords2.txt", "a")
    for word in words:
        if word not in knownWords:
            print("|" + word + "|")
            f.write(word + "\n")
    f.close()


def has_duplicates(input_list):
    seen = set()
    for item in input_list:
        if item in seen:
            return True
        seen.add(item)
    return False



if __name__ == "__main__":
    text = pdf_to_text("Le_Petit_Nicolas_-_Sempre_Goscinny.pdf")
    text = remove_punctuation(text)
    words = get_unique_words_from_string(text)
    addWordsToNew2(words)
