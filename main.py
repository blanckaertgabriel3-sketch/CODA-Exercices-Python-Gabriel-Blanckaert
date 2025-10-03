def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Exercice 2 : Afficher prenom.")
    prenom = input ("entrer votre prénom")
    print("bonjour, {prenom} !")

def exercice3():
    print("Exercice 3 : afficher message sur 3 lignes")
    print("Première ligne\n")
    print("Deuxième ligne\n")
    print("Troisième ligne\n")

def exercice4():
    print("Exercice 4 : Calculer l'âge")
    dateNaissance = input ("entrer date naissance")
    age = 2025
    age = age - dateNaissance
    print ("Vous avez environ {age} ans")

def exercice5():
    print("Exercice 5 : Addition simple")
    a = float(input ("Entrer le premier nombre: "))
    b = float(input ("Entrer le deuxième nombre: "))
    somme = a + b
    print (f"la somme des 2 nombres est :{somme}")

def exercice6():
    print("Exercice 6 : Soustraction simple")
    a = float(input ("Entrer le premier nombre: "))
    b = float(input ("Entrer le deuxième nombre: "))
    soustraction = a - b
    print (f"la soustraction des 2 nombres est :{soustraction}")


def exercice7():
    print("Exercice 7 : Multiplication simple")
    a = float(input ("Entrer le premier nombre"))
    b = float(input ("Entrer votre 2em nombre"))
    multiplication = a * b
    print (f"la multiplication des 2 est : {multiplication}")


def exercice8():
    print("Exercice  8: division simple")
    a = float(input("entrer votre nombre: "))
    b = float(input ("entrer votre 2em nombre"))
    division = a / b
    print (f"le résultat est {division}")





def exercice9():
    print("Exercice  9: Carré d'un nombre")
    a = float(input("entrer un nombre"))
    carré = a**2
    print (f"le résultat est : {carré}")

 

def exercice10(): 

    print("Exercice  10: Double d'un nombre") 
    a = float(input("entrer un nombre"))
    double = a *2
    print (f"le résultat est {double}")

def exercice11(): 

    print("Exercice  11: Moitié d'un nombre") 
    a = float(input("entrer un nombre"))
    division = a/2
    print (f"le résultat est {division}")

def exercice12(): 

    print("Exercice  12: Afficher 5 fois") 
    for i in range(5): 
        print ("Hello")
 
 
def exercice13(): 

    print("Exercice  13: Compter jusqu'à 5") 
    i = 0
    for i in range(5):
        i = i + 1
        print (f"{i}")


def exercice14(): 

    print("Exercice  14: Table de 2") 
    for i in range(1,6):    # i va de 1 à 5
        print (f"2*{i}={2*i}")
        
def exercice15(): 

    print("Exercice  15: Périmètre du carré")
    p = float(input("Entrer la longeur d'un côté du carré :"))
    print (f"Le périmètre du carré est {p*4}")

def exercice16(): 

    print("Exercice  16:  Aire du carré")
    côté = float(input("Donne la longeur du Côté :"))
    aire = côté ** 2
    print (f"Pour {côté} de côté, l'aire est: {aire}")


def exercice17(): 

    print("Exercice  17:  Conversion euros → dollars")
    montant = float(input("Entrez le montant en € :"))
    conversion = montant * 1.1
    print (f"Taux fixe : 1€ = 1.1$.     {montant}€ = {conversion}$")



def exercice18(): 

    print("Exercice  18:  Conversion minutes → secondes")
    min = float(input("Entrez un temps en minutes :"))
    print (f"{min} minutes = {min *60} secondes")

def exercice19(): 

    print("Exercice  19:  Prix TTC")
    montant = float(input("Entrez le montant HT :"))
    print (f"TVA = 20%. {montant} HT = {montant*0.2} TTC")

def exercice20(): 

    print("Exercice  20:  Message personnalisé")
    nom = input("Met ton nom :")
    age = input("met ton age :")
    print (f"Salut mon mignion, je sais tout de toi.\n{nom} je sais aussi que t'as {age}. N'ai pas peur mon petit, ça va bien se passer, on va s'occuper de toi c'est juste une question de temps :d")


