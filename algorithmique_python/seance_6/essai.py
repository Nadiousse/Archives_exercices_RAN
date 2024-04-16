while True:
    try:
        a = input("Veuillez saisir un nom : ")
        x = a.isnumeric()
        if x == True:
            raise Exception
        break
    except Exception:
        print("Erreur ! Un nombre ne peut être un nom ou un prénom.")



print(a)