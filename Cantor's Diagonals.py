def cantor(nested_list):

    return [not (line[i]) for i, line in enumerate(nested_list)]

    # for i in range(len(nested_list)):
    #     elem = nested_list[i][i]
    #     if elem == 0:
    #         cantor_list.append(1)
    #     else:
    #         cantor_list.append(0)

    # return cantor_list

nested_list = [[1,0,0], [0,1,0], [0,0,1]]


print(cantor(nested_list))







