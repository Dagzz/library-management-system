-- Create the database if it doesn't exist and use it
CREATE DATABASE IF NOT EXISTS bibliotheque_db;
USE bibliotheque_db;

-- Drop tables if they already exist to avoid conflicts
DROP TABLE IF EXISTS modify;
DROP TABLE IF EXISTS belongs;
DROP TABLE IF EXISTS writes;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS loan;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS language;
DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS addresse;
DROP TABLE IF EXISTS collection;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS city;

-- 1. Table: city
CREATE TABLE city (
    id_city    INT AUTO_INCREMENT NOT NULL,
    name       VARCHAR(50) NOT NULL,
    CONSTRAINT city_AK UNIQUE (name),
    CONSTRAINT city_PK PRIMARY KEY (id_city)
) ENGINE=InnoDB;

-- 2. Table: author
CREATE TABLE author (
    id_author     INT AUTO_INCREMENT NOT NULL,
    first_name    VARCHAR(100) NOT NULL,
    last_name     VARCHAR(100),
    bio           TEXT NOT NULL,
    CONSTRAINT author_PK PRIMARY KEY (id_author)
) ENGINE=InnoDB;

-- 3. Table: genre
CREATE TABLE genre (
    id_genre     INT AUTO_INCREMENT NOT NULL,
    name_genre   VARCHAR(100) NOT NULL,
    CONSTRAINT genre_AK UNIQUE (name_genre),
    CONSTRAINT genre_PK PRIMARY KEY (id_genre)
) ENGINE=InnoDB;

-- 4. Table: collection
CREATE TABLE collection (
    id_collection    INT AUTO_INCREMENT NOT NULL,
    description      TEXT NOT NULL,
    collection_name  VARCHAR(50) NOT NULL,
    CONSTRAINT collection_AK UNIQUE (collection_name),
    CONSTRAINT collection_PK PRIMARY KEY (id_collection)
) ENGINE=InnoDB;

-- 5. Table: addresse
CREATE TABLE addresse (
    id_addresse  INT AUTO_INCREMENT NOT NULL,
    number       VARCHAR(10) NOT NULL,
    street       VARCHAR(50) NOT NULL,
    postal_code  VARCHAR(15) NOT NULL,
    id_city      INT NOT NULL,
    CONSTRAINT addresse_PK PRIMARY KEY (id_addresse),
    CONSTRAINT addresse_city_FK FOREIGN KEY (id_city) REFERENCES city(id_city)
) ENGINE=InnoDB;

-- 6. Table: user
CREATE TABLE user (
    id_user              INT AUTO_INCREMENT NOT NULL,
    first_name           VARCHAR(100) NOT NULL,
    last_name            VARCHAR(100) NOT NULL,
    date_of_birth        DATE NOT NULL,
    mail                 VARCHAR(254) NOT NULL,
    phone                VARCHAR(15) NOT NULL,
    login                VARCHAR(100) NOT NULL,
    hashed_password      VARCHAR(255) NOT NULL,
    last_connection_date DATETIME NOT NULL,
    is_active            BOOLEAN NOT NULL,
    id_addresse          INT,
    CONSTRAINT user_PK PRIMARY KEY (id_user),
    CONSTRAINT user_addresse_FK FOREIGN KEY (id_addresse) REFERENCES addresse(id_addresse)
) ENGINE=InnoDB;

-- 7. Table: admin
CREATE TABLE admin (
    id_user         INT NOT NULL,
    id_admin        INT NOT NULL,
    first_name      VARCHAR(100) NOT NULL,
    last_name       VARCHAR(100) NOT NULL,
    date_of_birth   DATE NOT NULL,
    mail            VARCHAR(254) NOT NULL,
    phone           VARCHAR(15) NOT NULL,
    login           VARCHAR(100) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    last_connection_date DATETIME NOT NULL,
    is_active       BOOLEAN NOT NULL,
    id_addresse     INT,
    CONSTRAINT admin_PK PRIMARY KEY (id_user, id_admin),
    CONSTRAINT admin_user_FK FOREIGN KEY (id_user) REFERENCES user(id_user),
    CONSTRAINT admin_addresse0_FK FOREIGN KEY (id_addresse) REFERENCES addresse(id_addresse)
) ENGINE=InnoDB;

