#Variables

annee_en_cours = 2023
age = 0
variable_an_ans_phrase = "ans"


#Vérification de la saisie de l'année de naissance avec int

while True:
    try:
        annee_naissance = int(input("Veuillez saisir l'année de naissance : "))
        print("")
        
        #Vérification de l'année saisie : ne peut être la même année que l'actuel ou plus petit que l'actuel moins 120 ans.
        if annee_naissance >= 2023 or annee_naissance >= annee_en_cours - 120:
            raise ValueError
        
        break
    except ValueError:
        print("Le format de l'année de naissance doit être une entier.", end="\n\n")


#Calcul de l'âge

age = annee_en_cours - annee_naissance


#Vérification => si l'âge est égal à 1 alors la variable pour la phrase de fin change en "an".

if age == 1:
    variable_an_ans_phrase = "an"


#Print du résultat

print(f"La personne a {age} {variable_an_ans_phrase}.")