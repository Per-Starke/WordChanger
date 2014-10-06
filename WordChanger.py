


words = ["ironisch", "erotisch","aggressiv", "attraktiv",
                           "mystisch", "ministerisch", "Ironie", "Erotik", "Aggression", "Attraktivität",
                           "ministerium", "mysterium", "bundestag", "schützenverein", "problem", "ekzem"]  # List of Word to change to scan.
# every word with small letters



dict_of_words = {"ironisch" : "erotisch","aggressiv":"attraktiv",
                           "mystisch":"ministerisch", "ironie":"erotik", "aggression":"attraktivität",
                           "ministerium":"mysterium",
                           "erotisch":"ironisch", "attraktiv":"aggressiv",
                           "ministerisch":"mysterisch","erotik":"ironie", "attraktivität":"aggression",
                           "mysterium":"ministerium", "bundestag" : "schützenverein", "schützenverein":"bundestag", "problem":"ekzem",
                           "Ekzem":"Problem"}  # dict with the word to change to, every word with small letters

def string_to_list(string_to_change_into_list):
    list_wiht_chars = []
    for char in string_to_change_into_list:
        list_wiht_chars.append(char)
    return list_wiht_chars

def nested_list_to_string(nested_list):
    i = 0
    for list in nested_list:
        nested_list[i] = "".join(list)
        i += 1
    return nested_list


def detect_words(string_that_changes):
    realword = []
    list_with_detected_words = []

    for word in words:
        if word.upper() in string_that_changes.upper():
            nr_1 = string_that_changes.upper().find(word.upper())

            realword = string_to_list(word)

            realword[0] = string_that_changes[nr_1]

            list_with_detected_words.append(realword)
    return list_with_detected_words


def change_words_in_list(list_with_words):
    list_with_changed_words = []
    for word in list_with_words:
        new_word = dict_of_words[word.lower()]

        first = word[0]
        second = word[0].upper()
        if first == second:     # if  the first letter is a capital letter
            new_word = string_to_list(new_word)
            new_word[0] = new_word[0].upper()
            "".join(new_word)


        list_with_changed_words.append(new_word)

    return list_with_changed_words




def change_words_in_string(list_with_old_words,list_with_new_words, string_that_changes):
    new_str = string_that_changes
    i = 0
    for word in list_with_old_words:
        new_str = new_str.replace(list_with_old_words[i], list_with_new_words[i])
        i += 1
    return new_str


def change_words(string_to_change):
    list = detect_words(string_to_change)
    old_list = list
    list = nested_list_to_string(list)
    list = change_words_in_list(list)
    list = nested_list_to_string(list)
    new_list = list
    string = change_words_in_string(old_list, new_list, string_to_change)
    return (string)



string_to_change = "Des ironischen  Erotikministerium des Bundestages"


string = change_words(string_to_change)
print(string)
