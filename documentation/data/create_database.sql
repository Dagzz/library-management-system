#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: createur
#------------------------------------------------------------

CREATE TABLE createur(
        id_createur Int  Auto_increment  NOT NULL ,
        nom         Varchar (100) NOT NULL ,
        prenom      Varchar (100) ,
        bio         Text NOT NULL
	,CONSTRAINT createur_PK PRIMARY KEY (id_createur)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: genre
#------------------------------------------------------------

CREATE TABLE genre(
        id_genre  Int  Auto_increment  NOT NULL ,
        nom_genre Varchar (100) NOT NULL
	,CONSTRAINT genre_PK PRIMARY KEY (id_genre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: collection
#------------------------------------------------------------

CREATE TABLE collection(
        id_collection          Int  Auto_increment  NOT NULL ,
        nom_collection         Varchar (50) NOT NULL ,
        description_collection Text NOT NULL
	,CONSTRAINT collection_PK PRIMARY KEY (id_collection)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: livre
#------------------------------------------------------------

CREATE TABLE livre(
        id_livre         Int  Auto_increment  NOT NULL ,
        titre            Varchar (255) NOT NULL ,
        date_publication Date ,
        statut           Enum ("disponible","emprunte","reserve") NOT NULL ,
        etat             Enum ("neuf","bon","abime") NOT NULL ,
        isbn             Varchar (17) NOT NULL ,
        nombre_page      Int NOT NULL ,
        editeur          Varchar (255) NOT NULL ,
        langue           Varchar (10) NOT NULL ,
        resume           Text NOT NULL ,
        id_collection    Int NOT NULL
	,CONSTRAINT livre_PK PRIMARY KEY (id_livre)

	,CONSTRAINT livre_collection_FK FOREIGN KEY (id_collection) REFERENCES collection(id_collection)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: ville
#------------------------------------------------------------

CREATE TABLE ville(
        id_ville  Int  Auto_increment  NOT NULL ,
        nom_ville Varchar (50) NOT NULL
	,CONSTRAINT ville_PK PRIMARY KEY (id_ville)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: addresse
#------------------------------------------------------------

CREATE TABLE addresse(
        id_addresse Int  Auto_increment  NOT NULL ,
        numero      Varchar (10) NOT NULL ,
        voie        Varchar (50) NOT NULL ,
        code_postal Varchar (15) NOT NULL ,
        id_ville    Int NOT NULL
	,CONSTRAINT addresse_PK PRIMARY KEY (id_addresse)

	,CONSTRAINT addresse_ville_FK FOREIGN KEY (id_ville) REFERENCES ville(id_ville)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: ecrit
#------------------------------------------------------------

CREATE TABLE ecrit(
        id_createur Int NOT NULL ,
        id_livre    Int NOT NULL
	,CONSTRAINT ecrit_PK PRIMARY KEY (id_createur,id_livre)

	,CONSTRAINT ecrit_createur_FK FOREIGN KEY (id_createur) REFERENCES createur(id_createur)
	,CONSTRAINT ecrit_livre0_FK FOREIGN KEY (id_livre) REFERENCES livre(id_livre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: appartient
#------------------------------------------------------------

CREATE TABLE appartient(
        id_genre Int NOT NULL ,
        id_livre Int NOT NULL
	,CONSTRAINT appartient_PK PRIMARY KEY (id_genre,id_livre)

	,CONSTRAINT appartient_genre_FK FOREIGN KEY (id_genre) REFERENCES genre(id_genre)
	,CONSTRAINT appartient_livre0_FK FOREIGN KEY (id_livre) REFERENCES livre(id_livre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: notification
#------------------------------------------------------------

CREATE TABLE notification(
        id_notification   Int  Auto_increment  NOT NULL ,
        message           Text NOT NULL ,
        date_notification Date NOT NULL ,
        type_notification Enum ("rappel","retard","confirmation") NOT NULL ,
        canal             Enum ("sms","mail","courrier") NOT NULL ,
        id_utilisateur    Int NOT NULL
	,CONSTRAINT notification_PK PRIMARY KEY (id_notification)

	,CONSTRAINT notification_utilisateur_FK FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: emprunt
#------------------------------------------------------------

CREATE TABLE emprunt(
        id_emprunt            Int  Auto_increment  NOT NULL ,
        date_emprunt          Date NOT NULL ,
        date_retour_effective Date NOT NULL ,
        id_utilisateur        Int NOT NULL ,
        id_livre              Int NOT NULL
	,CONSTRAINT emprunt_PK PRIMARY KEY (id_emprunt)

	,CONSTRAINT emprunt_member_FK FOREIGN KEY (id_utilisateur) REFERENCES member(id_utilisateur)
	,CONSTRAINT emprunt_livre0_FK FOREIGN KEY (id_livre) REFERENCES livre(id_livre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: reservation
#------------------------------------------------------------

CREATE TABLE reservation(
        id_reservation     Int  Auto_increment  NOT NULL ,
        date_reservation   Date NOT NULL ,
        statut_reservation Enum ("attente","confirmee") NOT NULL ,
        id_utilisateur     Int NOT NULL ,
        id_livre           Int NOT NULL
	,CONSTRAINT reservation_PK PRIMARY KEY (id_reservation)

	,CONSTRAINT reservation_member_FK FOREIGN KEY (id_utilisateur) REFERENCES member(id_utilisateur)
	,CONSTRAINT reservation_livre0_FK FOREIGN KEY (id_livre) REFERENCES livre(id_livre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: utilisateur
#------------------------------------------------------------

CREATE TABLE utilisateur(
        id_utilisateur Int  Auto_increment  NOT NULL ,
        nom            Varchar (100) NOT NULL ,
        prenom         Varchar (100) NOT NULL ,
        mail           Varchar (254) NOT NULL ,
        telephone      Varchar (15) NOT NULL ,
        id_addresse    Int ,
        id_auth        Int NOT NULL
	,CONSTRAINT utilisateur_PK PRIMARY KEY (id_utilisateur)

	,CONSTRAINT utilisateur_addresse_FK FOREIGN KEY (id_addresse) REFERENCES addresse(id_addresse)
	,CONSTRAINT utilisateur_authentification0_FK FOREIGN KEY (id_auth) REFERENCES authentification(id_auth)
	,CONSTRAINT utilisateur_authentification_AK UNIQUE (id_auth)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: authentification
#------------------------------------------------------------

CREATE TABLE authentification(
        id_auth                 Int  Auto_increment  NOT NULL ,
        login                   Varchar (100) NOT NULL ,
        mot_de_passe            Varchar (255) NOT NULL ,
        date_derniere_connexion Date NOT NULL ,
        id_utilisateur          Int NOT NULL
	,CONSTRAINT authentification_PK PRIMARY KEY (id_auth)

	,CONSTRAINT authentification_utilisateur_FK FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
	,CONSTRAINT authentification_utilisateur_AK UNIQUE (id_utilisateur)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: admin
#------------------------------------------------------------

CREATE TABLE admin(
        id_utilisateur Int NOT NULL ,
        nom            Varchar (100) NOT NULL ,
        prenom         Varchar (100) NOT NULL ,
        mail           Varchar (254) NOT NULL ,
        telephone      Varchar (15) NOT NULL ,
        id_addresse    Int ,
        id_auth        Int NOT NULL
	,CONSTRAINT admin_PK PRIMARY KEY (id_utilisateur)

	,CONSTRAINT admin_utilisateur_FK FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
	,CONSTRAINT admin_addresse0_FK FOREIGN KEY (id_addresse) REFERENCES addresse(id_addresse)
	,CONSTRAINT admin_authentification1_FK FOREIGN KEY (id_auth) REFERENCES authentification(id_auth)
	,CONSTRAINT admin_authentification_AK UNIQUE (id_auth)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: member
#------------------------------------------------------------

CREATE TABLE member(
        id_utilisateur Int NOT NULL ,
        statut_membre  Enum ("actif","inactif") NOT NULL ,
        nom            Varchar (100) NOT NULL ,
        prenom         Varchar (100) NOT NULL ,
        mail           Varchar (254) NOT NULL ,
        telephone      Varchar (15) NOT NULL ,
        id_addresse    Int ,
        id_auth        Int NOT NULL
	,CONSTRAINT member_PK PRIMARY KEY (id_utilisateur)

	,CONSTRAINT member_utilisateur_FK FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
	,CONSTRAINT member_addresse0_FK FOREIGN KEY (id_addresse) REFERENCES addresse(id_addresse)
	,CONSTRAINT member_authentification1_FK FOREIGN KEY (id_auth) REFERENCES authentification(id_auth)
	,CONSTRAINT member_authentification_AK UNIQUE (id_auth)
)ENGINE=InnoDB;

