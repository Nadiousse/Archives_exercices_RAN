mot = input("Veuillez saisir un mot : ")
a = 0
x = len(mot)-1

for i in range(0, len(mot)) :
    if mot[i] == mot[x-i]:
        a = 0
    if mot[i] != mot[x-i]:
        a = a + 1

if a == 0:
    print("Le mot est un palindrome.")
else :
    print("Le mot n'est pas un palindrome.")