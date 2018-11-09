while True:
    brackets = input("Input: ")

    max_h = 0
    h = 0
    l = len(brackets)

    # Find max height
    for char in brackets:
        if char == '(':
            h += 1
            if h > max_h:
                max_h = h
        elif char == ')':
            h -= 1

    if h != 0:
        print('There are difference in opening and closing brackets amount:', h, 'instead of 0.')
        break

    # str_list[0] - first layer, [1] - second, and etc.
    str_list = [''] * max_h

    h = 0
    for i in range(len(brackets)):

        # Add one space to all layers
        for j in range(len(str_list)):
            str_list[j] += ' '

        # Replace the space with needed line on current layer
        if brackets[i] == '(':
            str_list[h] = str_list[h][:-1] + '/'

            # If next bracket = current bracket then change height,
            # else not. "h + 1 < max_h" - we don't have to pass the
            # array border, so if input == '((()))' then height = 3,
            # but strings_array[2] is max.
            try:
                if h + 1 < max_h and brackets[i] == brackets[i + 1]:
                    h += 1
            # If brackets[i] == brackets[-1] then brackets[i + 1] will
            # cause an IndexError and we can just pass it, because last
            # char is constantly ')'.
            except IndexError:
                pass

        elif brackets[i] == ')':
            str_list[h] = str_list[h][:-1] + '\\'
            try:
                if brackets[i] == brackets[i + 1]:
                    h -= 1
            except IndexError:
                pass

    # Print all layers in reverse order
    for string in str_list[::-1]:
        print(string)
