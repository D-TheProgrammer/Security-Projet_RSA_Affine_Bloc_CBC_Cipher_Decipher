
S=[12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]

#--------------------------------------------------------
#-----------------ENC x ENC BYTE-------------------------
#--------------------------------------------------------
def round (m,sousKey):
    t = m ^ sousKey
    return S[t] #on retourne la valeur a lindice

def enc(m,Key):
    #La clé est decimal donc on la transforme en Bin et on la separe
    #en deux partie de 4 bit
    Key_inBits=bin(Key)
    Key_inBits=Key_inBits[2:].zfill(8)
    K0=int(Key_inBits[:4],2)
    K1=int(Key_inBits[4:],2)

    m_modifie=round(m,K0)
    return round(m_modifie,K1)


def enc_byte(octet,key):
    nibble_droite=octet & 0b00001111
    #prend la partie gauche de l'octet quon decale a droite
    nibble_gauche= octet>>4

    #chiffre chaque partie
    chiffre_nib_droi=enc(nibble_droite,key)
    chiffre_nib_gau=enc(nibble_gauche,key)

    #on decale a gauche le nibble gauche car il a ete decalé a droite
    chiffre_nib_gau= chiffre_nib_gau <<4
    #print(chiffre_nib_gau)

    #On reuni les deux partie de 4 bit sous la forme dun octet 
    #le tout dans lordre
    resulat_2nibles_enc = chiffre_nib_gau + chiffre_nib_droi
    return resulat_2nibles_enc


#-----------------------------------------------
#------------DEC  x  DEC BYTE-------------------
#-----------------------------------------------

def round_back(m_chiffre,sousKey):
    i=0
    while (S[i] != m_chiffre):
        i=i+1
    t = i ^ sousKey
    return t #on retourne l'indice qui contient la valeur

def dec(m_chiffre,Key):
    Key_inBits=bin(Key)
    Key_inBits=Key_inBits[2:].zfill(8)
    K0=int(Key_inBits[:4],2)
    K1=int(Key_inBits[4:],2)

    m_modifie_back1=round_back(m_chiffre,K1)

    return round_back(m_modifie_back1,K0)

def dec_byte(octet,key):
    nibble_droite=octet & 0b00001111
    #prend la partie gauche de l'octet quon decale a droite
    nibble_gauche= octet>>4

    #chiffre chaque partie
    chiffre_nib_droi=dec(nibble_droite,key)
    chiffre_nib_gau=dec(nibble_gauche,key)

    #on decale a gauche le nibble gauche car il a ete decalé a droite
    chiffre_nib_gau= chiffre_nib_gau <<4
    #print(chiffre_nib_gau)

    #On reuni les deux partie de 4 bit sous la forme dun octet 
    #le tout dans lordre
    resulat_2nibles_enc = chiffre_nib_gau + chiffre_nib_droi
    return resulat_2nibles_enc



#---------------------------------------------
#--------------ENC FILE-----------------------
#---------------------------------------------
def enc_file(Tableau_Octet,key):
    nom_de_fichier2="test_enc.txt"
    g=open(nom_de_fichier2,"wb")
    temp=[]    
    for i in Tableau_Octet:
        temp.append(enc_byte(i,key))
        #print(temp)
    
    
    g.write(bytearray(temp))
    g.close()



#-----------------------------------------------------------------------------
#-------VERIFICATION ALGO CHIFFREMENT DECHIFFREMENT AVEC FICHIER TEST---------
#-----------------------------------------------------------------------------
#octet_en_param= 0b10100011
print("\nVERIFICATION lgo chiffrement dechiffrement par octet dun fichier :")

cle= 144 #CLE NON SEPARER EN K0 ET K1 (donc veuillez convertir en faisant Par exemple K1 : 1111  K0 :0101  donc K= 1111 0101)
print("Cle utiliser avec les Deux Cle NON SEPARER : ",cle)


#ouverture du fichier test.txt en Mode NORMAL
nom_de_fichier0="test.txt"
fichier0 = open(nom_de_fichier0,"r")
T0= fichier0.read() #tableau d'octet
print("Lecture du fichier Test en mode NORMAL : ",T0)

#ouverture du fichier test.txt en Mode RB
nom_de_fichier="test.txt"
fichier = open(nom_de_fichier,"rb")
T= fichier.read() #tableau d'octet
print("Lecture du fichier Test en mode RB : ",T)

#CHIFFRAGE DU FICHIER 
enc_file(T,cle)


#Affichage du chiffrage du Fichier Test de l'enonce
nom_de_fichier_enc_test="test_enc.txt"
fichier_enc_test = open(nom_de_fichier_enc_test,"rb")
T_enc_test= fichier_enc_test.read() #tableau d'octet
print("Lecture du fichier Test ENCODE en mode RB : ",T_enc_test)

nom_de_fichier_enc_testRB="test_enc.txt"
fichier_enc_testRB = open(nom_de_fichier_enc_testRB,"r")
T_enc_testRB= fichier_enc_testRB.read() #tableau d'octet
print("Lecture du fichier Test ENCODE en mode NORMAL : ",T_enc_testRB)
print("--------------------------------------------------")



#---------------------------------------------------------------
#---------------PARTIE ENC : DEC FILE CBC  ---------------------
#---------------------------------------------------------------

print("\nPour le dernier exercice nous allons realiser un chiffrage CBC !!! ")


#Cle et Vecteur Init utiliser 
cle= 144 #CLE NON SEPARER EN K0 ET K1
vecteurInit=22
print("Cle utiliser : ",cle)
print("VecteurInit : ",vecteurInit)