-- 8. Table: language
CREATE TABLE language (
    id_language INT AUTO_INCREMENT NOT NULL,
    name        VARCHAR(100) NOT NULL,
    CONSTRAINT language_AK UNIQUE (name),
    CONSTRAINT language_PK PRIMARY KEY (id_language)
) ENGINE=InnoDB;

-- 9. Table: book
CREATE TABLE book (
    id_book          INT AUTO_INCREMENT NOT NULL,
    title            VARCHAR(255) NOT NULL,
    publication_date DATE,
    status           ENUM('available', 'borrowed', 'reserved') NOT NULL,
    aspect           ENUM('new', 'good', 'damaged') NOT NULL,
    isbn             VARCHAR(17) NOT NULL,
    page_number      INT NOT NULL,
    editor           VARCHAR(255) NOT NULL,
    langue           VARCHAR(10) NOT NULL,
    resume           TEXT NOT NULL,
    create_at        DATETIME NOT NULL,
    delete_at        DATETIME NULL,
    update_at        DATETIME NOT NULL,
    id_collection    INT NOT NULL,
    id_user          INT NOT NULL,
    id_admin         INT NOT NULL,
    id_user_admin    INT NOT NULL,
    id_admin_delete  INT NOT NULL,
    id_language      INT NOT NULL,
    id_language_2    INT NULL, 
    CONSTRAINT book_PK PRIMARY KEY (id_book),
    
    CONSTRAINT book_collection_FK FOREIGN KEY (id_collection) REFERENCES collection(id_collection),
    CONSTRAINT book_admin0_FK FOREIGN KEY (id_user, id_admin) REFERENCES admin(id_user, id_admin),
    CONSTRAINT book_admin1_FK FOREIGN KEY (id_user_admin, id_admin_delete) REFERENCES admin(id_user, id_admin),
    
    CONSTRAINT book_language_FK FOREIGN KEY (id_language) REFERENCES language(id_language),
    CONSTRAINT book_language2_FK FOREIGN KEY (id_language_2) REFERENCES language(id_language)
) ENGINE=InnoDB;

-- 10. Table: loan
CREATE TABLE loan (
    id_loan      INT AUTO_INCREMENT NOT NULL,
    date_loan    DATE NOT NULL,
    return_date  DATE NOT NULL,
    id_user      INT NOT NULL,
    id_book      INT NOT NULL,
    CONSTRAINT loan_PK PRIMARY KEY (id_loan),
    CONSTRAINT loan_user_FK FOREIGN KEY (id_user) REFERENCES user(id_user),
    CONSTRAINT loan_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

-- 11. Table: reservation
CREATE TABLE reservation (
    id_reservation    INT AUTO_INCREMENT NOT NULL,
    reservation_date  DATE NOT NULL,
    is_confirmed      BOOLEAN NOT NULL,
    id_user           INT NOT NULL,
    id_book           INT NOT NULL,
    CONSTRAINT reservation_PK PRIMARY KEY (id_reservation),
    CONSTRAINT reservation_user_FK FOREIGN KEY (id_user) REFERENCES user(id_user),
    CONSTRAINT reservation_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book),
    CONSTRAINT reservation_user_AK UNIQUE (id_user)
) ENGINE=InnoDB;

-- 12. Table: writes
CREATE TABLE writes (
    id_author INT NOT NULL,
    id_book   INT NOT NULL,
    CONSTRAINT writes_PK PRIMARY KEY (id_author, id_book),
    CONSTRAINT writes_author_FK FOREIGN KEY (id_author) REFERENCES author(id_author),
    CONSTRAINT writes_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

-- 13. Table: belongs
CREATE TABLE belongs (
    id_genre INT NOT NULL,
    id_book  INT NOT NULL,
    CONSTRAINT belongs_PK PRIMARY KEY (id_genre, id_book),
    CONSTRAINT belongs_genre_FK FOREIGN KEY (id_genre) REFERENCES genre(id_genre),
    CONSTRAINT belongs_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

-- 14. Table: modify
CREATE TABLE modify (
    id_user           INT NOT NULL,
    id_admin          INT NOT NULL,
    id_book           INT NOT NULL,
    modification_date DATETIME NOT NULL,
    CONSTRAINT modify_PK PRIMARY KEY (id_user, id_admin, id_book),
    CONSTRAINT modify_admin_FK FOREIGN KEY (id_user, id_admin) REFERENCES admin(id_user, id_admin),
    CONSTRAINT modify_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
) ENGINE=InnoDB;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;
