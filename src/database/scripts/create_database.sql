/*--------------------------------------------------------------
  _      _ _                            _____        _        _                       _____                _   _             
 | |    (_) |                          |  __ \      | |      | |                     / ____|              | | (_)            
 | |     _| |__  _ __ __ _ _ __ _   _  | |  | | __ _| |_ __ _| |__   __ _ ___  ___  | |     _ __ ___  __ _| |_ _  ___  _ __  
 | |    | | '_ \| '__/ _` | '__| | | | | |  | |/ _` | __/ _` | '_ \ / _` / __|/ _ \ | |    | '__/ _ \/ _` | __| |/ _ \| '_ \ 
 | |____| | |_) | | | (_| | |  | |_| | | |__| | (_| | || (_| | |_) | (_| \__ \  __/ | |____| | |  __/ (_| | |_| | (_) | | | |
 |______|_|_.__/|_|  \__,_|_|   \__, | |_____/ \__,_|\__\__,_|_.__/ \__,_|___/\___|  \_____|_|  \___|\__,_|\__|_|\___/|_| |_|
                                 __/ |                                                                                       
                                |___/                                                                                        
--------------------------------------------------------------*/

#------------------------------------------------------------
# Reset Database
#------------------------------------------------------------

DROP TABLE IF EXISTS user_role;
DROP TABLE IF EXISTS genre_book;
DROP TABLE IF EXISTS writes;
DROP TABLE IF EXISTS modification;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS loan;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS language;
DROP TABLE IF EXISTS role;
DROP TABLE IF EXISTS collection;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS city;


#------------------------------------------------------------
# Table: author
#------------------------------------------------------------

