from math  import *
import random

def chiffrer_rsa(d, n, nombre):
    return expo_rapide(nombre, d, n) 

def expo_rapide(a,k,n):
    x= a%n
    if (k==0):
        return 1
    elif (k%2==0):
        aux= expo_rapide(x,k//2,n)
        res= (aux**2)%n
        return res
    else:
        aux= expo_rapide(x,(k-1)//2,n)
        res= (x*(aux**2))%n
        return res


def nb_premier(nombre):
    # On verifie les nombre premier
    for i in range (2, int(sqrt(nombre)+1)): #Car le sqrt ressort un float automamtiquement
        if(nombre !=0 and  nombre % i==0 and nombre != i): 
            return 0
    # si pas bon
    return 1 

def genAleaPremier(borne,max):
    # On genere un nombre aleatoire de la borne jusqua 10 000 
    nombre_aleatoire = random.randint(borne, max)
    test=nb_premier(nombre_aleatoire)
    if (test == 0):
        return genAleaPremier(borne, max)
    else:
        return nombre_aleatoire

def pgcd_ite(a,b):
 #Renvoie le PGCD des entiers a et b, version iterative
 while (b != 0):
    r= a%b
    a= b
    b= r
 return a


def inverse_mod(a, b):
    nb_a=nb_premier(a)
    nb_b= nb_premier(b)
    #sil sont pas premier return 0
    if ( nb_a !=1 and nb_b!=1 ):
        return 0
    
    #sil sont pas premier entre eux 0
    pgcd = pgcd_ite(a, b)
    if (pgcd != 1):
        return 0
    
    #on test pour voir linverse mod
    for x in range(b):
        if ( ((a*x) % b) == 1):
            return x
  

def dechiffrer_rsa(e, n, nombre_chiffre):
    nombre_dechiffre = expo_rapide(nombre_chiffre, e, n)
    return nombre_dechiffre


#______________Modification apporté pour cet partie uniquement_____________

#Ici la fonction Alea A ETE CHANGE elle prend en min le nombre 1 
# et en max le nombre x quon veut , donc ici 55 qui correspond a n 

n=0
while (n!=55) :
    p=genAleaPremier(1, 55)
    q=genAleaPremier(1, 55)

    #clé publique n
    n=p*q

print("p:",p," q:",q)
print("n:",n)

#création de d
e = 3
phi = (p-1) * (q-1)
while ( pgcd_ite(e, phi) != 1 ):
    e += 2
d= inverse_mod(e, phi)

c = 3
print("la clé de chiffrement de la consigne c est:",c)
print("la clé de DECHIFFREMENT TROUVEE d est:",d)


nombre= 13
print("\nceci est le nombre : ",nombre)


nb_chiffre=chiffrer_rsa(c,n,nombre)
print("ceci est le nombre chiffrer : ",nb_chiffre)


nombre_dechiffre = dechiffrer_rsa(d, n, nb_chiffre)
print("ceci est le nombre dechiffrer :", nombre_dechiffre)
