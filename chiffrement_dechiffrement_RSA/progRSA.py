from Crypto.Util.number import *
from math import gcd
from random import randint

print("Generation de Cle en fonction du nombre de bits : ")
def gen_rsa_keypair(tailleEnBit):
    
    p = getPrime(tailleEnBit //2 ) #Pour avoir une division entiere
    q= getPrime(tailleEnBit //2)
    n = p * q
    phi_n =(p - 1)*(q - 1)
    
    #e = getPrime(tailleEnBit //2) #Conseil du prof d'utiliser e = 65537 car il a tres peu de chance de ne pas foncntionner
    e= 65537
    #si ca respecte pas les condition lié a "e"
    while not ( gcd(e, phi_n ) ==1 or gcd(e, phi_n )== -1):
        e = randint(3,100000) #on regenere un nouveau "e" tant que ca respecte pas les condition

    d = inverse(e,phi_n)
    
    print("n :",n)
    print("p :",p)
    print("q :",q)
    
    print("phi_n : ",phi_n)
    print("e :",e)
    print("d :",d)

    return ((e,n),(d,n))
    


bits=60
paire_cle=gen_rsa_keypair(bits)
print("cle publique :", paire_cle[0])
print("cle prive :",paire_cle[1])


#---------------------------------------------
#----------CHIFFREMENT DECHIFFREMENT RSA------
#---------------------------------------------
print("--------------------------------")
print("Exemple de Chiffrement / Dechiffrement RSA :")
message_A_chiffre= 9
#pairCleEx = [(3,10),(587,10)]
print("Message a chiffre : ",message_A_chiffre)

#---Chiffrement-----
def chiffrement_rsa( message,paire_cle):
    c= pow(message,paire_cle[0][0],paire_cle[0][1])
    return c

mot_chiffre=chiffrement_rsa(message_A_chiffre ,paire_cle)
print("mot_chiffre :",mot_chiffre)


#---DECHIFFREMENT -----
def dechiffrement_rsa( m_chiffre,paire_cle):
    m_dechiffre= pow(m_chiffre,paire_cle[1][0],paire_cle[1][1])
    return m_dechiffre

mot_dechiffre=dechiffrement_rsa(mot_chiffre ,paire_cle)
print("mot_dechiffre :",mot_dechiffre)

print("--------------------------------")

#----------------------------------------------------------------------
#----CHIFFREMENT DECHIFFREMENT RSA CHAINE DE CARACTERE __ ENC DEC------
#----------------------------------------------------------------------
print("RSA Enchiffrement Dechiffrement (enc dec) :\n")
def rsa_enc(chaine_de_caractere,  key ):
    #Pour plus de simplicite la chaine de charactere est stocker dans une liste
    msg_A_chiffrer_enc=[]
    msg_A_chiffrer_enc = [int.from_bytes(chaine_de_caractere.encode('utf-8'), 'big')]
    print("VERSION NOMBRE ",msg_A_chiffrer_enc)
    
    #Si le message est plus long que n on le decoupe 
    if (msg_A_chiffrer_enc[0] > key[0][1]):
        print("DANGER !! ATTENTION Mot plus grand que n , decoupage Pour Chiffrage")
        temp_reletrage=  msg_A_chiffrer_enc[0].to_bytes((msg_A_chiffrer_enc[0].bit_length() + 7) // 8, 'big').decode('utf-8')
        print("Separation du mot : ",temp_reletrage)

        #On le decoupe en chaine de 4 caracteres
        result_reletrage = []
        for i in range(0, len(temp_reletrage), 4):
            result_reletrage.append(temp_reletrage[i : i + 4])
        print("on travail a partir de : ",result_reletrage)
    else:
        result_reletrage=msg_A_chiffrer_enc
        result_reletrage[0]=chaine_de_caractere


    #Pour Resumer Ici on travail encore avec des lettre et on les transforme ensuite en nombre 
    chiffrage_final=[]
    for i in result_reletrage:
        
        #Donc ici on converti en Nombre afin de chiffrer
        msg_A_chiffrer_enc_bout_liste = int.from_bytes(i.encode('utf-8'), 'big')
        msg_liste_chiffre=chiffrement_rsa(msg_A_chiffrer_enc_bout_liste,key)

        chiffrage_final.append(msg_liste_chiffre)
        
    return chiffrage_final

#POUR LA CLE On reutilise celle precedemmanet cree aleatoirement sur 60 BITS 
cle_alea=paire_cle
message_octet="bonjour LA FAMILLE"
print("Message  a chiffrer : ",message_octet)
resultat_chiffrement_octet=rsa_enc(message_octet,cle_alea)
print("\n")
print("chiffrage final : ",resultat_chiffrement_octet)

#---------- RSA DEC-------------
def rsa_dec(chaine_de_chiffre,  key ):
    Dechiffrage_final=[]

    for i in chaine_de_chiffre:
        #print("ca cest i",i)
        
        msg_liste_dechiffre=dechiffrement_rsa(i,key)

        #Donc ici on converti en Nombre afin de chiffrer
        msg_A_chiffrer_dec_bout_liste =  msg_liste_dechiffre.to_bytes((msg_liste_dechiffre.bit_length() + 7) // 8, 'big').decode('utf-8')
        #print("pour un i on dechiffre", msg_A_chiffrer_dec_bout_liste)

        Dechiffrage_final.append(msg_A_chiffrer_dec_bout_liste)
        chaine_de_caracteres = ''.join(Dechiffrage_final) #transforme la lisre en mot

    return chaine_de_caracteres

resultat_Dechiffrement_octet=rsa_dec(resultat_chiffrement_octet,cle_alea)
print("Dechiffrage final :", resultat_Dechiffrement_octet)


#-----------------------------------------
#----BAM BAM SIMULATION ALICE x BOB ------
#-----------------------------------------
print("\n------------------------------")
print("-----SIMULATION ALICE BOB--------")
print("--------------------------------")
messageAliceD="Im Alice"
print("Message d'Alice : ", messageAliceD)
messageBob="My name is Rob Freakin ROBERTS"
print("Message de Bob : ",messageBob)
print("\n")

#POUR LA CLE ON UTILISE CELLE PRECEDEMMENT CREE 
#cle_exempleAliceBob = gen_rsa_keypair(110)
cle_exempleAliceBob = paire_cle

mot_chiffreAlice=rsa_enc(messageAliceD ,cle_exempleAliceBob)
print("\nmot_chiffrer Alice :",mot_chiffreAlice,"\n")

mot_chiffreBob=rsa_enc(messageBob ,cle_exempleAliceBob)
print("\nmot_chiffrer Bob :",mot_chiffreBob)

mot_DEchiffre_pourBob=rsa_dec(mot_chiffreAlice ,cle_exempleAliceBob)
print("Message Dechiffrer que recoit Bob venant de Alice :",mot_DEchiffre_pourBob)

mot_DEchiffrepourAlice=rsa_dec(mot_chiffreBob ,cle_exempleAliceBob)
print("Message Dechiffrer que recoit Alice venant de Bob : ",mot_DEchiffrepourAlice)
