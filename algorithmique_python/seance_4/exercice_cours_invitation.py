# Alain et Catherine organisent une soirée pour des membres de leur club informatique.
# Ils décident que pour être invité il faut :

# - être ami d’Alain et de Catherine ;
# - ou ne pas être ami d’Alain, mais être ami de Catherine ;
# - ou ne pas être ami de Catherine, mais jouer au bridge.

# Pour un membre quelconque, on définit les variables booléennes suivantes par :
# a = 1 s’il est un ami d’Alain,
# b = 1 s’il joue au bridge,
# c = 1 s’il est un ami de Catherine.a

A = input("Etes vous un amis d'Alain ? ")
B = input("Jouez vous au bridge ? ")
C = input("Etes vous un amis de Catherine ? ")


a = 0
b = 0
c = 0


if A == "oui" or A == "Oui" or A == "OUI":
    a = 1

if B == "oui" or B == "Oui" or B == "OUI":
    b = 1

if C == "oui" or C == "Oui" or C == "OUI":
    c = 1


# CORRECTION :  if b == 1 or c == 1 :
                    #print("Bienvenue")
        #OU
print("Vous êtes invités à la soirée d'Alain et Catherine.")if b or c else print("Vous n'êtes pas invités !!!")

#if (a == 1 and c == 1) or (a == 0 and c == 1) or (c == 0 and b == 1):
    #print("Vous êtes invités à la soirée d'Alain et Catherine.")
#else:
    #print("Vous n'êtes pas invités !!!")


#=======> DRY : Don't Repeat Yourself !