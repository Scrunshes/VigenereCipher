import VigenereCipher


while True:
    try:
        cryptanalysis = int(input("Entrer 1 si vous voulez calculer l'indice de coincidence d'un texte :"))
    except ValueError:
        print("Veuillez présenter un choix correct.")

    if cryptanalysis == 1:
        try:
            cipher = str(input("Enter le message en question :"))
        except ValueError:
            print("Veuillez entrer un message correct.")

        print("L'indice de coincidence de votre message est de ", VigenereCipher.cryptanalysis(cipher))
        continue

    try:
        key = str(input('Présenter la clé à utiliser :'))
    except ValueError:
        print('Veuillez présenter une clé correcte !')

    try:
        action = int(input('Entrer 0 pour chiffrer un message et 1 pour déchiffrer :'))
    except ValueError:
        print("Veuillez demander une action correcte.")

    if action == 0:
        try:
            message = str(input('Entrer le texte à chiffrer :'))
        except ValueError:
            print("Veuiller présenter un message correct !")

        print("Votre message chiffré est : ", VigenereCipher.encrypt(message, key))

    elif action == 1:
            try:
                message = str(input('Entrer le texte à déchiffrer :'))
            except ValueError:
                print("Veuillez présenter un message correct.")

            print("Votre message déchiffré est", VigenereCipher.decrypt(message, key))
    else:
        print("Action non reconnu.")