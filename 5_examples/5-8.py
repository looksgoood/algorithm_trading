def get_3_word_list(str_list):
    new_list=[]
    for str in str_list:
        new_list.append(str[0:3])

    return new_list

list = ['Seoul', 'Deagu', 'Kwangju', 'Jeju']
print(get_3_word_list(list))