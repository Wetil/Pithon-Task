def coincidence(list=None, range=None):
    newlist = []

    if list is None or range is None:
        print(newlist)
    else:
        num1 = range.start
        num2 = range.stop

        for i in list:
            if isinstance(i, (int, float)) and (i >= num1 and i < num2):
                newlist.append(i)
        print(newlist)

coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
coincidence() # => []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]
