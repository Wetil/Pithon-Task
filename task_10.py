def count_words(string):
    new_string = string.lower().split()
    new_dict = {}

    for i in range(len(new_string)):
        if("," in new_string[i]):
            new_string[i] = new_string[i].replace(",", "")
        if(new_string[i].isalpha()):
            if(new_string[i] in new_dict):
                new_dict[new_string[i]] += 1
            else:
                new_dict[new_string[i]] = 1

    print(new_dict)

count_words("A man, a plan, a canal -- Panama")  # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo")  # => {"doo": 3, "bee": 2}
