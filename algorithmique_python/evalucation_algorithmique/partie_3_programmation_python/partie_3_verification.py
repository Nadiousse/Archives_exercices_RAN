#Variable de vérification

petit_ou_grand = 0


# Boucle de vérification

while True:
    try:
        nombre_a_verifier = float(input("Veuillez saisir un chiffre compris entre 10 et 20 : "))

        #vérification si en dehors des limites de 10 et 20 :
        if nombre_a_verifier < 10 or nombre_a_verifier > 20:
            petit_ou_grand = nombre_a_verifier
            raise Exception
        
        break

    # Exception qui renvoi s'il faut un chiffre plus petit ou plus grand.
    except Exception:
        if petit_ou_grand > 20 :
            print("Plus petit !", end="\n\n")
        elif petit_ou_grand < 10 :
            print("Plus grand !", end="\n\n")
