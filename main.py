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


def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif == "2":
        exercice2()
    elif == "3":
        exercice3()
        elif == "4":
        exercice4()

    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()