


words = ["ironisch", "erotisch", "Ironisch", "Erotisch", "aggressiv", "attraktiv","Aggressiv", "Attrakktiv",
                           "mystisch", "ministerisch", "Mystisch", "Ministerisch", "Ironie", "Erotik", "Aggression", "Attraktivität",
                           "Ministerium", "Mysterium", "Bundestag", "Schützenverein", "Problem", "Ekzem"]  # List of Word to changr to scan.


dict_of_words = {"ironisch" : "erotisch", "Ironisch":"Erotisch", "aggressiv":"attraktiv","Aggressiv":"Atrakktiv",
                           "mystisch":"ministerisch", "Mystisch":"Ministerisch", "Ironie":"Erotik", "Aggression":"Attraktivität",
                           "Ministerium":"Mysterium",
                           "erotisch":"ironisch", "Erotisch":"Ironisch", "attraktiv":"aggressiv", "Attraktiv": "Aggressiv",
                           "ministerisch":"mysterisch", "Ministerisch":"Mysterisch", "Erotik":"Ironie", "Attraktivität":"Aggression",
                           "Mysterium":"Ministerium", "Bundestag" : "Schützenverein", "Schützenverein":"Bundestag", "Problem":"Ekzem",
                           "Ekzem":"Problem"}  # dict with the word to change to


def changeWords(string_that_changes):
    newStr = string_that_changes  # assignment
    for word in words:            # scans the list words
        if word in string_that_changes: # if the word is in the text
            newWord = dict_of_words[word]
            newStr = newStr.replace(word, newWord)  # It changes to the assigned word in the dict
    return newStr


string_to_change = "Des ironischen Ministeriums des Bundestages"  


changed_string = changeWords(string_to_change)
print (string_to_change)
print (changed_string)
