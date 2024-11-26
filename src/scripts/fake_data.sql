-- Script SQL pour remplir la base de données avec des données inspirées de l'univers de la Terre du Milieu de Tolkien.

-- ------------------------------------------------------------
-- Table: author
-- ------------------------------------------------------------

INSERT INTO author (first_name, last_name, bio) VALUES
('Elrond', 'Peredhel', 'Seigneur de Fondcombe, mi-elfe, mi-humain.'),
('Gandalf', 'Mithrandir', 'Mage et membre des Istari.'),
('Bilbon', 'Sacquet', 'Hobbit aventureux du Comté.'),
('Frodo', 'Sacquet', 'Neveu de Bilbon et porteur de l\'Anneau.'),
('Saruman', 'Le Blanc', 'Chef des Istari, tombé dans l\'ombre.'),
('Legolas', 'Vertefeuille', 'Prince elfe de la Forêt Noire.'),
('Gimli', 'Fils de Glóin', 'Nain du peuple de Durin.');

-- ------------------------------------------------------------
-- Table: genre
-- ------------------------------------------------------------

INSERT INTO genre (name_genre) VALUES
('Fantastique'),
('Aventure'),
('Histoire'),
('Poésie'),
('Mythologie');

-- ------------------------------------------------------------
-- Table: collection
-- ------------------------------------------------------------

INSERT INTO `collection` (collection_name, description) VALUES
('Chroniques de la Terre du Milieu', 'Collection d\'écrits historiques et mythologiques sur la Terre du Milieu.'),
('Chants Élfiques', 'Recueil de poèmes et de chansons elfiques.');

-- ------------------------------------------------------------
-- Table: city
-- ------------------------------------------------------------

INSERT INTO city (name) VALUES
('Fondcombe'),
('Le Comté'),
('Isengard'),
('La Forêt Noire'),
('Khazad-dûm');

-- ------------------------------------------------------------
-- Table: adresse
-- ------------------------------------------------------------

INSERT INTO adresse (number, street, postal_code, id_city) VALUES
('1', 'Val d\'Imladris', '00001', 1),     -- Fondcombe
('221B', 'Chemin de Grand\'Cour', '00002', 2),  -- Le Comté
('3', 'Tour d\'Orthanc', '00003', 3),     -- Isengard
('7', 'Route des Arbres', '00004', 4),    -- La Forêt Noire
('9', 'Mine de Moria', '00005', 5);       -- Khazad-dûm

-- ------------------------------------------------------------
-- Table: user
-- ------------------------------------------------------------

INSERT INTO `user` (first_name, last_name, date_of_birth, mail, phone, login, hashed_password, last_connection_date, member_status, id_adresse) VALUES
('Elrond', 'Peredhel', '5000-01-01', 'elrond@fondcombe.me', '0102030405', 'elrond', 'hash_elrond', NOW(), 'actif', 1),
('Bilbon', 'Sacquet', '2890-09-22', 'bilbon@comte.me', '0102030406', 'bilbon', 'hash_bilbon', NOW(), 'actif', 2),
('Saruman', 'Le Blanc', '1000-01-01', 'saruman@isengard.me', '0102030407', 'saruman', 'hash_saruman', NOW(), 'actif', 3),
('Legolas', 'Vertefeuille', '2931-01-01', 'legolas@foretnoire.me', '0102030408', 'legolas', 'hash_legolas', NOW(), 'actif', 4),
('Gimli', 'Fils de Glóin', '2879-01-01', 'gimli@moria.me', '0102030409', 'gimli', 'hash_gimli', NOW(), 'actif', 5);

-- ------------------------------------------------------------
-- Table: book
-- ------------------------------------------------------------

INSERT INTO book (title, publication_date, status, `condition`, isbn, page_number, editor, langue, resume, created_at, deleted_at, updated_at, id_collection, id_user, id_user_delete) VALUES
('L\'Histoire de l\'Anneau Unique', '3018-10-25', 'disponible', 'neuf', '978-0-00-000000-1', 500, 'Archives de Fondcombe', 'Quenya', 'Un récit détaillé de l\'Anneau Unique.', NOW(), NULL, NOW(), 1, 1, NULL),
('Les Contes Perdus', '2000-01-01', 'disponible', 'bon', '978-0-00-000000-2', 300, 'Bibliothèque du Comté', 'Ouesternien', 'Histoires anciennes de la Terre du Milieu.', NOW(), NULL, NOW(), 1, 2, NULL),
('La Chute de Númenor', '1000-01-01', 'disponible', 'neuf', '978-0-00-000000-3', 400, 'Isengard Press', 'Adûnaic', 'Chronique de la chute de l\'île de Númenor.', NOW(), NULL, NOW(), 1, 3, NULL),
('Chants de la Forêt Noire', '2951-01-01', 'disponible', 'neuf', '978-0-00-000000-4', 250, 'Éditions Elfiques', 'Sindarin', 'Recueil de poèmes et chansons de la Forêt Noire.', NOW(), NULL, NOW(), 2, 4, NULL),
('Les Mines de la Moria', '2850-01-01', 'disponible', 'bon', '978-0-00-000000-5', 350, 'Khazad-dûm Publications', 'Khuzdul', 'Descriptions et plans des mines de la Moria.', NOW(), NULL, NOW(), 1, 5, NULL);

