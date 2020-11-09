phonebook = {
    "Afiq" : 60142321523,
    "Fatin" : 60132565891,
    "Wan" : 60112588656
    }

phonebook["Nur"] = 60125687459
del phonebook["Wan"]

if "Nur" in phonebook:
    print("Nur is listed in the phonebook.")
if "Wan" not in phonebook:
    print("Wan is not listed in the phonebook.")
    
