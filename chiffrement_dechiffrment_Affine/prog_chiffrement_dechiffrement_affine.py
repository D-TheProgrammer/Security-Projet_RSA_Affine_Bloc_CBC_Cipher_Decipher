from math import *
#CHIFFREMENT POUR L'ALPHABET A 29 CARAC (avec " " , ".",  ", ")
def chiffrer_aff(A, B, mot):
    alphabet29 = [" ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".",]
    new_alphabet = []

    #du coup fonction affine pour creer un nouveau alphabet de 29 carac
    for i in range(0, 29+1):
        x = i
        f = (A*x+B) % 29
        new_alphabet.append(f)
    
    #transformation afin de creer une liste avec les nouveau indice pour les lettre du mot
    new_mot = []
    for i in range(len(mot)):
        for y in range(len(alphabet29)):
            if alphabet29[y] == mot[i]:
                new_mot.append(new_alphabet[y])

    #on parcours afin de transformer les nouveau indice en lettre
    char_mot = ""
    for indice in new_mot:
        char_mot+= alphabet29[indice]

    return(char_mot)


#DECHIFFREMENT POUR L'ALPHABET A 29 CARAC (avec " " , ".",  ", ")
def dechiffrer_aff(a, b, mot_chiffre):
    alphabet29 = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", "."]

    #;calcul pour inverser l'affine
    i = 1
    a_inv = 0
    while ((i < 29) and (a_inv == 0) ):
        x=i
        if ( ((a * x) % 29 ) == 1):
            a_inv = x
        i += 1

    
    new_mot = []
    for lettre in mot_chiffre:
        i = 0
        # Recherche de l'indice de la lettre chiffrée dans l'alphabet
        while ( (i < len(alphabet29) ) and (alphabet29[i] != lettre) ):
            i += 1
        #transformation afin de creer une liste avec les nouveau indice pour les lettre du mot
        if (i < len(alphabet29) ):
            new_indice = (a_inv*(i-b))%29
            new_mot.append(new_indice)

    #on parcours afin de transformer les nouveau indice en lettre
    char_mot = ""
    for indice in new_mot:
        char_mot += alphabet29[indice]

    return (char_mot)



nb_a=4
nb_b=21


nb_a = int(input("Entrez un entier pour la clé privé : "))
while nb_a == 0 :
    nb_a = int(input("la clé privé doit etre different de 0 , ecrivez la de nouveau: "))

nb_b = int(input("Entrez un entier pour la clé publique : "))

a_chiffrer=" la clef est dans le coffre "
a_chiffrer=input("Ecrivez une phrase a chiffrer : ").lower()
print("la clé est (",nb_a,",",nb_b,")")

mot1=chiffrer_aff(nb_a, nb_b, a_chiffrer)
print("\nle chiffrement du mot '",a_chiffrer, "' sur l'alphabet 29 carac \navec un espace avant et apres la phrase est :\n'",mot1,"'")



mot2 = dechiffrer_aff(nb_a, nb_b, mot1)
print("\nle DEchiffrement du mot '",mot1, "' sur l'alphabet 29 carac \navec un espace avant et apres la phrase est :\n'",mot2,"'")
