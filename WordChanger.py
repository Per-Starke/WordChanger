
def wordsToList (string_to_change):
    list_with_words = []
    i = 0
    x = 0
    # print("Lenght of String: ", len(string_to_change))
    for symbol in string_to_change :
        i+=1
        if symbol == " " or symbol == "." :
            single_word = string_to_change[x:i-1]
            list_with_words.append(single_word)
            single_word = ""
            x = i

    return list_with_words


dict_of_words_to_change = {"ironisch" : "erotisch", "Ironisch":"Erotisch", "aggressiv":"attraktiv","Aggressiv":"Atrakktiv",
                           "mystisch":"ministerisch", "Mystisch":"Ministerisch", "Ironie":"Erotik", "Aggression":"Attraktivität",
                           "Ministerium":"Mysterium",
                           "erotisch":"ironisch", "Erotisch":"Ironisch", "attraktiv":"aggressiv", "Attraktiv": "Aggressiv",
                           "ministerisch":"mysterisch", "Ministerisch":"Mysterisch", "Erotik":"Ironie", "Attraktivität":"Aggression",
                           "Mysterium":"Ministerium"}

# word_to_change_to = ""
def changeWords():
    counter = 0
    for word in list_with_words:
        # print (word)
        if word in dict_of_words_to_change:
            print(word, " : ", dict_of_words_to_change[word])
            list_with_words[counter] = dict_of_words_to_change[word]


        # list_with_words[counter][0:len(list_with_words[counter])-1]

        elif word in list_with_words[counter][0:len(list_with_words[counter])-1]:

            list_with_words[counter] = list_with_words[counter][0:len(list_with_words[counter])-1]

        elif word in list_with_words[counter][0:len(list_with_words[counter])-2]:

            list_with_words[counter] = list_with_words[counter][0:len(list_with_words[counter])-2]

        counter = counter + 1
    return " ".join(list_with_words)



list_with_words = (wordsToList("Ironisch: hallo ich bin die aggressive ironische XY.")) # unbedingt "." oder " " am Ende des Satzes!
print(list_with_words)
print ("\n")
print(changeWords())