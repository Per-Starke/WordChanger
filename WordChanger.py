#
# def wordsToList (string_to_change):
#     list_with_words = []
#     i = 0
#     x = 0
#     # print("Lenght of String: ", len(string_to_change))
#     for symbol in string_to_change :
#         i+=1
#         if symbol == " " or symbol == "." or symbol ==":" or symbol == "," or symbol =="-" or symbol == "!":
#             single_word = string_to_change[x:i]
#             list_with_words.append(single_word)
#             single_word = ""
#             x = i
#
#     return list_with_words

words = ["ironisch", "erotisch", "Ironisch", "Erotisch", "aggressiv", "attraktiv","Aggressiv", "Attrakktiv",
                           "mystisch", "ministerisch", "Mystisch", "Ministerisch", "Ironie", "Erotik", "Aggression", "Attraktivität",
                           "Ministerium", "Mysterium", "Bundestag", "Schützenverein", "Problem", "Ekzem"]

# print(len(words))
dict_of_words_to_change = {"ironisch" : "erotisch", "Ironisch":"Erotisch", "aggressiv":"attraktiv","Aggressiv":"Atrakktiv",
                           "mystisch":"ministerisch", "Mystisch":"Ministerisch", "Ironie":"Erotik", "Aggression":"Attraktivität",
                           "Ministerium":"Mysterium",
                           "erotisch":"ironisch", "Erotisch":"Ironisch", "attraktiv":"aggressiv", "Attraktiv": "Aggressiv",
                           "ministerisch":"mysterisch", "Ministerisch":"Mysterisch", "Erotik":"Ironie", "Attraktivität":"Aggression",
                           "Mysterium":"Ministerium", "Bundestag" : "Schützenverein", "Schützenverein":"Bundestag", "Problem":"Ekzem",
                           "Ekzem":"Problem"}
# print(len(dict_of_words_to_change))

# word_to_change_to = ""



def changeWords(string_that_changes):
    newStr = string_that_changes
    for word in words:
        if word in string_that_changes:
            print("\n")
            print("Change!")
            print("\n")
            print(word)
            print(dict_of_words_to_change[word])
            newWord = dict_of_words_to_change[word]
            print("word = ", word)
            print("newWord = ", newWord)
            print("newStr = ", newStr)
            newStr = newStr.replace(word, newWord)
            print( newStr )

    return newStr


string_to_change = "Das ironische Ministerium des Bundestages."     # unbedingt "." oder " " am Ende des Satzes!
# list_with_words = (wordsToList(string_to_change))
# print(list_with_words)
# print ("\n")
#

# print("\n \n")
# print(" ".join(list_with_words))
# print("\n")
# print(changeWords())


changed_string = changeWords(string_to_change)
print(changed_string)