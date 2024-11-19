-- ------------------------------------------------------------
-- Populating the "Library Management System 2.0" Database
-- ------------------------------------------------------------

-- Disable foreign key checks to allow for ordered inserts
SET FOREIGN_KEY_CHECKS = 0;

-- ------------------------------------------------------------
-- Table: city
-- ------------------------------------------------------------
INSERT INTO city (city_id, city_name) VALUES
(1, 'Hogsmeade'),
(2, 'Gotham'),
(3, 'Metropolis'),
(4, 'Asgard'),
(5, 'Krypton'),
(6, 'Narnia'),
(7, 'Middle-earth'),
(8, 'New York'),
(9, 'Chicago'),
(10, 'Star Wars Universe');

-- ------------------------------------------------------------
-- Table: address
-- ------------------------------------------------------------
INSERT INTO address (address_id, number, street, postal_code, city_id) VALUES
(1, '12', 'Griffin Street', '12345', 1),    -- Hogsmeade
(2, '1007', 'Mountain Drive', '67890', 2), -- Gotham
(3, '344', 'Clark Kent Avenue', '13579', 3), -- Metropolis
(4, 'Asgard Tower', 'Rainbow Road', '24680', 4), -- Asgard
(5, '1', 'Fortress of Solitude', '11223', 5), -- Krypton
(6, 'Narnia Central', 'Wardrobe Lane', '33445', 6), -- Narnia
(7, 'Bag End', 'Underhill Road', '55667', 7), -- Middle-earth
(8, '200', 'Park Avenue', '77889', 8), -- New York
(9, '500', 'Lake Shore Drive', '99000', 9), -- Chicago
(10, 'Death Star', 'Imperial Street', '00001', 10); -- Star Wars Universe

-- ------------------------------------------------------------
-- Table: collection
-- ------------------------------------------------------------
INSERT INTO collection (collection_id, collection_name, collection_description) VALUES
(1, 'Fantasy Classics', 'A collection of timeless fantasy literature.'),
(2, 'Science Fiction', 'Books that explore futuristic concepts and advanced technology.'),
(3, 'Superhero Saga', 'Stories of heroes with extraordinary abilities.'),
(4, 'Epic Adventures', 'Grand tales of adventure and exploration.'),
(5, 'Mystery & Thriller', 'Engaging mysteries and thrilling narratives.');

-- ------------------------------------------------------------
-- Table: genre
-- ------------------------------------------------------------
INSERT INTO genre (genre_id, genre_name) VALUES
(1, 'Fantasy'),
(2, 'Science Fiction'),
(3, 'Adventure'),
(4, 'Mystery'),
(5, 'Thriller'),
(6, 'Superhero'),
(7, 'Horror'),
(8, 'Romance'),
(9, 'Historical'),
(10, 'Drama');

-- ------------------------------------------------------------
-- Table: creator
-- ------------------------------------------------------------
INSERT INTO creator (creator_id, last_name, first_name, bio) VALUES
(1, 'Rowling', 'J.K.', 'British author, best known for the Harry Potter series.'),
(2, 'Tolkien', 'J.R.R.', 'English writer, poet, and professor, known for The Lord of the Rings.'),
(3, 'Lucas', 'George', 'American filmmaker and creator of Star Wars.'),
(4, 'Lee', 'Stan', 'American comic book writer, known for creating Batman.'),
(5, 'Best', 'Brian', 'American writer, best known for creating The Flash.'),
(6, 'Roth', 'Margaret', 'American novelist, short story writer, and essayist.'),
(7, 'King', 'Stephen', 'American author of horror, supernatural fiction, suspense, and fantasy novels.'),
(8, 'Orson', 'Scott', 'American filmmaker, writer, and photographer, known for The Lord of the Rings film trilogy.'),
(9, 'Lopez', 'Joss', 'American screenwriter, director, and producer known for Buffy the Vampire Slayer.'),
(10, 'Schecter', 'Mark', 'American comic book writer and novelist.');

