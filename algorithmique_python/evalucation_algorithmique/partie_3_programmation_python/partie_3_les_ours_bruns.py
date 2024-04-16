# Definition de la fonction

def type_de_statut(age_du_beneficiaire):
    if age_du_beneficiaire < 12:
        return (1)
    elif age_du_beneficiaire > 60:
        return (2)
    else:
        return (0)


#Listes : tableaux de tarifs

Statut = ["Adultes", "Enfant", "Senior"]
TypeForfait_1 = [25.80, 18.70, 21.40]
TypeForfait_2 = [510, 300, 340]


#Variables :

Age = 0
Tarif = 0


# Vérification de saisie pour le type de forfait:

while True:
    try:
        forfait_choisi = int(input("Veuillez saisir le forfait. 1 pour le forfait jour, 2 pour le forfait saison : "))
        
        #Vérification de saisi 1 ou 2 et aucun autre chiffre
        if forfait_choisi < 1 or forfait_choisi > 2:
            raise ValueError
        
        break
    except ValueError:
        print("La saisie n'est pas au bon format.", end="\n\n")


# Vérification du statut du bénéficiaire :

while True :
    try:
        age_beneficiaire = int(input("Veuillez saisir l'âge du bénéficiaire : "))

        #Vérification de saisie entre 0 et 120 ans
        if age_beneficiaire > 120 or age_beneficiaire < 0 :
            raise ValueError
        
        break
    except ValueError:
        print("La saisie n'est pas au bon format.", end="\n\n")


#Calcul prix Final si forfait 1 journée

if forfait_choisi == 1 :
    Tarif = TypeForfait_1[type_de_statut(age_beneficiaire)]



#Calcur prix final si forfait saison 

if forfait_choisi == 2 :
    Tarif = TypeForfait_2[type_de_statut(age_beneficiaire)]


#Print du message final avec les résultats

print(f"Le prix pour un bénéficiaire {Statut[type_de_statut(age_beneficiaire)]} est de {Tarif}€.")