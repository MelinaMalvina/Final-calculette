import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

valeur1 = connexion_avec_client.recv(1).decode()
print(valeur1)

operation = connexion_avec_client.recv(1).decode()
print(operation)


valeur2 = connexion_avec_client.recv(1).decode()
print(valeur2)



if operation=="+":
	connexion_avec_client.send(str(int(valeur1) + int(valeur2)).encode ())
    
elif operation=="-":
	connexion_avec_client.send(str(int(valeur1) - int(valeur2)).encode ())

elif operation=="*":
    connexion_avec_client.send(str(int(valeur1) * int(valeur2)).encode ())

	
elif operation=="/":
   connexion_avec_client.send(str(int(valeur1) / int(valeur2)).encode ())




print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()