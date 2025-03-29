def sort_list(list):
    if len(list) == 0:
        print(list)
    else:
        maximum = max(list)
        minimum = min(list)

        for i in range(len(list)):
            if(list[i] == minimum):
                list[i] = maximum
                continue
            if (list[i] == maximum):
                list[i] = minimum
                continue
        list.append(minimum)
        print(list)

sort_list([]) # => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1]) # => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]
