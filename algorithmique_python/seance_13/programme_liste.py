
# Programme pour saisir et stocker les informations (nom, prénom, promo) d'un nombre d'élèves choisi


# Définition de la liste de stagiaires

liste_stagiaires = []


# Définition des textes à imprimer lors des saisies

notice_1 = "Veuillez saisir la promo : "
notice_2 = "Veuillez saisir le nombre de stagiaires : "
notice_3 = "Veuillez saisir le NOM : "
notice_4 = "Veuillez saisir le Prénom : "


# Fonction pour espacer les lignes dans le terminal

def espace_inter_ligne(nbr_fois):
    for i in range(nbr_fois):
        print("\n")



                            # Début programme

# Demande du nom de pormo


promo = input(notice_1)


# Demande le nombre de stagiaires de la promo avec vérification

while True:

    try:
        nombre_stagiaires = int(input(notice_2))

        if nombre_stagiaires < 1:
            raise ValueError
        
        espace_inter_ligne(2)
        break

    except ValueError:
        print("Saisissez un nombre entier supérieur à 1.")
        espace_inter_ligne(1)


# Demande des nom et enregistrement dans la liste

for nbr_stagiaires in range(nombre_stagiaires):

    print(f"-------- Pour le stagiaire numéro {nbr_stagiaires+1} --------")

    nom = input(notice_3)
    prenom = input(notice_4)

    liste_stagiaires.append([nom, prenom, promo])

    espace_inter_ligne(1)


# Print de la liste

for nbr_stagiaires in range(len(liste_stagiaires)):

    print(liste_stagiaires[nbr_stagiaires])

espace_inter_ligne(2)