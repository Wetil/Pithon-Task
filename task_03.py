def max_odd(array):
    new_array = []

    for i in array:
        if isinstance(i, (int, float)) and (i % 2 != 0):
            new_array.append(i)

    if(len(new_array) == 0):
        print(None)
    else:
        print(int(max(new_array)))

max_odd([1, 2, 3, 4, 4]) # => 3
max_odd([21.0, 2, 3, 4, 4]) # => 21
max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
max_odd(['ololo', 'fufufu']) # => None
max_odd([2, 2, 4]) # => None