-- ------------------------------------------------------------
-- Table: book
-- ------------------------------------------------------------
INSERT INTO book (book_id, title, publication_date, status, condition, isbn, page_count, publisher, language, summary, collection_id) VALUES
(1, 'Harry Potter and the Sorcerer\'s Stone', '1997-06-26', 'available', 'new', '978-0439708180', 309, 'Bloomsbury', 'English', 'The first book in the Harry Potter series.'),
(2, 'The Lord of the Rings: The Fellowship of the Ring', '1954-07-29', 'borrowed', 'good', '978-0544003415', 423, 'Allen & Unwin', 'English', 'The first volume of The Lord of the Rings trilogy.'),
(3, 'Star Wars: A New Hope', '1977-05-25', 'available', 'new', '978-0345339706', 208, 'Del Rey', 'English', 'The novelization of the original Star Wars film.'),
(4, 'Batman: Year One', '1987-02-01', 'reserved', 'good', '978-1563890454', 96, 'DC Comics', 'English', 'The origin story of Batman.'),
(5, 'The Flash: Rebirth', '2009-03-25', 'available', 'new', '978-1401244686', 80, 'DC Comics', 'English', 'The rebirth of the Flash in DC Comics.'),
(6, 'Good Omens', '1990-05-01', 'borrowed', 'damaged', '978-0060853983', 412, 'Workman Publishing', 'English', 'A comedic tale about the apocalypse.'),
(7, 'The Shining', '1977-01-28', 'available', 'good', '978-0385121675', 447, 'Doubleday', 'English', 'A horror novel about a haunted hotel.'),
(8, 'The Lord of the Rings: The Return of the King', '1955-10-20', 'available', 'new', '978-0618640157', 416, 'Allen & Unwin', 'English', 'The final volume of The Lord of the Rings trilogy.'),
(9, 'Buffy the Vampire Slayer: The Vampire Slayer', '1998-11-01', 'available', 'new', '978-1933916413', 180, 'Titan Books', 'English', 'A comic book series based on the Buffy the Vampire Slayer TV show.'),
(10, 'Wolverine: Origins', '2006-04-25', 'available', 'new', '978-1401244703', 144, 'Marvel Comics', 'English', 'Explores the origin of Wolverine.');

-- ------------------------------------------------------------
-- Table: writes
-- ------------------------------------------------------------
INSERT INTO writes (creator_id, book_id) VALUES
(1, 1),  -- J.K. Rowling wrote Harry Potter and the Sorcerer's Stone
(2, 2),  -- J.R.R. Tolkien wrote The Fellowship of the Ring
(3, 3),  -- George Lucas wrote Star Wars: A New Hope
(4, 4),  -- Stan Lee wrote Batman: Year One
(5, 5),  -- Brian Best wrote The Flash: Rebirth
(6, 6),  -- Margaret Roth wrote Good Omens
(7, 7),  -- Stephen King wrote The Shining
(8, 8),  -- Orson Scott wrote The Return of the King
(9, 9),  -- Joss Lopez wrote Buffy the Vampire Slayer: The Vampire Slayer
(10, 10); -- Mark Schecter wrote Wolverine: Origins

-- ------------------------------------------------------------
-- Table: belongs_to
-- ------------------------------------------------------------
INSERT INTO belongs_to (genre_id, book_id) VALUES
(1, 1),  -- Fantasy
(1, 2),  -- Fantasy
(2, 3),  -- Science Fiction
(6, 4),  -- Superhero
(6, 5),  -- Superhero
(4, 6),  -- Mystery
(7, 7),  -- Horror
(1, 8),  -- Fantasy
(6, 9),  -- Superhero
(6, 10); -- Superhero