def exercice21(): 

    print("Exercice  21:  Test positif/négatif")
    nb = float(input("Entrez nombre :"))
    if nb < 0 :
        print ("négatif")
    else:
        print("positif")

def exercice22(): 

    print("Exercice  22:  Majeur ou mineur")
    age = float(input("Entrez age :"))
    if age < 18 :
        print ("mineur")
    else:
        print("majeur")

def exercice23(): 

    print("Exercice  23:  Note validée")
    note = float(input("Entrez note :"))
    if note >= 10 :
        print ("validé")
    else:
        print("non validé")

def exercice24(): 

    print("Exercice  24:  Le plus grand de deux")
    a = float(input("entre 1 nombre :"))
    b = float(input("entre un 2em nb :"))
    if a > b: 
        print ("{a} > {b}")
    else:
        print ("{a} < {b}")


def exercice25(): 

    print("Exercice  25:  Ordre croissant")
    a = float(input("entre 1 nombre :"))
    b = float(input("entre un 2em nb :"))
    if a < b: 
        print ("{a}, {b}")
    else:
        print ("{b}, {a}")

def exercice26(): 

    print("Exercice  26:  divisible par 5")
    nb = float(input("entre 1 nombre :"))
    if nb % 5 == 0:
        print(f"{nb} est divisible par 5")
    else:
        print(f"{nb} n'est pas divisible par 5")

def exercice27(): 

    print("Exercice  27:  Catégorie d'âge")
    age = int(input("Entre ton âge : "))
    if age < 12:
        print(f"{age} ans → Enfant")
    elif 12 <= age <= 17:
        print(f"{age} ans → Adolescent")
    else:
        print(f"{age} ans → Adulte")

def exercice28(): 

    print("Exercice  28:  Température de l'eau")
    temp = int(input("entrez température"))
    if temp < 0: 
        print (f("{temp}---> glace "))
    elif 0 <= temp <=100:
        print (f"{temp}---> eau liquide")
    else: 
        print(f"{temp} --->vapeur")


def exercice29(): 

    print("Exercice  29:  Mention au bac")
    mention = float(input("entrez note :"))
    if mention < 8:
        print (f"{mention} ---> recalé")
    elif 8 <= mention <=11:
        print (f"{mention} ---> passable")
    elif 11 <= mention <=14:
        print (f"{mention} ---> bien")
    elif mention > 17:
        print (f"{mention} ---> très bien")

def exercice30(): 

    print("Exercice  30:  Compter de 1 à N :")
    n = int(input("entrez un nombre"))
    for n in range(1,n+1):
        print(f"n = {n}")







def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix== "4":
        exercice4()
    elif choix== "5":
        exercice5()
    elif choix== "6":
        exercice6()
    elif choix== "7":
        exercice7()
    elif choix== "8":
        exercice8()
    elif choix== "9":
        exercice9()
    elif choix== "10": 
        exercice10() 
    elif choix== "11": 
        exercice11() 
    elif choix== "12": 
        exercice12() 
    elif choix== "13": 
        exercice13() 
    elif choix== "14": 
        exercice14() 
    elif choix== "15": 
        exercice15() 
    elif choix== "16": 
        exercice16() 
    elif choix== "17": 
        exercice17() 
    elif choix== "18": 
        exercice18() 
    elif choix== "19": 
        exercice19() 
    elif choix== "20": 
        exercice20()
    elif choix== "21": 
        exercice21()
    elif choix== "22": 
        exercice22()
    elif choix== "23": 
        exercice23()
    elif choix== "24": 
        exercice24()
    elif choix== "25": 
        exercice25()
    elif choix== "26": 
        exercice26()
    elif choix== "27": 
        exercice27()
    elif choix== "28": 
        exercice28()
    elif choix== "29": 
        exercice29()
    elif choix== "30": 
        exercice30()
    elif choix== "31": 
        exercice31()
    elif choix== "32": 
        exercice32()





    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()