
def arithmetic_arranger(problems, *activate):
    # ! Definition of variables
    row1 = []
    row2 = []
    row_operator = []
    higher = []
    result_operation = []
    space_beetween = '    '
    list_space1 = []
    list_space2 = []
    list_space3 = []
    space3 = '  '
    list_dashes = []
    first_line = ''
    second_line = ''
    third_line = ''
    four_line = ''

    #! Asserts
    # Only 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Only Substraction and Addition
    for operation in problems:
        data = []
        data = operation.split()
        if data[1] == '*' or data[1] == '/':
            return "Error: Operator must be '+' or '-'."

        # Only digits
        try:
            int(data[0])
            int(data[2])
        except:
            return "Error: Numbers must only contain digits."

        # Only 4 digits
        if len(data[0]) > 4 or len(data[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # lists from data
        row1.append(int(data[0]))
        row2.append(int(data[2]))
        row_operator.append(data[1])

    # ! Main
    for i in range(len(row1)):

        # Maximum value between quantities
        if row1[i] > row2[i]:
            higher.append(row1[i])
        elif row2[i] > row1[i]:
            higher.append(row2[i])

        # List operators
        if row_operator[i] == '+':
            result_operation.append(row1[i] + row2[i])
        elif row_operator[i] == '-':
            result_operation.append(row1[i] - row2[i])

        # List Dash
        dash = '-'
        dash *= len(str(higher[i])) + 2
        list_dashes.append(dash)

        # List Spaces
        space1 = ' '
        space1 *= len(str(list_dashes[i])) - len(str(row1[i]))
        list_space1.append(space1)

        space2 = ' '
        space2 *= len(str(list_dashes[i])) - \
            len(str(row2[i])) - len(str(row_operator[i]))
        list_space2.append(space2)

        space3 = ' '
        space3 *= len(str(list_dashes[i])) - len(str(result_operation[i]))
        list_space3.append(space3)

        # Delete space at the end
        if i == len(row1) - 1:
            space_beetween = ''

        # Creating print lines
        first_line += list_space1[i] + str(row1[i]) + space_beetween
        second_line += row_operator[i] + \
            list_space2[i] + str(row2[i]) + space_beetween
        third_line += list_dashes[i] + space_beetween
        four_line += list_space3[i] + str(result_operation[i]) + space_beetween

    # Condition to print result
    if activate and activate[0] == True:
        arranged_problems = first_line + '\n' + \
            second_line + '\n' + third_line + '\n' + four_line
    else:
        arranged_problems = first_line + '\n' + \
            second_line + '\n' + third_line

    # Fin
    return arranged_problems


# ! Samples
# x = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
# y = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
# print(x)
# print(y)
# print(len(x))
# print(len(y))
# # x = list(x)
# # y = list(y)
# # for i in range(len(x)):
# #     print(x[i], y[i])
# if x == y:
#     print('yes')
# else:
#     print('no')
