"""
Ethan Wong
407
un jeux ou tu peux te battre avec des monstres
"""
import random

game = True
regles = False
niveau_vie = 20
nombre_victoires = 0
nombre_defaites = 0
force_adversaire = 0
boss = 0


def dice(faces):
    return random.randint(1,faces)


def dice2(faces):
    return random.randint(1,faces)


while game:
    if not regles:
        if boss != 0 and boss % 3 == 0:
            force_adversaire = random.randint(8, 12)
            print("un monstre tres fort est apparu, c'est un boss!")

        else:
            force_adversaire = dice(10)
    else:
        if boss != 0 and boss % 3 == 0:
            print("un monstre tres fort est apparu, c'est un boss!")
            regles = False
    print(f"vous avez recontrer un monstre de {force_adversaire} force.")
    print(f"vous avez {niveau_vie}HP.")
    menu = input("""
    Que voulez-vous faire ? 
        1- Combattre cet adversaire
        2- Contourner cet adversaire et aller ouvrir une autre porte
        3- Afficher les règles du jeu
        4- Quitter la partie
    """)
    if menu == "1":
        print("vous avez attaqué")
        result = dice(6) + dice2(6)
        print(f"vous avez eu: {result} et le monstre a eu: {force_adversaire}")
        if result > force_adversaire:
            print(f"vous avez gagne, alors vous allez avoir {force_adversaire} point de HP de plus")
            niveau_vie += force_adversaire
            nombre_victoires += 1
            print(f"Ton score de Victoire et Defaites est: {nombre_victoires} VS {nombre_defaites}")
            boss += 1

        elif result  < force_adversaire:
            if boss != 0 and boss % 3 == 0:
                boss = 0
            print(f"vous avez perdu, alors vous allez avoir {force_adversaire} point de HP de moins")
            niveau_vie -= force_adversaire
            nombre_defaites += 1
            print(f"Ton score de Victoire et Defaites est: {nombre_victoires} VS {nombre_defaites}")

        elif result == force_adversaire:
            print("vous avez eu la meme resultats, alors votre Hp n'a pas change")
            print(f"Ton score de Victoire et Defaites est: {nombre_victoires} VS {nombre_defaites}")

    elif menu == "2":
        print("vous avez evite le combat, alors vous allez perdre 1 HP")
        niveau_vie -= 1
        if boss != 0 and boss % 3 == 0:
            boss = 0

    elif menu == "3":
        regles = True
        print(""" REGLES:
        Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.
        Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
        Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
        Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
        La partie se termine lorsque les points de vie de l’usager tombent sous 0.
        L’usager peut combattre ou éviter chaque adversaire, 
        dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
        """)

    elif menu == "4":
        print("Merci et au revoir...")
        game = False

    if niveau_vie <= 0:
        print(f"vous etes mort, vous avez vaincu {nombre_victoires} monstre(s).")
        exit()
        game = False