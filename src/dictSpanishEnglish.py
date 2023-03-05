spanish_words = {"perro": "Dog, animal descendent from the wolfs",
                 "cuchara": "Spoon, utensil used to eat",
                 "carro": "Car"}

english_words = {"dog": "Perro, animal descendiente de los lobos",
                 "spoon": "Cuchara, utensilico usado para comer",
                 "car": "Carro"}


def process_word(word_to_process = ""):
    resulted_word = word_to_process.lower()

    return resulted_word



def get_word_meaning(word_to_search):

    word_to_search = process_word(word_to_search)

    word_meaning = spanish_words.get(word_to_search)
    
    if word_meaning == None:
        word_meaning = english_words.get(word_to_search)
        
    return word_meaning

