# Security-Projet_RSA_Affine_Cipher_Decipher
[French] Projet de Chiffrement-Déchiffrement RSA et Affine     
[English] RSA and Affine Encryption-Decryption Project  (First it will be the French README then the English README After)   


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

## [Tutoriel / Tutorial]

#### ÉTAPE 1 : Dans la partie 1  RSA lancer le programme  / STEP 1: In part 1 RSA launch the program
<div align="center">
  <img width="267" alt="image" src="https://github.com/D-TheProgrammer/Security-Projet_RSA_Affine_Cipher_Decipher/assets/151149998/da6affdc-15cd-42ae-b13d-22376a908413">
</div>

#### ÉTAPE 2 : Dans la partie 2 Affine lancer le programme   / STEP 2: In part 2 Affineafter launch the program
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
