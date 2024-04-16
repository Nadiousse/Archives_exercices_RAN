T_ambiante = float(input("Veuillez saisir la température ambiante : "))
T_bassin = float(input("Veuillez saisir la température du bassinde refroidissement : "))

difference = T_ambiante - T_bassin

if difference < 0 :
    difference = -difference

if (difference < 20) or (difference > 40):
    print("Alarme !")