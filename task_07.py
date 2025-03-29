def combine_anagrams(words_array):
    new_array = []
    final_array = []
    seen = []

    for i in range(len(words_array)):
        if(words_array[i] in seen):
            continue
        for j in range(len(words_array)):
            if(sorted(words_array[i].lower()) == sorted(words_array[j].lower())):
                new_array.append(words_array[j])
                seen.append(words_array[j])
        final_array = final_array + [new_array]
        new_array = []
    print(final_array)


combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]) # => [["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"]]
