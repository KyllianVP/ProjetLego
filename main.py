#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                    InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import socket
import json
import time




# Création del'obet robot ,  sous le nom ev3
ev3 = EV3Brick()

# Programme à exécuter

# numéro de l'exemple à exécuter
# à choisir parmi 1, 2, 3, 4, 5, 6.1, 6.2, 7, 8, 9.1, 9.2, 9.3 ou 10
numero = 11

if numero <= 0:
    pass

elif numero == 1:
    # Exemple 1
    # Création de l'écran
    ecran = ev3.screen
    # Afficher un texte au point (10,10) de l'écran
    ecran.draw_text(10, 10, "Hello World !")
    wait(1000)

elif numero == 2:
    # Exemple 2
    # le robot parle...
    ev3.speaker.say("Hello world !")
    # ... et que la Force soit avec vous !
    morceau = [(392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100), (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100), (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100), (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100), (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100), (392, 250, 100), (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400), (311.13, 25, 200), (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100), (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700,100)]
    for note in morceau:
        ev3.speaker.beep(note[0], note[1])
        wait(note[2])

elif numero == 3:
    # Exemple 3
    # On allume les leds en jaune
    ev3.light.on(Color.YELLOW)
    # Pause d'1 seconde
    wait(1000)
    # On allume les leds en rouge
    ev3.light.on(Color.RED)
    # Pause d'1 seconde
    wait(1000)
    # On éteint toutes les leds
    ev3.light.off()
    # Pause d'1 seconde
    wait(1000)

elif numero == 4:
    # Exemple 4
    # test d’appui
    for i in range(0, 100):
        if Button.LEFT in ev3.buttons.pressed():   # Appui sur le bouton [GAUCHE]
            print("Left is pressed")
        if Button.DOWN in ev3.buttons.pressed():   # Appui sur le bouton [BAS]
            print("Down is pressed")
        wait(100)

elif numero == 5:
    # Exemple 5
    # initialisation du capteur
    contact_sensor = TouchSensor(Port.S1)
    # test du capteur
    # Tant qu'il n'est pas enfoncé, on allume les leds en rouge
    while contact_sensor.pressed() is False:
        ev3.light.on(Color.RED)
        # Si il est enfoncé, on allume les leds en jaune
    if contact_sensor.pressed() == True:
        ev3.light.on(Color.YELLOW)
        wait(2000)
        # On éteint toutes les leds
        ev3.light.off()
        wait(1000)    

elif numero == 6.1:
    # Exemple 6.1
    # Création du capteur lumineux
    color_sensor = ColorSensor(Port.S3)
    # Tant que la couleur n'est pas blanche...
    while color_sensor.color() != Color.WHITE:
        if color_sensor.color() == Color.RED:
            ev3.light.on(Color.RED)
        if color_sensor.color() == Color.GREEN:
            ev3.light.on(Color.GREEN)
        if color_sensor.color() == Color.YELLOW:
            ev3.light.on(Color.YELLOW)
    # On éteint tout
    ev3.light.off()

elif numero == 6.2:
    # Exemple 6.2
    # Création du capteur lumineux
    color_sensor = ColorSensor(Port.S3)
    # Pendant 10 secondes on change la led selon la lumière
    for i in range(0, 10):
        if color_sensor.reflection() < 50:
            ev3.light.on(Color.RED)
        else:
            ev3.light.on(Color.YELLOW)
        wait(1000)
    # On éteint tout
    ev3.light.off()

elif numero == 7:
    # Exemple 7
    # Création du capteur ultrason et de l'écran
    us = UltrasonicSensor(Port.S2)
    ecran = ev3.screen
    # Pendant 10 secondes on lit et affiche la distance en cm
    for i in range(0, 10):
        distance = int(us.distance()) / 10
        affichage =  "%f cm" % distance
        ecran.print("Distance = ")
        ecran.print(affichage)
        wait(1000)
        ecran.clear()

elif numero == 8:
    # Exemple 8
    # Création du capteur gyroscopique et de l'écran
    gs = GyroSensor(Port.S4, Direction.CLOCKWISE)
    ecran = ev3.screen
    # Pendant 10 secondes on lit et affiche l’angle
    for i in range(0, 10):
        angle = gs.angle()
        ecran.draw_text(10, 10, "Angle = %d degres" % angle)
        wait(1000)
        ecran.clear()