-- ------------------------------------------------------------
-- Table: notification
-- ------------------------------------------------------------

INSERT INTO notification (message, notification_date, notification_type, seen, id_user) VALUES
('Le livre "Les Contes Perdus" est maintenant disponible.', NOW(), 'confirmation', 0, 1),
('Votre emprunt du livre "La Chute de Númenor" est dû dans 5 jours.', NOW(), 'rappel', 0, 2);

-- ------------------------------------------------------------
-- Table: loan
-- ------------------------------------------------------------

INSERT INTO loan (date_loan, return_date, id_user, id_book) VALUES
(NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY), 2, 2),  -- Bilbon emprunte "Les Contes Perdus"
(NOW(), DATE_ADD(NOW(), INTERVAL 15 DAY), 3, 3);  -- Saruman emprunte "La Chute de Númenor"

-- ------------------------------------------------------------
-- Table: reservation
-- ------------------------------------------------------------

INSERT INTO reservation (reservation_date, reservation_status, id_user, id_book) VALUES
(NOW(), 'attente', 4, 4),  -- Legolas réserve "Chants de la Forêt Noire"
(NOW(), 'confirmee', 5, 5); -- Gimli réserve "Les Mines de la Moria"

-- ------------------------------------------------------------
-- Table: role
-- ------------------------------------------------------------

INSERT INTO `role` (role_name, description) VALUES
('administrateur', 'Administrateur de la bibliothèque'),
('membre', 'Membre inscrit'),
('super_administrateur', 'Super administrateur avec tous les droits');

-- ------------------------------------------------------------
-- Table: is
-- ------------------------------------------------------------

INSERT INTO `is` (id_role, id_user) VALUES
(3, 1),  -- Elrond est super_administrateur
(2, 2),  -- Bilbon est membre
(1, 3),  -- Saruman est administrateur
(2, 4),  -- Legolas est membre
(2, 5);  -- Gimli est membre

-- ------------------------------------------------------------
-- Table: genre_book (association entre genres et livres)
-- ------------------------------------------------------------

-- Comme la table 'belongs' lie 'id_genre' et 'id_book', nous allons l'utiliser.

INSERT INTO belongs (id_genre, id_book) VALUES
(1, 1),  -- "L'Histoire de l'Anneau Unique" est du genre Fantastique
(3, 1),  -- et Histoire
(1, 2),  -- "Les Contes Perdus" est du genre Fantastique
(3, 2),  -- et Histoire
(3, 3),  -- "La Chute de Númenor" est du genre Histoire
(5, 3),  -- et Mythologie
(4, 4),  -- "Chants de la Forêt Noire" est du genre Poésie
(2, 5);  -- "Les Mines de la Moria" est du genre Aventure

-- ------------------------------------------------------------
-- Table: author_book (association entre auteurs et livres)
-- ------------------------------------------------------------

-- Utilisation de la table 'writes' pour lier 'id_author' et 'id_book'

INSERT INTO writes (id_author, id_book) VALUES
(1, 1),  -- Elrond a écrit "L'Histoire de l'Anneau Unique"
(2, 2),  -- Gandalf a écrit "Les Contes Perdus"
(3, 2),  -- Bilbon a co-écrit "Les Contes Perdus"
(4, 1),  -- Frodo a contribué à "L'Histoire de l'Anneau Unique"
(5, 3),  -- Saruman a écrit "La Chute de Númenor"
(6, 4),  -- Legolas a écrit "Chants de la Forêt Noire"
(7, 5);  -- Gimli a écrit "Les Mines de la Moria"

-- ------------------------------------------------------------
-- Table: modify (historique des modifications)

INSERT INTO `modify` (id_user, id_book, modification_date) VALUES
(1, 1, NOW()),  -- Elrond a modifié "L'Histoire de l'Anneau Unique"
(3, 3, NOW()),  -- Saruman a modifié "La Chute de Númenor"
(4, 4, NOW()),  -- Legolas a modifié "Chants de la Forêt Noire"
(5, 5, NOW());  -- Gimli a modifié "Les Mines de la Moria"
