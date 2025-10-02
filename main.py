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
    division = (f"le résultat est {division}")

def exercice12(): 

    print("Exercice  12: Afficher 5 fois") 
    for i in range(5): 
    print ("Hello")
 
 


  











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





    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()