elif numero == 9.1:
    # Exemple 9.1
    # Création des moteurs
    left_m = Motor(Port.A, Direction.CLOCKWISE)
    right_m = Motor(Port.C, Direction.CLOCKWISE)
    medium_m = Motor(Port.B, Direction.CLOCKWISE)
    # Les moteurs tournent pendant 2s à une vitesse de 500 deg/s dans le même sens (horaire)
    # le robot avance
    left_m.run(500)
    right_m.run(500) 
    wait(2000)
    left_m.stop()
    right_m.stop()
    # Les moteurs tournent pendant 2,8s à une vitesse de 500 deg/s dans des sens différents
    # le robot tourne sur lui-même
    left_m.run(-500)
    right_m.run(500) 
    wait(2800)
    left_m.stop()
    right_m.stop()
    # Les moteurs tournent pendant 2s à une vitesse de 500 deg/s dans le même sens (anti-horaire)
    # le robot recule
    left_m.run(-500)
    right_m.run(-500) 
    wait(2000)
    left_m.stop()
    right_m.stop()
    # Le troisème moteur abaisse et remonte la barre
    medium_m.run(-1000)
    wait(1000)
    medium_m.stop()
    medium_m.run(+1000)
    wait(1000)
    medium_m.stop()


elif numero == 9.2:
    # Exemple 9.2
    # Création des moteurs gauche et droit reliés aux ports A et C
    left_m = Motor(Port.A, Direction.CLOCKWISE)
    right_m = Motor(Port.C, Direction.CLOCKWISE)
    # Les moteurs tournent pendant 1s chacun leur tour
    left_m.run_time(500, 1000)
    right_m.run_time(500, 1000)
    wait(1000)
    # Les moteurs tournent pendant 1s simultanément
    left_m.run_time(500, 1000, wait = False)
    right_m.run_time(500, 1000, wait = False)
    wait(1000)

elif numero == 9.3:
    # Exemple 9.3
    # Initialisation des moteurs.
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.C)
    # Initialisation du mode de pilotage.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
    # Le robot avance et recule d'un mètre.
    robot.straight(1000)
    ev3.speaker.beep()
    robot.straight(-1000)
    ev3.speaker.beep()
    # Le robot fait un tour sur lui-même puis recommence dans l'autre sens.
    robot.turn(360)
    ev3.speaker.beep()
    robot.turn(-360)
    ev3.speaker.beep()

elif numero == 10:
    # Exemple 10
    continuer = True
    while continuer:
        # on écrit ici le code à exécuter
        # on fait clignoter les leds en jaune et en rouge
        for loop in range(1000):
            ev3.light.on(Color.YELLOW)  
            if len(ev3.buttons.pressed()) != 0:
                continuer = False
        for loop in range(1000):
            ev3.light.on(Color.RED)
            if len(ev3.buttons.pressed()) != 0:
                continuer = False
    # on écrit ici l'action à exécuter en cas d'arrêt
    ev3.light.off()
    wait(1000)

elif numero == 11:
    
    # Initialisation Capteurs et moteurs
    us = UltrasonicSensor(Port.S2) # capteur ultrason
    bobarium_sensor = ColorSensor(Port.S3) # capteur de couleur pour le bobarium
    gyroscope = GyroSensor(Port.S4) # capteur gyroscopique
    moteur_G = Motor(Port.A) # moteur gauche
    moteur_D = Motor(Port.C) # moteur droit
    bras = Motor(Port.B)  # moteur du bras


    # Partie CSV (journal capteurs)
    mission_name = "Mission1" # Nom de préfixe du fichier
    date_str = time.strftime("%Y%m%d_%H%M%S") # Date et heure pour nom unique
    file_name = mission_name + "_" + date_str # Nom complet du fichier

    # Journal CSV avec DataLog 6 colonnes
    # temps, bobarium, distance, gyro, moteur_G, moteur_D
    # timestamp=False pour une gestion du temps personnalisée
    log = DataLog('temps', 'bobarium', 'distance', 'gyro', 'moteur_G', 'moteur_D',
                  name=file_name, timestamp=False)
    chrono = StopWatch() # Chronomètre pour le temps de la mission
    log_active = True # Flag enregistrement actif/inactif

    # Base de pilotage
    robot = DriveBase(moteur_G, moteur_D, wheel_diameter=55.5, axle_track=104)

    # Fonction de lecture des capteurs en 1 fois
    def read_sensors():
        return {
            "temps": chrono.time() / 1000,            # temps en secondes (/1000)
            "bobarium": bobarium_sensor.reflection(), # valeur du capteur de couleur pour le bobarium
            "distance": us.distance(),                # distance par l'ultrason en mm
            "angle_gyro": gyroscope.angle(),          # angle du gyroscope en degrés
            "angle_moteur_G": moteur_G.angle(),       # angle moteur gauche en degrés
            "angle_moteur_D": moteur_D.angle()        # angle moteur droit en degrés
        }

    # Affiche l'IP du robot en dur donc a modifier selon la configuration
    try:
        ip = "192.168.1.101"
        print("✅ IP EV3 :", ip)
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "IP: " + ip)
    except Exception as _:
        # Si échec, on ne fait rien
        pass
