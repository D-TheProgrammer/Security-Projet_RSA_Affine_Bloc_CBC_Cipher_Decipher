# Security-Projet_RSA_Affine_Bloc_CBC_Cipher_Decipher
[French] Projet de Chiffrement-Déchiffrement RSA et Affine et bloc CBC  
[English] RSA, Affine, Bloc CBC Encryption-Decryption Project  (First it will be the French README then the English README After)   


#### SOMMAIRE / SUMMARY
- [Présentation en francais / Presentation in French](#presentation-en-francais)
- [Présentation en anglais / Presentation in English](#english-presentation)
- [Tutoriel dans les deux langues / Tutorial in both languages](#tutoriel--tutorial)

## [PRESENTATION EN FRANCAIS]
Projet de sécurité basé sur plusieurs méthodes de chiffrement.

Ce projet est divisé en plusieurs parties, disponibles dans différents dossiers et se basant sur des thématiques spécifiques.

### Partie 1 : RSA 
Le programme met en œuvre le chiffrement RSA, un système de cryptographie asymétrique. Ce système utilise une paire de clés : une clé publique pour chiffrer les données et une clé privée pour les déchiffrer. Les clés sont générées à partir de deux grands nombres premiers, et le chiffrement est effectué en utilisant des opérations de puissance modulaire. Le programme comprend les étapes suivantes :

- Vérification de la primalité d'un nombre.
- Génération d'un nombre premier aléatoire.
- Calcul de l'inverse modulaire.
- Génération des clés publiques et privées.
- Chiffrement d'un message avec la clé publique.
- Déchiffrement d'un message avec la clé privée.

> [!NOTE]
> Pour installer la bibliothèque `Crypto`:
> ```bash
> pip install pycryptodome
> ````


> [!TIP]
> Pour utiliser le programme:
> ```bash
> python3 progRSA.py
> ````




### Partie 2 : Chiffrement-Déchiffrement Affine  
Cette partie met en œuvre un système de chiffrement affine, où chaque lettre d'un message est transformée individuellement en utilisant une fonction affine modulaire. Les lettres de l'alphabet sont représentées par les nombres de 0 à 29 (car c'est un alphabet de longueur 29, incluant les  espaces, une virgule et un point dans l'alphabet il y a  " " , ".",  " , ").  
La fonction de chiffrement est de la forme fa,b(x) = ax + b mod 29, où a et b sont des entiers et x est l'indice de la lettre dans l'alphabet. Par exemple, avec a = 3 et b = 11, la lettre A est transformée en la lettre L. La fonction de chiffrement est bijective lorsque a est premier avec 29, permettant le déchiffrement.

Le programme comprend les étapes suivantes :

- Une fonction pour chiffrer un texte en utilisant une clé de chiffrement donnée.
- Un exemple de chiffrement d'une phrase choisi par l'utilisateur avec une clé donnée.
- Le déchiffrement du message donné avec une clé de chiffrement spécifique. 


> [!TIP]
> Pour utiliser le programme:
> ```bash
> python3 prog_chiffrement_dechiffrement_affine.py
> ````


### Partie 3 : Chiffrement-Déchiffrement par Bloc avec ToyCipher et avec CBC 

Implémentation d'un chiffrement par bloc à deux tours appelé ToyCipher avec une clé de 8 bits et une taille de bloc de 4 bits. Il contient des fonctions pour le chiffrement et le déchiffrement de données, ainsi que des opérations sur des fichiers, le chiffrement se fait en deux tours d'opérations sur les données. Chaque tour comprend l'ajout de la clé correspondante à l'état des données, suivi d'une permutation. Le déchiffrement, quant à lui, inverse ce processus en effectuant les tours dans l'ordre inverse, en commençant par les opérations inverses de la permutation, suivies de l'annulation de l'ajout de la clé  Pour cela le code utilise des modes d'opération de chiffrement, en particulier le mode CBC (chiffrement en mode chaîné), pour renforcer la sécurité du chiffrement et vérifie son fonctionnement . 

> [!TIP]
> Pour utiliser le programme:
> ```bash
> python3 chiffrement_bloc_toycipher_cbc.py
> ````




## [ENGLISH PRESENTATION]
Security project based on several encryption methods.

This project is divided into several parts available in several files based on a theme.

### Part 1: RSA
The program implements RSA encryption, an asymmetric cryptography system. This system uses a pair of keys: a public key to encrypt the data and a private key to decrypt it. Keys are generated from two large prime numbers, and encryption is performed using modular power operations. The program includes the following steps:

- Checking the primality of a number.
- Generation of a random prime number.
- Calculation of the modular inverse.
- Generation of public and private keys.
- Encryption of a message with the public key.
- Decryption of a message with the private key.

> [!NOTE]
> To install the library `Crypto`:
> ```bash
> pip install pycryptodome
> ````

> [!TIP]
> To use the program:
> ```bash
> python3 progRSA.py
> ````


### Part 2: Affine Encryption-Decryption
This part implements an affine encryption system, where each letter of a message is transformed individually using a modular affine function. The letters of the alphabet are represented by the numbers 0 to 29 (because it is an alphabet of length 29, including spaces, a comma and a period in the alphabet there is " " , ".", " , ").
The encryption function is of the form fa,b(x) = ax + b mod 29, where a and b are integers and x is the index of the letter in the alphabet. For example, with a = 3 and b = 11, the letter A is transformed into the letter L. The encryption function is bijective when a is prime with 29, allowing decryption.

The program includes the following steps:

- A function to encrypt text using a given encryption key.
- An example of encryption of a sentence chosen by the user with a given key.
- Decryption of the given message with a specific encryption key.


> [!TIP]
> To use the program:
> ```bash
> python3 prog_encryption_decryption_affine.py
> ````


### Part 3: Block Encryption-Decryption with ToyCipher and CBC

Implementation of a two-round block encryption called ToyCipher with an 8-bit key and a block size of 4 bits. It includes functions for data encryption and decryption, as well as file operations. Encryption is done in two rounds of operations on the data. Each round involves adding the corresponding key to the data state, followed by a permutation. Decryption, on the other hand, reverses this process by performing the rounds in reverse order, starting with the inverse permutation operations, followed by canceling out the key addition. The code utilizes encryption operation modes, particularly CBC mode (Cipher Block Chaining), to enhance encryption security and verifies its functionality.

> [!TIP]
> To use the program :
> ```bash
> python3 chiffrement_bloc_toycipher_cbc.py
> ````


## [Tutoriel / Tutorial]

#### ÉTAPE 1 : Dans la partie 1  RSA lancer le programme  / STEP 1: In part 1 RSA launch the program
[FRENCH] Le programme affiche d'abord un ensemble d'informations liées à la clé publique et privée.  
[ENGLISH] The program first displays a set of information related to the public and private key.   
<div align="center">
  <img width="294" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Bloc_CBC_Cipher_Decipher/assets/151149998/1c913524-ab24-4906-a346-88890b0a1268">
  
</div>

[FRENCH] Ensuite, le programme présente un exemple de chiffrement/déchiffrement  
[ENGLISH] Next, the program demonstrates an example of encryption/decryption  
<div align="center">
  <img width="315" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Bloc_CBC_Cipher_Decipher/assets/151149998/42bdee12-ec2c-4eaa-986b-fe096f170708">
</div>


[FRENCH] Une phrase est alors chiffrée puis déchiffrée  
[ENGLISH] A phrase is then encrypted and decrypted  
<div align="center">
  <img width="315" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Bloc_CBC_Cipher_Decipher/assets/151149998/b013788e-c05f-43dd-8dbf-8c661f8c6669">
</div>

[FRENCH] Enfin, il est possible de voir le chiffrement RSA appliqué à une conversation entre deux personnes       
[ENGLISH] Finally, it is possible to see RSA encryption applied to a conversation between two people    
<div align="center">
<img width="435" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Bloc_CBC_Cipher_Decipher/assets/151149998/44c23214-adcc-4730-a474-11f6073bd133">
</div>



#### ÉTAPE 2 : Dans la partie 2 Affine lancer le programme   / STEP 2: In part 2 Affine after launch the program
[FRENCH] L'utilisateur pourra choisir la clé privé et publique ( la clé privé ne peut etre le chiffre 0)   
[ENGLISH] The user can choose the private and public key (the private key cannot be the number 0)  
<div align="center">
  <img width="294" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Cipher_Decipher/assets/151149998/b36429a0-9de6-4806-b336-89f80abe053d">
</div>

[FRENCH] Après cela, l'utilisateur pourra entrer une phrase à chiffrer. Elle sera automatiquement déchiffrée par la suite.     
[ENGLISH] After that, the user will be able to enter a phrase to encrypt. It will be automatically decrypted afterwards.  
<div align="center">
  <img width="356" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Cipher_Decipher/assets/151149998/4be02451-934e-45fa-ac1a-c706bed2ce40">
</div>

[FRENCH] Enfin les informations de la clé sont affichés avec la phrase chiffré et la phrase déchiffré   
[ENGLISH] Finally the key information is displayed with the encrypted phrase and the decrypted phrase.   
<div align="center">
  <img width="391" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Cipher_Decipher/assets/151149998/8bad188b-ce51-4478-a93e-c5de87356e2e">
</div>

#### ÉTAPE 3 : Dans la partie 3 Bloc lancer le programme   / STEP 2: In part 2 Bloc after launch the program
[FRENCH] Le code utilise un fichier texte pour effectuer d'abord un chiffrement par bloc avec ToyCipher. Ensuite, il affiche la clé utilisée. Enfin, il montre le contenu du fichier chiffré, ainsi que les étapes d'encodage et de décodage  
[FRENCH] The code uses a text file to first perform block encryption with ToyCipher. Then, it displays the key used. Finally, it shows the content of the encrypted file, as well as the encoding and decoding steps.

<div align="center">
  <img width="615" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Cipher_Decipher/assets/151149998/6b4d243a-3431-4481-9e83-7252e5c39ad9">
</div>
