import random

# Activités de Sheldon Cooper

liste_activités_sheldon = ["aller au magasin de BD", "Aller tester son QI", "conception de Robots", "jouer à Dongeons et Dragons", "Jouer aux jeux vidéos"]
liste_activités = []
boissons = ["thé", "café", "chocolat chaud", "the", "cafe", "chocolat chaud"]

# Variables de vérifications

is_true = True
is_false = False
x = False
n = 0

# Fonction de vérification numérique

def verif_numeric(a):
    y = 0
    y = a.isnumeric()
    if y == True:
        raise ValueError

# L'Histoire commence !!!


# Chapitre 1 : L'appel de Sheldon

print("Sheldon a décidé de vous appeler.")
print(" ")

while True:
    try:
        question_1 = input("Voulez-vous répondre à son appel ?          Saisissez oui ou non : ")
        verif_numeric(question_1)
        if question_1.lower() == "oui":
            break
        else:
            raise Exception
    except ValueError:
        print(" ")
        print("Mauvais format ! Il faut uniquement saisir oui ou non.")
        print(" ")
    except Exception :
        print(" ")
        print("Vous n'avez pas répondu à l'appel. Sheldon vous rappel 1 minute après.")
        print(" ")


# Chapirte 2 : Un repas ?

print(" ")
print("Vous avez répondu à l'appel. C'est gentil de votre part. Il entamme l'échange avec vous par une question.")
print(" ")

while True:
    try:
        question_2 = input("Sheldon : Voudrais-tu partager un repas avec moi ?          Saisissez oui ou non : ")
        verif_numeric(question_1)
        if question_2.lower() == "oui":
            x = True
        elif question_2.lower() == "non":
            x = False
        else:
            raise Exception
        break
    except ValueError:
        print(" ")
        print("Sheldon : Un nombre ?! Je ne comprends pas ce que tu veux dire...")
        print(" ")
    except Exception:
        print(" ")
        print("Sheldon : Tu n'as pas répondu à ma question.")
        print(" ")

if x == True :
    print(" ")
    print("Sheldon : D'accord. On se rejoint dans 30 minutes. A plus tard !")
    print("                     Félicitation ! Vous êtes concidéré comme un ami par Sheldon Cooper !")


# Chapitre 3 : Non ? Alors autre chose ?

if x == False:

    print(" ")
    print("Sheldon : Pas faim ?")

    while True:
        try:
            question_3 = input("Dans ce cas là, voudrais-tu partager une boisson chaude ?           Saisissez oui ou non : ")
            verif_numeric(question_3)
            if question_3.lower() == "oui":
                x = True
                break
            elif question_3.lower() == "non":
                x = False
                break
            else:
                raise Exception
        except ValueError:
            print(" ")
            print("Sheldon : Un nombre ?! Je ne comprends pas ce que tu veux dire...")
            print(" ")
        except Exception:
            print(" ")
            print("Sheldon : Tu n'as pas répondu à ma question.")
            print(" ")

    # Chapitre  3.1 : Quel boisson ?
    
    print(" ")

    if x == True :
        print("Sheldon : Parfait !")
        while True:
            try:
                question_3_1 = input("Dans ce cas là, voudrais-tu un thé, un café ou un chocolat chaud ?           Saisissez votre réponse : ")
                verif_numeric(question_3_1)
                if question_3_1.lower() == "thé" or question_3_1.lower() == "café" or question_3_1.lower() == "chocolat chaud":
                    z = question_3_1
                    x = True
                else:
                    raise Exception
                break
            except ValueError:
                print(" ")
                print("Sheldon : Un nombre ?! Je ne comprends pas ce que tu veux dire...")
                print(" ")
            except Exception:
                print(" ")
                print("Mauvais format ! Il faut uniquement saisir l'une des boissons proposés par Sheldon.")
                print(" ")
        if x == True:
            print(" ")
            print(f"Sheldon : Parfait allons boire du {z}.")
            print("                     Félicitation ! Vous êtes concidéré comme un ami par Sheldon Cooper !")

    # Chapitre 4 : Non ? Une activité ?

    if x == False :
        print("Sheldon : Pas soif ?")
        print("Un activité précréative peut-être ?")
        while n != 6 :
            try :
                question_4 = input("Saisissez une activité que vous pourriez pratiquer avec Sheldon : ")
                verif_numeric(question_4)
                liste_activités.append(question_4)
                if question_4 in liste_activités_sheldon:
                    z = question_4
                    break
                else:
                    n += 1
                    raise Exception
            except ValueError:
                print(" ")
                print("Sheldon : Un nombre ?! Je ne comprends pas ce que tu veux dire...")
                print(" ")
            except Exception :
                print(" ")
                print("Sheldon réfléchi.")
                print(" ")
        
        if n == 6 :
            a = random.randint(0,5)
            z = liste_activités[a]
        
        print(" ")
        print(f"Allors faire l'activité '{z}' !")
        print(" ")
        print("                     Félicitation ! Vous êtes concidéré comme un ami par Sheldon Cooper !")
        print(" ")