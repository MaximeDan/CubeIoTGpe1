#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: utilisateurs
#------------------------------------------------------------

CREATE TABLE utilisateurs(
        id           Int  Auto_increment  NOT NULL ,
        username     Varchar (50) NOT NULL ,
        nom          Varchar (50) NOT NULL ,
        prenom       Varchar (50) NOT NULL ,
        email        Char (50) NOT NULL ,
        mot_de_passe Varchar (50) NOT NULL ,
        avatar       Varchar (255) NOT NULL
	,CONSTRAINT utilisateurs_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: donnees
#------------------------------------------------------------

CREATE TABLE donnees(
        id          Int  Auto_increment  NOT NULL ,
        temperature Float NOT NULL ,
        humidite    Float NOT NULL ,
        date        Datetime NOT NULL
	,CONSTRAINT donnees_PK PRIMARY KEY (id)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: api
#------------------------------------------------------------

CREATE TABLE api(
        capteur                 Varchar (100) NOT NULL ,
        discription             Text NOT NULL ,
        version                 Varchar (10) NOT NULL ,
        statut                  Varchar (30) NOT NULL ,
        capteur_donnees_capteur Varchar (100) NOT NULL ,
        id                      Int NOT NULL
	,CONSTRAINT api_PK PRIMARY KEY (capteur)

	,CONSTRAINT api_donnees_FK FOREIGN KEY (id) REFERENCES donnees(id)
)ENGINE=InnoDB;

