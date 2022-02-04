# CubeIoTGpe1
Projet réalisé dans le cadre d'étude. réalisation d'une satation météo à l'aide d'un Raspberry PI.
Adresse GitHub : https://github.com/MDANDEL/CubeIoTGpe1.git


Sujets préférentiel
- Ismail : back-end /database/
- Stan : Front/Back end / database
- Clément :  Back/Front
- Maxime : Back/Front
github Repo

la répartion des tâches :
    - Base de  données
modèle conceptuel
Table sonde n°1
script d'ajout d'une table à la connexion d'une nouvelle sonde
 Script SQL  API - requêtes - DB
    - Modélisation des données
    - API Python -Flask-RESTFUL
 Connectez l'api à la base de données
 API  pour  GET POST DELETE UPDATE 
*  Créer la requête pour envoyer les données vers le front, JSON to parse( HTML)
   -  EOS et circuit 
 * prototype et articles pour monter le IOS .
* Branchement et voltage 
* Micropython 
* sera administrable via SSH
    - Front-end (HTML , CSS, Flask)
    - Documentation
* Liens des librairies utilisées
* indiquer les étapes d'installation
* doc des outils 


APPLICATION:

- Interface web consultable (navigateur) = responsive
- Graphique des données température / humidité
- Pictogramme (code couleur) = déduire à partir des données la météo actuelle
- Une charte graphique qui affiche les données en live.
- Bonus : 
- carte (plan jpeg) qui permet de situer les sonde 
- Bouton "partage" du graphique ou du dernier relevé (permet d'envoyer les données à vos amis (mail, réseau sociaux, autres)

API et BDD:
- API Sonde : Méthode pour C(reate) R(ead) U(pdate)
- Table des relevés : Méthode C(reate) R(ead)
- Tourne même machine locale
- BONUS: gérer l'authentification des utilisateurs

Serveur:
Hébergement : 
- Serveur web
- SGBDR (correctement configuré)
- Administrable via SSH
- API
- BDD ne sera accessible qu'à travers API
- Ecran permettant d'afficher :
- Adresse IP
- Date
- Heure
- Defiler les derniers relevés des sondes

Sonde de température
- Correctement câblée avec les capteurs de température /hulidité et alimentation
- Programmée avec le langage de notre choix compatible avec un ESP (C, micropython, LUA)
- Eviter les relevés imprécis le capteur fera des relevés toutes les quelque secondes et realiser une moyenne d'au moins 5 relevés afin d'envoyer des données "lissées" à l'API (Avoir un graphique cohérent)

Cahier des charges



