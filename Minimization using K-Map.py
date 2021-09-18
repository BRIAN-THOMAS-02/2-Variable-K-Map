from prettytable import PrettyTable
k_map = PrettyTable()

print("Minimization using K-Map")
print("")

variable = int(input("How many Variables : "))

"""cell = int(input("Enter Cell Number : "))
one = 1
zero = 0

if (variable == 2):
    k_map.field_names = [" ", "B_", "B"]

    if (cell == 0):
        k_map.add_row(["A_", one, 0])
        k_map.add_row(["A", 0, 0])

    elif (cell == 1):
        k_map.add_row(["A_", 0, one])
        k_map.add_row(["A", 0, 0])

    elif (cell == 2):
        k_map.add_row(["A_", 0, 0])
        k_map.add_row(["A", one, 0])

    elif (cell == 3):
        k_map.add_row(["A_", 0, 0])
        k_map.add_row(["A", 0, one])

    print(k_map)

elif (variable == 3):
    k_map.field_names = [" ", "B_ C_", "B_ C", "B C", "B C_"]
    k_map.add_row(["A_", zero, one, zero, one])
    k_map.add_row(["A", zero, zero, one, one])

    print(k_map)


elif(variable == 4):
    k_map.field_names = [" ", "C_ D_", "C_ D", "C  D", "C D_"]
    k_map.add_row(["A_ B_ ", zero, one, zero, one])
    k_map.add_row(["A_ B ", zero, zero, one, one])
    k_map.add_row(["A  B_ ", one, one, zero, one])
    k_map.add_row(["A  B ", zero, zero, one, zero])

    print(k_map)

else:
    print("Not Possible ")"""


def cell_3():
    cell_value = int(input("Value in Cell 3 : "))
    if (cell_value == 0):
        kmap_row1.append(int((cell_value) * 0))
    else:
        kmap_row1.append(int(cell_value))


def cell_7():
    cell_value = int(input("Value in Cell 7 : "))
    if (cell_value == 0):
        kmap_row2.append(int((cell_value) * 0))
    else:
        kmap_row2.append(int(cell_value))


if (variable == 2):
    kmap_row1 = []
    kmap_row2 = []
    for cell in range(0, 4):
        if (cell == 0):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row1.append(int((1)*0))
            else:
                kmap_row1.append(int((1)))

        elif (cell == 1):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row1.append(int((cell/1) * 0))
            else:
                kmap_row1.append(int(cell/1))

        elif (cell == 2):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row2.append(int((cell / 2) * 0))
            else:
                kmap_row2.append(int(cell / 2))

        elif (cell == 3):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row2.append(int((cell/3) * 0))
            else:
                kmap_row2.append(int(cell/3))

        else:
            print("hello")
    print("_", "|", "0", "|", " 1", "|")
    print("0", "|", kmap_row1)
    print("1", "|", kmap_row2)
    print(" ")

    # for pair in range(0, 4):
    if (kmap_row1[0] == kmap_row1[1] == 1):
        print("Pairing : ")
        print("Cell ", 0)
        print("Cell ", 1)

    elif (kmap_row1[0] == kmap_row2[0] == 1):
        print("Pairing : ")
        print("Cell ", 0)
        print("Cell ", 2)

    elif (kmap_row1[1] == kmap_row2[1] == 1):
        print("Pairing : ")
        print("Cell ", 1)
        print("Cell ", 3)

    elif (kmap_row2[1] == kmap_row2[1] == 1):
        print("Pairing : ")
        print("Cell ", 2)
        print("Cell ", 3)

    else:
        print("No Pairs ")

if (variable == 3):
    kmap_row1 = []
    kmap_row2 = []
    for cell in range(0, 8):
        if (cell == 0):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row1.append(int((cell_value) * 0))
            else:
                kmap_row1.append(int(cell_value))

        elif (cell == 1):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row1.append(int((cell_value) * 0))
            else:
                kmap_row1.append(int(cell_value))

        # elif (cell == 3):
        #    cell_value = int(input("Value in Cell " + str(cell) + " : "))
        #    if (cell_value == 0):
        #        kmap_row1.append(int((cell_value) * 0))
        #    else:
        #        kmap_row1.append(int(cell_value))

        elif (cell == 2):
            cell_3()
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row1.append(int((cell_value) * 0))
            else:
                kmap_row1.append(int(cell_value))

        elif (cell == 4):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row2.append(int((cell_value) * 0))
            else:
                kmap_row2.append(int(cell_value))

        elif (cell == 5):
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row2.append(int((cell_value) * 0))
            else:
                kmap_row2.append(int(cell_value))

        # elif (cell == 7):
        #    cell_value = int(input("Value in Cell " + str(cell) + " : "))
        #    if (cell_value == 0):
        #        kmap_row2.append(int((cell_value) * 0))
        #    else:
        #        kmap_row2.append(int(cell_value))

        elif (cell == 6):
            cell_7()
            cell_value = int(input("Value in Cell " + str(cell) + " : "))
            if (cell_value == 0):
                kmap_row2.append(int((cell_value) * 0))
            else:
                kmap_row2.append(int(cell_value))

        else:
            print("")

    print("_", "| " + "00" + " | " + "01" + " | " + "10" + " | " + "11")
    print("0", "|", kmap_row1)
    print("1", "|", kmap_row2)
