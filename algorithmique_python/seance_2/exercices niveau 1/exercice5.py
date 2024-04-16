import datetime

while True:
    try:
        a = int(input("Veuillez entrer l'année de naissance : "))
        break
    except ValueError:
        print("Erreur ! Mauvais format.")

date = datetime.datetime.now()
b = int(f"{date.year}")
print(b)
c = b - a

if c!=1 :
    print("Vous avez ", c, " ans.")
else:
    print("Vous avez ", c, " an.")