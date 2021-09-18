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