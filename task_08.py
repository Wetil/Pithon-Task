def multiply_numbers(inputs=None):
    inputs = str(inputs)
    count = 0
    number = 1

    for i in range(len(inputs)):
        if(inputs[i].isdigit()):
            number = number * int(inputs[i])
            count += 1

    if(count == 0):
        print("None")
    else:
        print(number)

multiply_numbers() # => None
multiply_numbers('ss') # => None
multiply_numbers('1234') # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3) # => 6
multiply_numbers([5, 6, 4]) # => 120