-- ------------------------------------------------------------
-- Table: collection
-- ------------------------------------------------------------
INSERT INTO collection (collection_id, collection_name, collection_description) VALUES
(1, 'Fantasy Classics', 'A collection of timeless fantasy literature.'),
(2, 'Science Fiction', 'Books that explore futuristic concepts and advanced technology.'),
(3, 'Superhero Saga', 'Stories of heroes with extraordinary abilities.'),
(4, 'Horror', 'Books that evoke fear and suspense.'),
(5, 'Comedic Tales', 'Humorous and satirical stories.');

-- ------------------------------------------------------------
-- Table: user
-- ------------------------------------------------------------
INSERT INTO user (user_id, last_name, first_name, email, phone, address_id, auth_id) VALUES
(1, 'Potter', 'Harry', 'harry.potter@hogwarts.edu', '123-456-7890', 1, 1),
(2, 'Wayne', 'Bruce', 'bruce.wayne@gotham.com', '098-765-4321', 2, 2),
(3, 'Kent', 'Clark', 'clark.kent@metropolis.com', '555-555-5555', 3, 3),
(4, 'Thor', 'Odinson', 'thor@asgard.com', '111-222-3333', 4, 4),
(5, 'Kal-El', 'John', 'kal.el@krypton.com', '444-555-6666', 5, 5),
(6, 'Peter', 'Pevensie', 'peter.pevensie@narnia.com', '777-888-9999', 6, 6),
(7, 'Frodo', 'Baggins', 'frodo.baggins@middleearth.com', '222-333-4444', 7, 7),
(8, 'Tony', 'Stark', 'tony.stark@starkindustries.com', '333-444-5555', 8, 8),
(9, 'Barry', 'Allen', 'barry.allen@centralcity.com', '666-777-8888', 9, 9),
(10, 'Luke', 'Skywalker', 'luke.skywalker@starwars.com', '999-000-1111', 10, 10);

-- ------------------------------------------------------------
-- Table: authentication
-- ------------------------------------------------------------
INSERT INTO authentication (auth_id, username, password, last_login_date, user_id) VALUES
(1, 'harry_p', 'harry123', '2024-09-15', 1),
(2, 'batman_b', 'batman456', '2024-09-16', 2),
(3, 'superman_c', 'superman789', '2024-09-17', 3),
(4, 'thor_o', 'thor321', '2024-09-18', 4),
(5, 'superman_j', 'superman654', '2024-09-19', 5),
(6, 'peter_p', 'peter987', '2024-09-20', 6),
(7, 'frodo_b', 'frodo654', '2024-09-21', 7),
(8, 'ironman_t', 'ironman321', '2024-09-22', 8),
(9, 'flash_b', 'flash654', '2024-09-23', 9),
(10, 'luke_s', 'luke987', '2024-09-24', 10);

-- ------------------------------------------------------------
-- Table: admin
-- ------------------------------------------------------------
INSERT INTO admin (user_id, last_name, first_name, email, phone, address_id, auth_id) VALUES
(2, 'Wayne', 'Bruce', 'bruce.wayne@gotham.com', '098-765-4321', 2, 2),
(8, 'Stark', 'Tony', 'tony.stark@starkindustries.com', '333-444-5555', 8, 8);

-- ------------------------------------------------------------
-- Table: member
-- ------------------------------------------------------------
INSERT INTO member (user_id, member_status, last_name, first_name, email, phone, address_id, auth_id) VALUES
(1, 'active', 'Potter', 'Harry', 'harry.potter@hogwarts.edu', '123-456-7890', 1, 1),
(3, 'active', 'Kent', 'Clark', 'clark.kent@metropolis.com', '555-555-5555', 3, 3),
(4, 'active', 'Odinson', 'Thor', 'thor@asgard.com', '111-222-3333', 4, 4),
(5, 'active', 'El', 'John', 'kal.el@krypton.com', '444-555-6666', 5, 5),
(6, 'active', 'Pevensie', 'Peter', 'peter.pevensie@narnia.com', '777-888-9999', 6, 6),
(7, 'active', 'Baggins', 'Frodo', 'frodo.baggins@middleearth.com', '222-333-4444', 7, 7),
(9, 'active', 'Allen', 'Barry', 'barry.allen@centralcity.com', '666-777-8888', 9, 9),
(10, 'active', 'Skywalker', 'Luke', 'luke.skywalker@starwars.com', '999-000-1111', 10, 10);

