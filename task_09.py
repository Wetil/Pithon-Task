def connect_dicts(dict1, dict2):
    new_dict = {}

    for key, value in dict1.items():
        if(value >= 10):
            new_dict[key] = value

    for key, value in dict2.items():
        if(value >= 10):
            if (key in dict1):
                if (sum(dict1.values()) <= sum(dict2.values())):
                    new_dict[key] = value
                else:
                    continue
            else:
                new_dict[key] = value

    print(dict(sorted(new_dict.items(), key=lambda item: item[1])))

connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }) # => { "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # => { d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }) # => { "c": 11, "b": 12, "a": 15 }
