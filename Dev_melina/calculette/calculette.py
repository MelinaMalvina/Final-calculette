#coding:utf-8

""" opérateurs en python : 	+ (addition)
							- (soustraction)
							/ (division)
							% (modulo) -> reste d'une division


Variable = variable + B
Variable += B							
"""



print ("Calculatrice") 

premiere_valeur = input ("saisir une peremiere valeur :")
seconde_valeur = input ("saisir une seconde valeur :")

#Resultat = float(premiere_valeur) + float(seconde_valeur) 

ADDITION = 1;
SOUSTRACTION = 2;
MULTIPLICATION = 3;
DIVISION = 4;

choixUtilisateur = input("Entrer votre choix \n(1 Pour additioner; 2 pour soustraire ; 3 pour multiplier ou 4 pour diviser): ") 
op = input("Entrer votre choix (1 ; 2 ; 3 ou 4): ")

switch (op) {
            case ADDITION: print (premiere_valeur + seconde_valeur);
                     break;
            case SOUSTRACTION: print (premiere_valeur - seconde_valeur);
                     break;
            case MULTIPLICATION: print (premiere_valeur * seconde_valeur);
                     break;
            case DIVISION: print (premiere_valeur / seconde_valeur);
                     break;
            default: print ("Vous n'avez pas selectionnez la bonne valeur");
                     break; 
                     }

print ("le resulat est : ", int(Resultat) )



