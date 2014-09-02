
def wordsToList (string_to_change):
    list_with_words = []
    i = 0
    x = 0
    # print("Lenght of String: ", len(string_to_change))
    for symbol in string_to_change :
        i+=1
        if symbol == " " or symbol == ".":
            single_word = string_to_change[x:i]
            list_with_words.append(single_word)
            single_word = ""
            x = i

    return list_with_words


dict_of_words_to_change = {"ironisch":"erotisch", "Ironisch":"Erotisch", "aggressiv":"attraktiv","Aggressiv":"Atrakktiv",
                           "mystisch":"ministerisch", "Mystisch":"Ministerisch", "Ironie":"Erotik", "Aggression":"Attraktivität",
                           "Ministerium":"Mysterium",
                           "erotisch":"ironisch", "Erotisch":"Ironisch", "attraktiv":"aggressiv", "Attraktiv": "Aggressiv",
                           "ministerisch":"mysterisch", "Ministerisch":"Mysterisch", "Erotik":"Ironie", "Attraktivität":"Aggression",
                           "Mysterium":"Ministerium"}


# def changeWords(listOfWords):


# return ''.join(unknown)



print(wordsToList("hallo ich bin die aggressive ironische XY.")) # unbedingt "." oder " " am Ende des Satzes!