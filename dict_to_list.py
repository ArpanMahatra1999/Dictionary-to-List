textDictionary = {' love': 1, ' relief': 1, ' envy': 1}


def dict_to_list(dictionary):
    article = str(dictionary)
    important_chars = ""
    for a in article:
        if a == " " or a == "'" or a == "{" or a == "}":
            pass
        else:
            important_chars = important_chars + a
    article_key_value = important_chars.split(",")
    article_in_array = []
    for akv in article_key_value:
        akv_unmaintained = akv.split(':')
        akv_unmaintained[1] = int(akv_unmaintained[1])
        article_in_array.append([akv_unmaintained[0], akv_unmaintained[1]])
    return article_in_array


print(dict_to_list(textDictionary))