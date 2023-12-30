from Backend import dataset_importer


def men1():
    print("\n\nHOW SHOULD THE DATASET BE IMPORTED?\n")
    print("Press 1 for importing csv.")
    print("Press 2 for importing excel file.\n")

    i= int(input("Enter your input: "))
    src= input("Enter the source address/hyperlink: ")

    out= dataset_importer.importer(i, src)
    return out 