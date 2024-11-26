#------------------------------------------------------------
#        Script MySQL corrigé.
#------------------------------------------------------------

#------------------------------------------------------------
# Table: author
#------------------------------------------------------------

CREATE TABLE author(
    id_author  INT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name  VARCHAR(100),
    bio        TEXT NOT NULL,
    CONSTRAINT author_PK PRIMARY KEY (id_author)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: genre
#------------------------------------------------------------

CREATE TABLE genre(
    id_genre   INT AUTO_INCREMENT NOT NULL,
    name_genre VARCHAR(100) NOT NULL,
    CONSTRAINT genre_PK PRIMARY KEY (id_genre)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: collection
#------------------------------------------------------------

CREATE TABLE `collection`(
    id_collection   INT AUTO_INCREMENT NOT NULL,
    collection_name VARCHAR(50) NOT NULL,
    description     TEXT NOT NULL,
    CONSTRAINT collection_PK PRIMARY KEY (id_collection)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: city
#------------------------------------------------------------

CREATE TABLE city(
    id_city INT AUTO_INCREMENT NOT NULL,
    name    VARCHAR(50) NOT NULL,
    CONSTRAINT city_PK PRIMARY KEY (id_city)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: adresse
#------------------------------------------------------------

CREATE TABLE adresse(
    id_adresse  INT AUTO_INCREMENT NOT NULL,
    number      VARCHAR(10) NOT NULL,
    street      VARCHAR(50) NOT NULL,
    postal_code VARCHAR(15) NOT NULL,
    id_city     INT NOT NULL,
    CONSTRAINT adresse_PK PRIMARY KEY (id_adresse),
    CONSTRAINT adresse_city_FK FOREIGN KEY (id_city) REFERENCES city(id_city)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: user
#------------------------------------------------------------

CREATE TABLE `user`(
    id_user              INT AUTO_INCREMENT NOT NULL,
    first_name           VARCHAR(100) NOT NULL,
    last_name            VARCHAR(100) NOT NULL,
    date_of_birth        DATE NOT NULL,
    mail                 VARCHAR(254) NOT NULL,
    phone                VARCHAR(15) NOT NULL,
    login                VARCHAR(100) NOT NULL,
    hashed_password      VARCHAR(255) NOT NULL,
    last_connection_date DATE NOT NULL,
    member_status        ENUM('actif','inactif') NOT NULL,
    id_adresse           INT,
    CONSTRAINT user_PK PRIMARY KEY (id_user),
    CONSTRAINT user_adresse_FK FOREIGN KEY (id_adresse) REFERENCES adresse(id_adresse)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: book
#------------------------------------------------------------

CREATE TABLE book(
    id_book          INT AUTO_INCREMENT NOT NULL,
    title            VARCHAR(255) NOT NULL,
    publication_date DATE,
    status           ENUM('disponible','emprunte','reserve') NOT NULL,
    `condition`      ENUM('neuf','bon','abime') NOT NULL,
    isbn             VARCHAR(17) NOT NULL,
    page_number      INT NOT NULL,
    editor           VARCHAR(255) NOT NULL,
    langue           VARCHAR(20) NOT NULL,
    resume           TEXT NOT NULL,
    created_at       DATETIME NOT NULL,
    deleted_at       DATETIME DEFAULT NULL,
    updated_at       DATETIME NOT NULL,
    id_collection    INT NOT NULL,
    id_user          INT NOT NULL,
    id_user_delete   INT DEFAULT NULL,
    CONSTRAINT book_PK PRIMARY KEY (id_book),
    CONSTRAINT book_collection_FK FOREIGN KEY (id_collection) REFERENCES `collection`(id_collection),
    CONSTRAINT book_user0_FK FOREIGN KEY (id_user) REFERENCES `user`(id_user),
    CONSTRAINT book_user1_FK FOREIGN KEY (id_user_delete) REFERENCES `user`(id_user)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: notification
#------------------------------------------------------------

CREATE TABLE notification(
    id_notification   INT AUTO_INCREMENT NOT NULL,
    message           TEXT NOT NULL,
    notification_date DATE NOT NULL,
    notification_type ENUM('rappel','retard','confirmation') NOT NULL,
    seen              BOOL NOT NULL,
    id_user           INT NOT NULL,
    CONSTRAINT notification_PK PRIMARY KEY (id_notification),
    CONSTRAINT notification_user_FK FOREIGN KEY (id_user) REFERENCES `user`(id_user)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: loan
#------------------------------------------------------------

CREATE TABLE loan(
    id_loan     INT AUTO_INCREMENT NOT NULL,
    date_loan   DATE NOT NULL,
    return_date DATE NOT NULL,
    id_user     INT NOT NULL,
    id_book     INT NOT NULL,
    CONSTRAINT loan_PK PRIMARY KEY (id_loan),
    CONSTRAINT loan_user_FK FOREIGN KEY (id_user) REFERENCES `user`(id_user),
    CONSTRAINT loan_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: reservation
#------------------------------------------------------------

CREATE TABLE reservation(
    id_reservation     INT AUTO_INCREMENT NOT NULL,
    reservation_date   DATE NOT NULL,
    reservation_status ENUM('attente','confirmee') NOT NULL,
    id_user            INT NOT NULL,
    id_book            INT NOT NULL,
    CONSTRAINT reservation_PK PRIMARY KEY (id_reservation),
    CONSTRAINT reservation_user_FK FOREIGN KEY (id_user) REFERENCES `user`(id_user),
    CONSTRAINT reservation_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: role
#------------------------------------------------------------

CREATE TABLE `role`(
    id_role     INT AUTO_INCREMENT NOT NULL,
    role_name   ENUM('administrateur','membre','super_administrateur') NOT NULL,
    description TEXT NOT NULL,
    CONSTRAINT role_PK PRIMARY KEY (id_role)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: writes
#------------------------------------------------------------

CREATE TABLE writes(
    id_author INT NOT NULL,
    id_book   INT NOT NULL,
    CONSTRAINT writes_PK PRIMARY KEY (id_author, id_book),
    CONSTRAINT writes_author_FK FOREIGN KEY (id_author) REFERENCES author(id_author),
    CONSTRAINT writes_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: belongs
#------------------------------------------------------------

CREATE TABLE belongs(
    id_genre INT NOT NULL,
    id_book  INT NOT NULL,
    CONSTRAINT belongs_PK PRIMARY KEY (id_genre, id_book),
    CONSTRAINT belongs_genre_FK FOREIGN KEY (id_genre) REFERENCES genre(id_genre),
    CONSTRAINT belongs_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: is
#------------------------------------------------------------

CREATE TABLE `is`(
    id_role INT NOT NULL,
    id_user INT NOT NULL,
    CONSTRAINT is_PK PRIMARY KEY (id_role, id_user),
    CONSTRAINT is_role_FK FOREIGN KEY (id_role) REFERENCES `role`(id_role),
    CONSTRAINT is_user0_FK FOREIGN KEY (id_user) REFERENCES `user`(id_user)
) ENGINE=InnoDB;

#------------------------------------------------------------
# Table: modify
#------------------------------------------------------------

CREATE TABLE `modify`(
    id_user           INT NOT NULL,
    id_book           INT NOT NULL,
    modification_date DATETIME NOT NULL,
    CONSTRAINT modify_PK PRIMARY KEY (id_user, id_book),
    CONSTRAINT modify_user_FK FOREIGN KEY (id_user) REFERENCES `user`(id_user),
    CONSTRAINT modify_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;