#------------------------ Serveur HTTP ---------------------------#
    # Serveur HTTP très simple
    socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permet de relancer rapidement le serveur après une coupure
    socket_serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Le serveur écoute sur toutes les interfaces réseau du port 1664
    socket_serveur.bind(("0.0.0.0", 1664))
    socket_serveur.listen(10)
    print("✅ Serveur en écoute sur le port 1664...")

#--- Boucle principale du serveur HTTP attente et gestion des clients ---#



    while True:
        # ici on attend une connexion d'un client
        socket_client, adresse = socket_serveur.accept()
        try:
            # Lecture de la requête HTTP envoyée par le client (512 octets max)
            requete = socket_client.recv(512).decode()
            if not requete:
                socket_client.close()
                continue

            # On récupère la première ligne de la requête HTTP 
            # Exemple : GET /avancer HTTP/1.1
            premiere_ligne = requete.split("\r\n")[0]
            
# Décodage des commandes HTTP pour piloter le robot
            # Avancer en continu
            if premiere_ligne.startswith("GET /avancer"):
                robot.drive(500, 0)
            # Reculer en continu
            elif premiere_ligne.startswith("GET /reculer"):
                robot.drive(-500, 0)
            # Aller à gauche en continu
            elif premiere_ligne.startswith("GET /gauche"):
                robot.drive(0, -120)
            # Aller à droite en continu
            elif premiere_ligne.startswith("GET /droite"):
                robot.drive(0, 120) 
            # Stopper le robot
            elif premiere_ligne.startswith("GET /stop"):
                robot.stop()
            # Lever le bras
            elif premiere_ligne.startswith("GET /lever"):
                bras.run_angle(800, 90)
            # Baisser le bras
            elif premiere_ligne.startswith("GET /baisser"):
                bras.run_angle(800, -90)
            # Allumer les leds en rouge
            elif premiere_ligne.startswith("GET /led_on"):
                ev3.light.on(Color.RED)
            # Éteindre les leds
            elif premiere_ligne.startswith("GET /led_off"):
                ev3.light.off()
            # Démarrer l'enregistrement CSV
            elif premiere_ligne.startswith("GET /csv_start"):
                log_active = True
                chrono.reset()
            # Arrêter l'enregistrement CSV
            elif premiere_ligne.startswith("GET /csv_stop"):
                log_active = False
                
            # Télécharger le fichier CSV
            elif premiere_ligne.startswith("GET /download_csv"):
                try:
                    # Ouverture et lecture du fichier CSV par DataLog
                    with open("/home/robot/Projet_LEGO/" + file_name + ".csv", "r") as f:
                        contenu = f.read()

                    # Réponse HTTP avec le fichier CSV avec les bons en-têtes
                    reponse = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/csv\r\n"
                        "Content-Disposition: attachment; filename=\"" + file_name + ".csv\"\r\n"
                        "Connection: close\r\n\r\n"
                        + contenu
                    )
                except Exception as e:
                    # En cas d'erreur (fichier non trouvé, etc.)
                    reponse = (
                        "HTTP/1.1 404 Not found\r\n"
                        "Connection: close\r\n\r\n" + str(e)
                    )
                socket_client.send(reponse.encode())
                socket_client.close()
                # On passe au client suivant
                continue
                        
                    

             

            # Lecture capteurs sans bouger
            elif premiere_ligne.startswith("GET /sensors") or premiere_ligne.startswith("GET /"):
                # On ne change rien, on lit juste les capteurs
                pass
            else:
                # si la route n'est pas reconnue
                rep = "HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n"
                socket_client.send(rep.encode())
                socket_client.close()
                continue


#--- Lecture des capteurs ---#

            valeurs = read_sensors()
            json_valeurs = json.dumps(valeurs)

