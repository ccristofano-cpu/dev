def str_to_int(text):
    try: 
        return int(text)
    except ValueError:
        print("Erreur de conversion")
        return 0


# print(str_to_int("42"))
# print(str_to_int("abc"))
# print(str_to_int("-15"))

def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Index hors limites")
        return None

numbers = [10,20,30,40]

print(safe_list_access(numbers, 0))
print(safe_list_access(numbers, 10))


def read_file(filename)