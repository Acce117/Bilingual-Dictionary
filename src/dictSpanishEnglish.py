from json import *

spanish_words = {}

english_words = {}


def load_data(directory):
    with open(directory) as f:
        data = f.read()
    
    return loads(data)

english_words = load_data("src\data\english_words.txt")
spanish_words = load_data("src\data\spanish_words.txt")


def process_word(word_to_process = ""):
    resulted_word = word_to_process.lower()

    return resulted_word



def get_word_meaning(word_to_search):

    word_to_search = process_word(word_to_search)

    word_meaning = spanish_words.get(word_to_search)
    
    if word_meaning == None:
        word_meaning = english_words.get(word_to_search)
        
    return word_meaning