#--- Journal CSV ---#
    # Journal CSV avec DataLog
            if log_active:
                log.log(
                    valeurs["temps"],           # temps en secondes (ou chrono.time() si tu veux en ms)
                    valeurs["bobarium"],
                    valeurs["distance"],
                    valeurs["angle_gyro"],
                    valeurs["angle_moteur_G"],
                    valeurs["angle_moteur_D"]
                )


# Réponse HTTP avec JSON

            reponse = "HTTP/1.1 200 OK\r\n"
            reponse += "Content-Type: application/json\r\n"
            reponse += "Connection: close\r\n"
            reponse += "Content-Length: " + str(len(json_valeurs)) + "\r\n"
            reponse += "\r\n"
            reponse += json_valeurs

            socket_client.send(reponse.encode())

        except Exception as e:
            try:
                # En cas d'erreur, on envoie une réponse 500 au client
                err = ("HTTP/1.1 500 Internal Server Error\r\n"
                       "Connection: close\r\n\r\n" + str(e))
                socket_client.send(err.encode())
            except:
                # Si l'envoi de l'erreur échoue, on n'abandonne
                pass
        finally:
                 # On ferme la connexion avec le client
            socket_client.close()
elif numero == 11:

    # --- Capteurs et moteurs ---
    us = UltrasonicSensor(Port.S2)
    bobarium_sensor = ColorSensor(Port.S3)
    gyroscope = GyroSensor(Port.S4)
    moteur_G = Motor(Port.A)
    moteur_D = Motor(Port.C)
    bras = Motor(Port.B)

    # Base de pilotage (DriveBase pour mouvements continus)
    robot = DriveBase(moteur_G, moteur_D, wheel_diameter=55.5, axle_track=104)

    # Affichage IP (en dur)
    try:
        ip = "192.168.1.101"
        print("IP EV3 :", ip)
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "IP: " + ip)
    except Exception:
        pass

    # Serveur HTTP
    socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_serveur.bind(("0.0.0.0", 1664))
    socket_serveur.listen(10)
    print("Serveur en écoute sur le port 1664...")

    while True:
        socket_client, adresse = socket_serveur.accept()
        try:
            requete = socket_client.recv(512).decode()
            if not requete:
                socket_client.close()
                continue

            premiere_ligne = requete.split("\r\n")[0]

            # --- Commandes du robot (pilotage continu) ---

            # Avancer tant qu'on n'envoie pas une autre commande
            if premiere_ligne.startswith("GET /avancer"):
                robot.drive(500, 0)

            # Reculer en continu
            elif premiere_ligne.startswith("GET /reculer"):
                robot.drive(-500, 0)

            # Tourner à gauche sur place
            elif premiere_ligne.startswith("GET /gauche"):
                robot.drive(0, -120)

            # Tourner à droite sur place
            elif premiere_ligne.startswith("GET /droite"):
                robot.drive(0, 120)

            # Stop complet
            elif premiere_ligne.startswith("GET /stop"):
                robot.stop()

            # Lever le bras
            elif premiere_ligne.startswith("GET /lever"):
                bras.run_angle(800, 90)
            # Baisser le bras
            elif premiere_ligne.startswith("GET /baisser"):
                bras.run_angle(800, -90)
            # Allumer les leds en rouge
            elif premiere_ligne.startswith("GET /led_on"):
                ev3.light.on(Color.RED)
            # Éteindre les leds
            elif premiere_ligne.startswith("GET /led_off"):
                ev3.light.off()

            # --- Lecture capteurs ---
            valeurs = {
                "bobarium": bobarium_sensor.reflection(),
                "distance": us.distance(),
                "angle_gyro": gyroscope.angle(),
                "angle_moteur_G": moteur_G.angle(),
                "angle_moteur_D": moteur_D.angle()
            }

            json_valeurs = json.dumps(valeurs)

            # --- Réponse HTTP JSON ---
            reponse = "HTTP/1.1 200 OK\r\n"
            reponse += "Content-Type: application/json\r\n"
            reponse += "Connection: close\r\n"
            reponse += "Content-Length: " + str(len(json_valeurs)) + "\r\n"
            reponse += "\r\n"
            reponse += json_valeurs

            socket_client.send(reponse.encode())

        except Exception as e:
            try:
                err = (
                    "HTTP/1.1 500 Internal Server Error\r\n"
                    "Connection: close\r\n\r\n" + str(e)
                )
                socket_client.send(err.encode())
            except:
                pass
        finally:
            socket_client.close()
