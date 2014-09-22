
def wordsToList (string_to_change):
    list_with_words = []
    i = 0
    x = 0
    # print("Lenght of String: ", len(string_to_change))
    for symbol in string_to_change :
        i+=1
        if symbol == " " or symbol == "." or symbol ==":" or symbol == "," or symbol =="-" or symbol == "!":
            single_word = string_to_change[x:i]
            list_with_words.append(single_word)
            single_word = ""
            x = i

    return list_with_words

words = ["ironisch" , "erotisch", "Ironisch", "Erotisch", "aggressiv", "attraktiv","Aggressiv", "Atrakktiv",
                           "mystisch", "ministerisch", "Mystisch", "Ministerisch", "Ironie", "Erotik", "Aggression", "Attraktivität",
                           "Ministerium", "Mysterium"]

print(len(words))
dict_of_words_to_change = {"ironisch" : "erotisch", "Ironisch":"Erotisch", "aggressiv":"attraktiv","Aggressiv":"Atrakktiv",
                           "mystisch":"ministerisch", "Mystisch":"Ministerisch", "Ironie":"Erotik", "Aggression":"Attraktivität",
                           "Ministerium":"Mysterium",
                           "erotisch":"ironisch", "Erotisch":"Ironisch", "attraktiv":"aggressiv", "Attraktiv": "Aggressiv",
                           "ministerisch":"mysterisch", "Ministerisch":"Mysterisch", "Erotik":"Ironie", "Attraktivität":"Aggression",
                           "Mysterium":"Ministerium", "Bundestag" : "Schützenverein"}

# word_to_change_to = ""


def changeWords():
    counter = 0
    for word in list_with_words:
        # print (word)
        if word in dict_of_words_to_change:
            # print(word, " : ", dict_of_words_to_change[word])
            list_with_words[counter] = dict_of_words_to_change[word]


        elif word[0:len(word)-1] in dict_of_words_to_change:

            changed_word = word[0:len(word)-1]
            list_with_words[counter] = dict_of_words_to_change[changed_word] + word[-1]

        elif word[0:len(word)-2] in dict_of_words_to_change:
            changed_word = word[0:len(word)-2]
            list_with_words[counter] = dict_of_words_to_change[changed_word] + word[-2:len(word)]

        elif word[0:len(word)-3] in dict_of_words_to_change:
            changed_word = word[0:len(word)-3]
            list_with_words[counter] = dict_of_words_to_change[changed_word] + word[-3:len(word)]

        elif word[0:len(word)-4] in dict_of_words_to_change:
            changed_word = word[0:len(word)-4]
            list_with_words[counter] = dict_of_words_to_change[changed_word] + word[-4:len(word)]


        counter = counter + 1
    return " ".join(list_with_words)



list_with_words = (wordsToList("Das ironische Ministerium des Bundestages.")) # unbedingt "." oder " " am Ende des Satzes!
print(list_with_words)
print ("\n")


print("\n \n \n")
print(" ".join(list_with_words))
print("\n")
print(changeWords())