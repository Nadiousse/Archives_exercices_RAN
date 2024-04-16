list_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
list_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

A = int(input("Veuillez saisir l'année actuelle : "))
M = int(input("Veuillez saisir le mois actuel : "))
J = int(input("Veuillez saisir le jour actuel : "))

a = A
m = M

if M == 1 or M == 2:
    a = A - 1
    m = M + 12

N = J + int((13*m+3)/5) + int(5*a/4) - int(a/100) + int(a/400)
N = N % 7

print("Le ", J, list_mois[M-1], A, "est un", list_semaine[N],".")