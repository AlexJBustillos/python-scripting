def mult(num):
    return num * 2

with open('prime_numbers.txt') as prime_numbers_file:
    prime_num = prime_numbers_file.readlines()
    for num in prime_num:
        print(mult(int(num)))

with open('one_to_hundred.txt') as numbers_file:
    list_of_num = numbers_file.readlines()
    result = []

    for num_text in list_of_num:
        if 'Five' in num_text:
            remove_newline_txt = num_text[:-1]
            # print(remove_newline_txt)
            result.append(remove_newline_txt)
        elif 'Fifteen' in num_text:
            remove_newline_txt = num_text[:-1]
            # print(remove_newline_txt)
            result.append(remove_newline_txt)
    print(result)