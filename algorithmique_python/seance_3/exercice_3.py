import datetime

a = datetime.datetime.now()
annee_actuelle = int(f"{a.year}")

while True:
    try:
        naissance = int(input("Veuillez saisir l'année de naissance : "))
        if naissance > annee_actuelle :
            print("Erreur ! Le bébé n'est pas encore né !")
            naissance = int(input("Veuillez saisir l'année de naissance : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

age = annee_actuelle - naissance

if age < 3 :
    print("Le bébé a gagné une palette de petits pois.")
else:
    print("Le bébé n'a rien gagné.")