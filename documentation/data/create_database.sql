#------------------------------------------------------------
#        MySQL Script.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: creator
#------------------------------------------------------------

CREATE TABLE creator(
        creator_id     INT AUTO_INCREMENT NOT NULL,
        last_name      VARCHAR(100) NOT NULL,
        first_name     VARCHAR(100),
        bio            TEXT NOT NULL,
    CONSTRAINT creator_PK PRIMARY KEY (creator_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: genre
#------------------------------------------------------------

CREATE TABLE genre(
        genre_id   INT AUTO_INCREMENT NOT NULL,
        genre_name VARCHAR(100) NOT NULL,
    CONSTRAINT genre_PK PRIMARY KEY (genre_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: collection
#------------------------------------------------------------

CREATE TABLE collection(
        collection_id          INT AUTO_INCREMENT NOT NULL,
        collection_name        VARCHAR(50) NOT NULL,
        collection_description TEXT NOT NULL,
    CONSTRAINT collection_PK PRIMARY KEY (collection_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: book
#------------------------------------------------------------

CREATE TABLE book(
        book_id          INT AUTO_INCREMENT NOT NULL,
        title            VARCHAR(255) NOT NULL,
        publication_date DATE,
        status           ENUM("available","borrowed","reserved") NOT NULL,
        condition        ENUM("new","good","damaged") NOT NULL,
        isbn             VARCHAR(17) NOT NULL,
        page_count       INT NOT NULL,
        publisher        VARCHAR(255) NOT NULL,
        language         VARCHAR(10) NOT NULL,
        summary          TEXT NOT NULL,
        collection_id    INT NOT NULL,
    CONSTRAINT book_PK PRIMARY KEY (book_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: city
#------------------------------------------------------------

CREATE TABLE city(
        city_id   INT AUTO_INCREMENT NOT NULL,
        city_name VARCHAR(50) NOT NULL,
    CONSTRAINT city_PK PRIMARY KEY (city_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: address
#------------------------------------------------------------

CREATE TABLE address(
        address_id   INT AUTO_INCREMENT NOT NULL,
        number       VARCHAR(10) NOT NULL,
        street       VARCHAR(50) NOT NULL,
        postal_code  VARCHAR(15) NOT NULL,
        city_id      INT NOT NULL,
    CONSTRAINT address_PK PRIMARY KEY (address_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: writes
#------------------------------------------------------------

CREATE TABLE writes(
        creator_id INT NOT NULL,
        book_id    INT NOT NULL,
    CONSTRAINT writes_PK PRIMARY KEY (creator_id, book_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: belongs_to
#------------------------------------------------------------

CREATE TABLE belongs_to(
        genre_id INT NOT NULL,
        book_id  INT NOT NULL,
    CONSTRAINT belongs_to_PK PRIMARY KEY (genre_id, book_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: notification
#------------------------------------------------------------

CREATE TABLE notification(
        notification_id   INT AUTO_INCREMENT NOT NULL,
        message           TEXT NOT NULL,
        notification_date DATE NOT NULL,
        notification_type  ENUM("reminder","late","confirmation") NOT NULL,
        channel            ENUM("sms","email","mail") NOT NULL,
        user_id            INT NOT NULL,
    CONSTRAINT notification_PK PRIMARY KEY (notification_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: loan
#------------------------------------------------------------

CREATE TABLE loan(
        loan_id             INT AUTO_INCREMENT NOT NULL,
        loan_date           DATE NOT NULL,
        actual_return_date  DATE NOT NULL,
        user_id             INT NOT NULL,
        book_id             INT NOT NULL,
    CONSTRAINT loan_PK PRIMARY KEY (loan_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: reservation
#------------------------------------------------------------

CREATE TABLE reservation(
        reservation_id     INT AUTO_INCREMENT NOT NULL,
        reservation_date   DATE NOT NULL,
        reservation_status ENUM("pending","confirmed") NOT NULL,
        user_id            INT NOT NULL,
        book_id            INT NOT NULL,
    CONSTRAINT reservation_PK PRIMARY KEY (reservation_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: user
#------------------------------------------------------------

CREATE TABLE user(
        user_id      INT AUTO_INCREMENT NOT NULL,
        last_name    VARCHAR(100) NOT NULL,
        first_name   VARCHAR(100) NOT NULL,
        email        VARCHAR(254) NOT NULL,
        phone        VARCHAR(15) NOT NULL,
        address_id   INT,
        auth_id      INT NOT NULL,
    CONSTRAINT user_PK PRIMARY KEY (user_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: authentication
#------------------------------------------------------------

CREATE TABLE authentication(
        auth_id                 INT AUTO_INCREMENT NOT NULL,
        username                VARCHAR(100) NOT NULL,
        password                VARCHAR(255) NOT NULL,
        last_login_date         DATE NOT NULL,
        user_id                 INT NOT NULL,
    CONSTRAINT authentication_PK PRIMARY KEY (auth_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: admin
#------------------------------------------------------------

CREATE TABLE admin(
        user_id      INT NOT NULL,
        last_name    VARCHAR(100) NOT NULL,
        first_name   VARCHAR(100) NOT NULL,
        email        VARCHAR(254) NOT NULL,
        phone        VARCHAR(15) NOT NULL,
        address_id   INT,
        auth_id      INT NOT NULL,
    CONSTRAINT admin_PK PRIMARY KEY (user_id)
) ENGINE=InnoDB;


#------------------------------------------------------------
# Table: member
#------------------------------------------------------------

CREATE TABLE member(
        user_id          INT NOT NULL,
        member_status    ENUM("active","inactive") NOT NULL,
        last_name        VARCHAR(100) NOT NULL,
        first_name       VARCHAR(100) NOT NULL,
        email            VARCHAR(254) NOT NULL,
        phone            VARCHAR(15) NOT NULL,
        address_id       INT,
        auth_id          INT NOT NULL,
    CONSTRAINT member_PK PRIMARY KEY (user_id)
) ENGINE=InnoDB;



ALTER TABLE book
    ADD CONSTRAINT book_collection_FK
    FOREIGN KEY (collection_id)
    REFERENCES collection(collection_id);

ALTER TABLE address
    ADD CONSTRAINT address_city_FK
    FOREIGN KEY (city_id)
    REFERENCES city(city_id);

ALTER TABLE writes
    ADD CONSTRAINT writes_creator_FK
    FOREIGN KEY (creator_id)
    REFERENCES creator(creator_id);

ALTER TABLE writes
    ADD CONSTRAINT writes_book_FK
    FOREIGN KEY (book_id)
    REFERENCES book(book_id);

ALTER TABLE belongs_to
    ADD CONSTRAINT belongs_to_genre_FK
    FOREIGN KEY (genre_id)
    REFERENCES genre(genre_id);

ALTER TABLE belongs_to
    ADD CONSTRAINT belongs_to_book_FK
    FOREIGN KEY (book_id)
    REFERENCES book(book_id);

ALTER TABLE notification
    ADD CONSTRAINT notification_user_FK
    FOREIGN KEY (user_id)
    REFERENCES user(user_id);

ALTER TABLE loan
    ADD CONSTRAINT loan_member_FK
    FOREIGN KEY (user_id)
    REFERENCES member(user_id);

ALTER TABLE loan
    ADD CONSTRAINT loan_book_FK
    FOREIGN KEY (book_id)
    REFERENCES book(book_id);

ALTER TABLE reservation
    ADD CONSTRAINT reservation_member_FK
    FOREIGN KEY (user_id)
    REFERENCES member(user_id);

ALTER TABLE reservation
    ADD CONSTRAINT reservation_book_FK
    FOREIGN KEY (book_id)
    REFERENCES book(book_id);

ALTER TABLE user
    ADD CONSTRAINT user_address_FK
    FOREIGN KEY (address_id)
    REFERENCES address(address_id);

ALTER TABLE user
    ADD CONSTRAINT user_authentication_FK
    FOREIGN KEY (auth_id)
    REFERENCES authentication(auth_id);

ALTER TABLE user 
    ADD CONSTRAINT user_authentication_UK 
    UNIQUE (auth_id);

ALTER TABLE authentication
    ADD CONSTRAINT authentication_user_FK
    FOREIGN KEY (user_id)
    REFERENCES user(user_id);

ALTER TABLE authentication 
    ADD CONSTRAINT authentication_user_UK 
    UNIQUE (user_id);

ALTER TABLE admin
    ADD CONSTRAINT admin_user_FK
    FOREIGN KEY (user_id)
    REFERENCES user(user_id);

ALTER TABLE admin
    ADD CONSTRAINT admin_address_FK
    FOREIGN KEY (address_id)
    REFERENCES address(address_id);

ALTER TABLE admin
    ADD CONSTRAINT admin_authentication_FK
    FOREIGN KEY (auth_id)
    REFERENCES authentication(auth_id);

ALTER TABLE admin 
    ADD CONSTRAINT admin_authentication_UK 
    UNIQUE (auth_id);

ALTER TABLE member
    ADD CONSTRAINT member_user_FK
    FOREIGN KEY (user_id)
    REFERENCES user(user_id);

ALTER TABLE member
    ADD CONSTRAINT member_address_FK
    FOREIGN KEY (address_id)
    REFERENCES address(address_id);

ALTER TABLE member
    ADD CONSTRAINT member_authentication_FK
    FOREIGN KEY (auth_id)
    REFERENCES authentication(auth_id);

ALTER TABLE member 
    ADD CONSTRAINT member_authentication_UK 
    UNIQUE (auth_id);
