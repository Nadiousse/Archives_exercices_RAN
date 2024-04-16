#Fonctions

    # Quand ?
# On crée une fonction quand un code se répète à plusieurs endroits.

    # Quoi ?
# C'est un ensemble d'instructions qui réponde à un traitement spécifique.

# Etapes :
# 1. Definir la fonction avec "def" + "nom_fonction" + "():" .
# 2. Ensuite on défini des instructions de la fonction.

# Exemple :
#       def hello():
#           print("bonjours")

# Pour appeler une fonction :
#       hello()

# La fonction hello() s'appelle une procedure car elle effectue juste des traitements.

# Les autres fonction s'appelle des fonction car ils ont une ligne "return".
#       return => permet de "retourner" une valeur en dehors de la fonction.

# On peut utiliser les fonctions comme des variables.

# Les fonctions peuvent acceder aux variables en lecture seule, ils ne peuvent les modifier.

# Variables :
#       Les variables en dehors de la fonction sont des variables GLOBALES.
#       Les variables dans les fonctions sont des variables LOCALES.

# Pour redéfinir les variables GLOBALES dans une fonction il faut utiliser un pointeur : global.
#       global res
# Ceci est à éviter car dans les bonnes pratiques, les fonctions ne devrait pas dépendre des variables globales.

# Les fonctions doivent être les plus réutilisables possible. Il faut leur donner des paramètres.
#       Exemple :   def somme(a,b):
#                       return a+b