CREATE TABLE author(
        id_author  Int  Auto_increment  NOT NULL ,
        first_name Varchar (100) NOT NULL ,
        last_name  Varchar (100) ,
        bio        Text NOT NULL
	,CONSTRAINT author_PK PRIMARY KEY (id_author)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: genre
#------------------------------------------------------------

CREATE TABLE genre(
        id_genre   Int  Auto_increment  NOT NULL ,
        name_genre Varchar (100) NOT NULL
	,CONSTRAINT genre_AK UNIQUE (name_genre)
	,CONSTRAINT genre_PK PRIMARY KEY (id_genre)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: collection
#------------------------------------------------------------

CREATE TABLE collection(
        id_collection   Int  Auto_increment  NOT NULL ,
        description     Text NOT NULL ,
        collection_name Varchar (50) NOT NULL
	,CONSTRAINT collection_AK UNIQUE (collection_name)
	,CONSTRAINT collection_PK PRIMARY KEY (id_collection)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: city
#------------------------------------------------------------

CREATE TABLE city(
        id_city Int  Auto_increment  NOT NULL ,
        name    Varchar (50) NOT NULL
	,CONSTRAINT city_AK UNIQUE (name)
	,CONSTRAINT city_PK PRIMARY KEY (id_city)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: address
#------------------------------------------------------------

CREATE TABLE address(
        id_address  Int  Auto_increment  NOT NULL ,
        number      Varchar (10) NOT NULL ,
        street      Varchar (50) NOT NULL ,
        postal_code Varchar (15) NOT NULL ,
        id_city     Int NOT NULL
	,CONSTRAINT address_PK PRIMARY KEY (id_address)

	,CONSTRAINT address_city_FK FOREIGN KEY (id_city) REFERENCES city(id_city)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: user
#------------------------------------------------------------

CREATE TABLE user(
        id_user              Int  Auto_increment  NOT NULL ,
        first_name           Varchar (100) NOT NULL ,
        date_of_birth        Datetime NOT NULL ,
        phone                Varchar (15) NOT NULL ,
        hashed_password      Varchar (255) NOT NULL ,
        last_connection_date Datetime NOT NULL ,
        is_active            Bool NOT NULL ,
        login                Varchar (100) NOT NULL ,
        last_name            Varchar (100) NOT NULL ,
        mail                 Varchar (254) NOT NULL ,
        id_address           Int
	,CONSTRAINT user_AK UNIQUE (login)
	,INDEX user_Idx (last_name, mail)
	,CONSTRAINT user_PK PRIMARY KEY (id_user)

	,CONSTRAINT user_address_FK FOREIGN KEY (id_address) REFERENCES address(id_address)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: role
#------------------------------------------------------------

CREATE TABLE role(
        id_role     Int  Auto_increment  NOT NULL ,
        description Text NOT NULL ,
        role_name   Varchar (50) NOT NULL
	,CONSTRAINT role_AK UNIQUE (role_name)
	,CONSTRAINT role_PK PRIMARY KEY (id_role)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: language
#------------------------------------------------------------

CREATE TABLE language(
        id_language   Int  Auto_increment  NOT NULL ,
        language_name Varchar (50) NOT NULL
	,CONSTRAINT language_PK PRIMARY KEY (id_language)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: book
#------------------------------------------------------------

CREATE TABLE book(
        id_book          Int  Auto_increment  NOT NULL ,
        title            Varchar (255) NOT NULL ,
        publication_date Datetime ,
        status           Enum ("available","borrowed","reserved") NOT NULL ,
        aspect           Enum ("new","good","damaged") NOT NULL ,
        isbn             Varchar (17) NOT NULL ,
        page_number      Int NOT NULL ,
        editor           Varchar (255) NOT NULL ,
        resume           Text NOT NULL ,
        created_at       Datetime NOT NULL ,
        deleted_at       Datetime ,
        id_collection    Int NOT NULL ,
        id_language      Int NOT NULL
	,CONSTRAINT book_PK PRIMARY KEY (id_book)

	,CONSTRAINT book_collection_FK FOREIGN KEY (id_collection) REFERENCES collection(id_collection)
	,CONSTRAINT book_language0_FK FOREIGN KEY (id_language) REFERENCES language(id_language)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: loan
#------------------------------------------------------------

CREATE TABLE loan(
        id_loan     Int  Auto_increment  NOT NULL ,
        date_loan   Datetime NOT NULL ,
        return_date Datetime NOT NULL ,
        id_user     Int NOT NULL ,
        id_book     Int NOT NULL
	,CONSTRAINT loan_PK PRIMARY KEY (id_loan)

	,CONSTRAINT loan_user_FK FOREIGN KEY (id_user) REFERENCES user(id_user)
	,CONSTRAINT loan_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: reservation
#------------------------------------------------------------

CREATE TABLE reservation(
        id_reservation   Int  Auto_increment  NOT NULL ,
        reservation_date Datetime NOT NULL ,
        is_confirmed     Bool NOT NULL ,
        id_user          Int NOT NULL ,
        id_book          Int NOT NULL
	,CONSTRAINT reservation_PK PRIMARY KEY (id_reservation)

	,CONSTRAINT reservation_user_FK FOREIGN KEY (id_user) REFERENCES user(id_user)
	,CONSTRAINT reservation_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
	,CONSTRAINT reservation_user_AK UNIQUE (id_user)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: modification
#------------------------------------------------------------

CREATE TABLE modification(
        id_modif          Int  Auto_increment  NOT NULL ,
        date_modification Datetime NOT NULL ,
        id_book           Int NOT NULL ,
        id_user           Int NOT NULL
	,CONSTRAINT modification_PK PRIMARY KEY (id_modif)

	,CONSTRAINT modification_book_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
	,CONSTRAINT modification_user0_FK FOREIGN KEY (id_user) REFERENCES user(id_user)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: writes
#------------------------------------------------------------

CREATE TABLE writes(
        id_author Int NOT NULL ,
        id_book   Int NOT NULL
	,CONSTRAINT writes_PK PRIMARY KEY (id_author,id_book)

	,CONSTRAINT writes_author_FK FOREIGN KEY (id_author) REFERENCES author(id_author)
	,CONSTRAINT writes_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: genre_book
#------------------------------------------------------------

CREATE TABLE genre_book(
        id_genre Int NOT NULL ,
        id_book  Int NOT NULL
	,CONSTRAINT genre_book_PK PRIMARY KEY (id_genre,id_book)

	,CONSTRAINT genre_book_genre_FK FOREIGN KEY (id_genre) REFERENCES genre(id_genre)
	,CONSTRAINT genre_book_book0_FK FOREIGN KEY (id_book) REFERENCES book(id_book)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: user_role
#------------------------------------------------------------

CREATE TABLE user_role(
        id_user Int NOT NULL ,
        id_role Int NOT NULL
	,CONSTRAINT user_role_PK PRIMARY KEY (id_user,id_role)

	,CONSTRAINT user_role_user_FK FOREIGN KEY (id_user) REFERENCES user(id_user)
	,CONSTRAINT user_role_role0_FK FOREIGN KEY (id_role) REFERENCES role(id_role)
)ENGINE=InnoDB;

