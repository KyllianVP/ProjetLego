Tache réalisée : 

Commence une nouvelle commande avec elif numéro == 11

Import de JSON et de socket

Création d'un serveur TCP/HTTP avec des valeurs en JSON des capteurs

Donc initialisation des capteurs 
     initialisation des valeurs en JSON
Lecture dynamique des capteurs
Lors d'un lancement on peut donc avoir les valeurs :
{
bobarium
distance
angle_gyro
angle_moteur_D "angle_moteur Droit"
angle_moteur_G "angle_moteur Gauche"
}

Date : 15 Octobre 2025 // Kyllian

---------------------------------------------------------------------------------

Tache réalisée : 
Commence une nouvelle commande avec elif numéro == 11
Requete GET pour avancer, reculer, allez à droite, allez à gauche

premiere_ligne = requete.split("\r\n")[0]


        if premiere_ligne.startswith("GET /avancer"):
            robot.straight(200)
        elif premiere_ligne.startswith("GET /reculer"):
            robot.straight(-200)
        elif premiere_ligne.startswith("GET /gauche"):
            robot.turn(-90)
        elif premiere_ligne.startswith("GET /droite"):
            robot.turn(90)
        elif premiere_ligne.startswith("GET /stop"):
            moteur_G.stop()
            moteur_D.stop()


Date : 16 Octobre 2025 // Kyllian

---------------------------------------------------------------------------------
Tache réalisée : 
Commence une nouvelle commande avec elif numéro == 11
Les requetes permettent au robot d'ava,cer indéfiniment tant qu'on ne lui envoie pas d'autre requete
remplacement de robot.straight(200) => robot.drive(500, 0)


if premiere_ligne.startswith("GET /avancer"):
    robot.drive(500, 0)
elif premiere_ligne.startswith("GET /reculer"):
    robot.drive(-500, 0)
elif premiere_ligne.startswith("GET /gauche"):
    robot.drive(0, -120)
elif premiere_ligne.startswith("GET /droite"):
    robot.drive(0, 120)
elif premiere_ligne.startswith("GET /stop"):
    robot.stop()

Date : 10 Novembre 2025 // Kyllian
