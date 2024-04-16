while True:
    try:
        x = input("Veuillez entrer Oui ou Non : ")
        if x.isnumeric() == True:
            raise Exception
        if x.lower() == "oui":
            break
        else:
            raise ValueError
    except ValueError:
        print("Non, et maintenant ?")
    except Exception:
        print("Oui ou non, pas de nombres.")