-- ------------------------------------------------------------
-- Table: loan
-- ------------------------------------------------------------
INSERT INTO loan (loan_id, loan_date, actual_return_date, user_id, book_id) VALUES
(1, '2024-09-01', '2024-09-22', 1, 1), -- Harry borrows Harry Potter
(2, '2024-09-05', '2024-09-26', 3, 2), -- Clark borrows The Fellowship of the Ring
(3, '2024-09-10', '2024-09-30', 4, 3), -- Thor borrows Star Wars: A New Hope
(4, '2024-09-15', '2024-10-06', 5, 4), -- John borrows Batman: Year One
(5, '2024-09-20', '2024-10-11', 6, 5), -- Peter borrows The Flash: Rebirth
(6, '2024-09-25', '2024-10-16', 7, 6), -- Frodo borrows Good Omens
(7, '2024-09-30', '2024-10-21', 9, 7), -- Barry borrows The Shining
(8, '2024-10-05', '2024-10-26', 10, 8); -- Luke borrows The Return of the King

-- ------------------------------------------------------------
-- Table: reservation
-- ------------------------------------------------------------
INSERT INTO reservation (reservation_id, reservation_date, reservation_status, user_id, book_id) VALUES
(1, '2024-09-12', 'pending', 1, 3), -- Harry reserves Star Wars: A New Hope
(2, '2024-09-18', 'confirmed', 3, 4), -- Clark reserves Batman: Year One
(3, '2024-09-25', 'pending', 5, 6), -- John reserves Good Omens
(4, '2024-10-01', 'confirmed', 6, 7); -- Peter reserves The Shining

-- ------------------------------------------------------------
-- Table: notification
-- ------------------------------------------------------------
INSERT INTO notification (notification_id, message, notification_date, notification_type, channel, user_id) VALUES
(1, 'Reminder: Your loan for "Harry Potter and the Sorcerer\'s Stone" is due on 2024-09-22.', '2024-09-20', 'reminder', 'email', 1),
(2, 'Late Notice: "The Fellowship of the Ring" was due on 2024-09-26.', '2024-10-01', 'late', 'email', 3),
(3, 'Confirmation: Your reservation for "Batman: Year One" has been confirmed.', '2024-09-18', 'confirmation', 'email', 3),
(4, 'Reminder: Your loan for "Star Wars: A New Hope" is due on 2024-09-30.', '2024-09-28', 'reminder', 'email', 4),
(5, 'Reminder: Your loan for "Batman: Year One" is due on 2024-10-06.', '2024-10-04', 'reminder', 'email', 5),
(6, 'Confirmation: Your reservation for "Good Omens" has been confirmed.', '2024-09-25', 'confirmation', 'email', 5),
(7, 'Reminder: Your loan for "Good Omens" is due on 2024-10-16.', '2024-10-14', 'reminder', 'email', 7),
(8, 'Late Notice: "The Shining" was due on 2024-10-21.', '2024-10-25', 'late', 'email', 9),
(9, 'Reminder: Your loan for "The Return of the King" is due on 2024-10-26.', '2024-10-24', 'reminder', 'email', 10),
(10, 'Confirmation: Your reservation for "The Shining" has been confirmed.', '2024-10-01', 'confirmation', 'email', 6);

-- ------------------------------------------------------------
-- Table: notification
-- ------------------------------------------------------------
-- Note: The 'notification' table is already populated above.

-- ------------------------------------------------------------
-- Table: authentication
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: admin
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: member
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: loan
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: reservation
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: notification
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: user
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: authentication
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: admin
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Table: member
-- ------------------------------------------------------------
-- Already populated above.

-- ------------------------------------------------------------
-- Re-enable foreign key checks
-- ------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 1;
