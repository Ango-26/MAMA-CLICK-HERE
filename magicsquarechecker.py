columns_ok = 0
rows_ok = 0
diagonals_ok = 0

print('Hello there, Welcome to the Magic Square 3x3 Task')
name = input("What is your name?   ")

print("Hey " + str(name))
know = input("Do you know what a magic square is? 'y' for yes and 'n' for no. ")

if know == "n":

    print('A Magic Square 3x3 uses numbers for 1 to 9 only once')
    print('such that sum of all rows, sum of all columns and sum of all diaganols are equal')
    print('Please input 9 unique digits between one to nine in the form of a grid')
    print("Use enter to proceed " + str(name))

    num_1 = int(input(" Can u give me the column 1 and row 1 digit?  "))
    num_2 = int(input(" Can u give me the column 2 and row 1 digit?  "))
    num_3 = int(input(" Can u give me the column 3 and row 1 digit?  "))
    num_4 = int(input(" Can u give me the column 1 and row 2 digit?  "))
    num_5 = int(input(" Can u give me the column 2 and row 2 digit?  "))
    num_6 = int(input(" Can u give me the column 3 and row 2 digit?  "))
    num_7 = int(input(" Can u give me the column 1 and row 3 digit?  "))
    num_8 = int(input(" Can u give me the column 2 and row 3 digit?  "))
    num_9 = int(input(" Can u give me the column 3 and row 3 digit?  "))

    sumcolumn_1 = num_1 + num_4 + num_7
    sumcolumn_2 = num_2 + num_5 + num_8
    sumcolumn_3 = num_3 + num_6 + num_9

    sumrow_1 = num_1 + num_2 + num_3
    sumrow_2 = num_4 + num_5 + num_6
    sumrow_3 = num_7 + num_8 + num_9

    sumdiagonal_1 = num_1 + num_5 + num_9
    sumdiagonal_2 = num_3 + num_5 + num_7

    if sumcolumn_1 == sumcolumn_2 == sumcolumn_3:
        columns_ok = 0
    else:
        columns_ok = 1

    if sumrow_1 == sumrow_2 and sumrow_2 == sumrow_3 and sumrow_3 == sumrow_1:
        rows_ok = 0
    else:
        rows_ok = 1

    if sumdiagonal_1 == sumdiagonal_2:
        diagonals_ok = 0
    else:
        diagonals_ok = 1

    if columns_ok == rows_ok == diagonals_ok == 0:
        print(" It's a magic square!!!")
    else:
        print("It's unfortunately not a magic square")

elif know == "y":

    print('Please input 9 unique digits between one to nine in the form of a grid')
    print("Use enter to proceed " + str(name))

    num_1 = int(input(" Can u give me the column 1 and row 1 digit?  "))
    num_2 = int(input(" Can u give me the column 2 and row 1 digit?  "))
    num_3 = int(input(" Can u give me the column 3 and row 1 digit?  "))
    num_4 = int(input(" Can u give me the column 1 and row 2 digit?  "))
    num_5 = int(input(" Can u give me the column 2 and row 2 digit?  "))
    num_6 = int(input(" Can u give me the column 3 and row 2 digit?  "))
    num_7 = int(input(" Can u give me the column 1 and row 3 digit?  "))
    num_8 = int(input(" Can u give me the column 2 and row 3 digit?  "))
    num_9 = int(input(" Can u give me the column 3 and row 3 digit?  "))

    sumcolumn_1 = num_1 + num_4 + num_7
    sumcolumn_2 = num_2 + num_5 + num_8
    sumcolumn_3 = num_3 + num_6 + num_9

    sumrow_1 = num_1 + num_2 + num_3
    sumrow_2 = num_4 + num_5 + num_6
    sumrow_3 = num_7 + num_8 + num_9

    sumdiagonal_1 = num_1 + num_5 + num_9
    sumdiagonal_2 = num_3 + num_5 + num_7

    if sumcolumn_1 == sumcolumn_2 == sumcolumn_3:
        columns_ok = 0
    else:
        columns_ok = 1

    if sumrow_1 == sumrow_2 and sumrow_2 == sumrow_3 and sumrow_3 == sumrow_1:
        rows_ok = 0
    else:
        rows_ok = 1

    if sumdiagonal_1 == sumdiagonal_2:
        diagonals_ok = 0
    else:
        diagonals_ok = 1

    if columns_ok == rows_ok == diagonals_ok == 0:
        print(" It's a magic square!!!")
    else:
        print("It's unfortunately not a magic square")