#--------CHIFFRAGE CBC : EXPLICATION--------------------
#But de code : 
# Faire un Xor avec un chiffre clair et un vecteur init
# entrer le resultat avec une cle pour encode
#mettre le resultat dans la liste des resultat et lenvoyer
#afin de Xor avec le prochain chiffre clair a la place du vecteur init 
# repeat etape 2 a 4

def enc_file_cbc(octet_en_param_cbc,vecteurInit,Key):
    nom_de_fichier2="fichier_A_cbc_enc.txt"
    g=open(nom_de_fichier2,"wb")

    ensemble_Bloc_Chiffre=[]
    #print("Premier Elem ",octet_en_param_cbc[0])
    #print("Charac Premier Elem ",chr(octet_en_param_cbc[0]))

    VecXorClair= vecteurInit ^ octet_en_param_cbc[0]
    ensemble_Bloc_Chiffre.append(enc_byte(VecXorClair,Key))
    
    for i in range (1,len(octet_en_param_cbc)):
        VecXorClair= ensemble_Bloc_Chiffre[i-1] ^ octet_en_param_cbc[i]
        ensemble_Bloc_Chiffre.append(enc_byte(VecXorClair,Key))
        
    g.write(bytearray(ensemble_Bloc_Chiffre))
    g.close()



#--------deCHIFFRAGE CBC : EXPLICATION--------------------

#But de code : Faire l'inverse du chiffrement 
# le premier octet chiffre doit etre decodé avec la cle 
#Son resultat va etre XOR avec la vecteur d'initialisation
#mettre le resultat dans la liste des resultat et lenvoyer
#Afin de dechiffrer le prochain octet chiffrer qui va etre XOR (donc avec le octet chiffrrer precedent) 
# a la place du vecteur init

def dec_file_cbc(octet_en_param_cbc,vecteurInit,Key):
    nom_de_fichier4="fichier_A_cbc_dec.txt"
    g=open(nom_de_fichier4,"wb")

    ensemble_Bloc_DeChiffre=[]
    
    #print("Premier Elem Chiffrer ",octet_en_param_cbc[0])
    #print("Charac Premier Elem chiffrer ",chr(octet_en_param_cbc[0]))

    
    for i in range (len(octet_en_param_cbc)):
        res_temp=dec_byte(octet_en_param_cbc[i],Key)
        
        VecXorClair_dec= vecteurInit ^ res_temp
        ensemble_Bloc_DeChiffre.append(VecXorClair_dec)

        vecteurInit = octet_en_param_cbc[i]
        
    #VecXorClair= ensemble_Bloc_Chiffre[i] ^ ord(octet_en_param_cbc[len(octet_en_param_cbc) -1 ])
    #ensemble_Bloc_Chiffre.append(enc_byte(VecXorClair,Key))


    g.write(bytearray(ensemble_Bloc_DeChiffre))
    g.close()



#----------------------------------------------------------------------------
#--------AFFICHAGE DU RESULTAT DU CHIFFRAGE / DECHIFFRAGE CBC ---------------
#----------------------------------------------------------------------------

print("\nEncodage du fichier en mode CBC :")
nom_de_fichier2="fichier_A_cbc.txt"
fichier2 = open(nom_de_fichier2,"r")
T2= fichier2.read() #tableau d'octet
print("Le fichier A encode en CBC (donc pas encore fait) est composé en mode NORMAL de : ",T2)

nom_de_fichier2_RB="fichier_A_cbc.txt"
fichier2_RB = open(nom_de_fichier2_RB,"rb")
T2_RB= fichier2_RB.read() #tableau d'octet
print("Le fichier A encode en CBC (donc pas encore fait) est composé en mode RB de : ",T2_RB)



#CHIFFRAGE DU Fichier en mode CBC 
#enc_file_cbc(octet_en_param_cbc,vecteurInit,cle)
enc_file_cbc(T2_RB,vecteurInit,cle)
print("\nChiffrage du fichier en mode CBC :")

nom_de_fichier3="fichier_A_cbc_enc.txt"
fichier3 = open(nom_de_fichier3,"r")
T3= fichier3.read() #tableau d'octet
print("Le fichier Chiffrer en CBC est composé en mode NORMAL de : ",T3)

nom_de_fichier3_RB="fichier_A_cbc_enc.txt"
fichier3_RB = open(nom_de_fichier3_RB,"rb")
T3_RB= fichier3_RB.read() #tableau d'octet
print("Le fichier Chiffrer en CBC est composé en mode RB de : ",T3_RB)



#DEchiffrage DU Fichier en mode CBC 
#enc_file_cbc(octet_en_param_cbc,vecteurInit,cle)
dec_file_cbc(T3_RB,vecteurInit,cle)

#Print de la Preuve de Reussite 
print("\nDECHIFFRAGE et Verification en ouvrant le fichier avec le message qui a ete code DECODE :")
nom_de_fichier_verif="fichier_A_cbc_dec.txt"
fichier_verif = open(nom_de_fichier_verif,"r")
T_verif= fichier_verif.read() #tableau d'octet
print("Le fichier DEchiffrer en CBC est composé en mode NORMAL de : ",T_verif)

nom_de_fichier_verifRB="fichier_A_cbc_dec.txt"
fichier_verifRB = open(nom_de_fichier_verifRB,"rb")
T_verifRB= fichier_verifRB.read() #tableau d'octet
print("Le fichier DEchiffrer en CBC est composé en mode RB de : ",T_verifRB)