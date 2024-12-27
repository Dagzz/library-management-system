/* --------------------------------------------------------------
 __          __                       __ _     ______    _          _____        _        
 \ \        / /                      / _| |   |  ____|  | |        |  __ \      | |       
  \ \  /\  / /_ _ _ __ ___ _ __ __ _| |_| |_  | |__ __ _| | _____  | |  | | __ _| |_ __ _ 
   \ \/  \/ / _` | '__/ __| '__/ _` |  _| __| |  __/ _` | |/ / _ \ | |  | |/ _` | __/ _` |
    \  /\  / (_| | | | (__| | | (_| | | | |_  | | | (_| |   <  __/ | |__| | (_| | || (_| |
     \/  \/ \__,_|_|  \___|_|  \__,_|_|  \__| |_|  \__,_|_|\_\___| |_____/ \__,_|\__\__,_|
                                                                                          
-------------------------------------------------------------- */

#------------------------------------------------------------
# Table: city
#------------------------------------------------------------

INSERT INTO city (name) VALUES
('Stormwind City'),
('Ironforge'),
('Darnassus'),
('Orgrimmar'),
('Undercity'),
('Thunder Bluff'),
('Booty Bay'),
('Gadgetzan'),
('Ratchet'),
('Stonard'),
('Crossroads'),
('Brill'),
('Revantusk Village'),
('Valor\'s Edge'),
('Thunderlord Stronghold'),
('Astranaar'),
('Feathermoon'),
('Freewind Post'),
('Marshal\'s Refuge'),
('Vendetta Point');

#------------------------------------------------------------
# Table: author
#------------------------------------------------------------

INSERT INTO author (first_name, last_name, bio) VALUES
('Jaina', 'Proudmoore', 'Archmage of the Kirin Tor and leader of the Alliance\'s magical community. Renowned for her mastery of arcane magic and diplomatic prowess.'),
('Thrall', NULL, 'Former Warchief of the Horde and a powerful shaman. Known for uniting the Horde and leading it with honor and strength.'),
('Tyrande', 'Whisperwind', 'High Priestess of Elune and leader of the Night Elves. A fierce warrior and protector of her people.'),
('Garrosh', 'Hellscream', 'Son of Grommash Hellscream and a formidable warrior. Later becomes Warchief of the Horde, known for his aggressive strategies.'),
('Khadgar', NULL, 'One of the most powerful sorcerers in Azeroth. A key member of the Kirin Tor and instrumental in defeating the Burning Legion.'),
('Anduin', 'Lothar', 'Legendary general of the Alliance and key figure in the First and Second Wars. Known as the "Lion of Azeroth" for his bravery.'),
('Grommash', 'Hellscream', 'Chieftain of the Warsong Clan and one of the most feared warriors in the Horde. Played a pivotal role in the creation of the new Horde.'),
('Sylvanas', 'Windrunner', 'Ranger-General of Silvermoon and leader of the Forsaken. A skilled archer and tactician with a tragic past.'),
('Medivh', NULL, 'The Last Guardian and a powerful mage. Played a crucial role in both the First and Second Wars, though his legacy is marred by his own inner conflicts.'),
('Arthas', 'Menethil', 'Prince of Lordaeron who becomes the Lich King. His tragic fall from grace is one of the most pivotal stories in WoW lore.'),
('Genn', 'Greymane', 'King of Gilneas and a valiant warrior. Known for his leadership during the events leading up to and during the Second War.'),
('Uther', 'the Lightbringer', 'Noble paladin and mentor to Prince Arthas. Revered as a paragon of justice and righteousness within the Alliance.'),
('Rexxar', NULL, 'Legendary Beastmaster and champion of the wilds. Travels between Horde and Alliance territories, fostering understanding and cooperation.'),
('Cairne', 'Bloodhoof', 'High Chieftain of the Tauren and a wise leader. Revered for his spiritual guidance and dedication to his people.'),
('Taretha', 'Foxton', 'Manager of the Stormwind Library. Known for her organizational skills and vast knowledge of Azeroth\'s history.'),
('Lor\'themar', 'Theron', 'Regent Lord of Quel\'Thalas and leader of the Blood Elves. A strategic mind and skilled warrior.'),
('Brann', 'Bronzebeard', 'Adventurer and historian from the dwarven kingdom. Known for his explorations and preservation of ancient knowledge.'),
('Alexandros', 'Mograine', 'Paladin and member of the Knights of the Silver Hand. Known for his unwavering dedication to combating evil.'),
('Baelgun', NULL, 'Chief Librarian of the Kirin Tor. Keeper of ancient tomes and secrets of Azeroth, ensuring the preservation of magical knowledge.'),
('Elandra', 'Moonwhisper', 'Elven scholar and historian specializing in ancient Night Elf magic. Dedicated to uncovering lost spells and preserving elven heritage.');

#------------------------------------------------------------
# Table: genre
#------------------------------------------------------------

INSERT INTO genre (name_genre) VALUES
('Magic'),
('Warfare'),
('History'),
('Crafting'),
('Adventures'),
('Beast Mastery'),
('Lore'),
('Engineering'),
('Alchemy'),
('Diplomacy');

#------------------------------------------------------------
# Table: collection
#------------------------------------------------------------


INSERT INTO collection (description, collection_name) VALUES
('A compilation of magical spellbooks, arcane theories, and sorcery practices used by the mages and sorcerers of Azeroth.', 'Arcane Tomes'),
('Guides detailing military strategies, battle tactics, and historical warfare accounts essential for generals and warriors.', 'Battle Manuals'),
('Chronicles the significant events, legendary figures, and pivotal moments that have shaped the history of Azeroth.', 'Azerothian History'),
('Manuals for blacksmithing, alchemy, engineering, and other crafting professions, providing step-by-step instructions for artisans.', 'Crafting Guides'),
('Stories of heroic quests, explorations, and epic journeys undertaken by adventurers across the various regions of Azeroth.', 'Adventurer\'s Tales'),
('Detailed accounts of taming, training, and understanding the diverse wildlife and mythical creatures inhabiting Azeroth.', 'Beastmaster\'s Compendium'),
('Technical drawings, inventions, and engineering projects that showcase the ingenuity and mechanical prowess of Azerothian engineers.', 'Engineering Schematics'),
('Documentation of spiritual practices, elemental summons, and shamanic ceremonies performed by the shamans of the Horde and other factions.', 'Shamanic Rituals'),
('Sacred texts and doctrines outlining the principles, oaths, and combat techniques of the noble paladins serving the Alliance.', 'Paladin\'s Codex'),
('Field guides and survival manuals for rangers and scouts, covering tracking, archery, and wilderness navigation.', 'Ranger\'s Almanac');

#------------------------------------------------------------
# Table: language
#------------------------------------------------------------

INSERT INTO language (language_name) VALUES
('Common'),
('Orcish'),
('Darnassian'),
('Dwarvish'),
('Taurahe'),
('Thalassian'),
('Draenei'),
('Gnomish'),
('Goblin'),
('Troll'),
('Old Tongue'),
('Darkspeak'),
('Fel Sorcery'),
('Titan'),
('Draconic'),
('Shal\'dorei'),
('Saurfang'),
('Runic'),
('Elemental'),
('Mystic');

#------------------------------------------------------------
# Table: address
#------------------------------------------------------------

INSERT INTO address (number, street, postal_code, id_city) VALUES
('12A', 'Mage Quarter', 'SW-1001', 1),           -- Stormwind City
('34B', 'Ironforge Street', 'IF-2002', 2),       -- Ironforge
('56C', 'Moonfall Avenue', 'DA-3003', 3),        -- Darnassus
('78D', 'Warsong Boulevard', 'OR-4004', 4),      -- Orgrimmar
('90E', 'Shadow Alley', 'UC-5005', 5),           -- Undercity
('21F', 'Eagle Rise Terrace', 'TB-6006', 6),     -- Thunder Bluff
('43G', 'Pirate\'s Cove Road', 'BB-7007', 7),    -- Booty Bay
('65H', 'Goblin Workshop Lane', 'GZ-8008', 8),   -- Gadgetzan
('87I', 'Pirate\'s Den Street', 'RA-9009', 9),   -- Ratchet
('09J', 'Stonard Wharf', 'ST-1010', 10),         -- Stonard
('11K', 'Valley of Heroes Road', 'CR-1111', 11),  -- Crossroads
('22L', 'Silverpine Road', 'BR-1212', 12),        -- Brill
('33M', 'Revenant\'s Rest Lane', 'RV-1313', 13),  -- Revantusk Village
('44N', 'Valor\'s Edge Blvd', 'VE-1414', 14),     -- Valor's Edge
('55O', 'Lightning Spur Road', 'TL-1515', 15),    -- Thunderlord Stronghold
('66P', 'Starfire Path', 'AS-1616', 16),          -- Astranaar
('77Q', 'Feathermoon Way', 'FM-1717', 17),        -- Feathermoon
('88R', 'Windrunner\'s Trail', 'FW-1818', 18),    -- Freewind Post
('99S', 'Refugee\'s Refuge Road', 'MR-1919', 19), -- Marshal's Refuge
('10T', 'Vendetta Point Lane', 'VP-2020', 20);    -- Vendetta Point

#------------------------------------------------------------
# Table: user
#------------------------------------------------------------

INSERT INTO user (
    first_name, 
    last_name, 
    date_of_birth, 
    mail, 
    phone, 
    login, 
    hashed_password, 
    last_connection_date, 
    is_active, 
    id_address
) VALUES
('Jaina', 'Proudmoore', '1975-05-15', 'jaina@frostmourne.com', '555-1234', 'jaina_p', 'hashed_pw_jaina_p', '2024-12-20 10:00:00', TRUE, 1),
('Thrall', 'Haut-Shaman', '1980-08-22', 'thrall@shadowfang.com', '555-5678', 'thrall_h', 'hashed_pw_thrall_h', '2024-12-21 11:30:00', TRUE, 2),
('Tyrande', 'Whisperwind', '1972-03-30', 'tyrande@moonfall.com', '555-8765', 'tyrande_w', 'hashed_pw_tyrande_w', '2024-12-22 09:15:00', TRUE, 3),
('Garrosh', 'Hellscream', '1983-07-19', 'garrosh@warsong.com', '555-4321', 'garrosh_h', 'hashed_pw_garrosh_h', '2024-12-23 14:45:00', TRUE, 4),
('Khadgar', 'Mage-Réformé', '1965-11-05', 'khadgar@kirintor.com', '555-6543', 'khadgar_mr', 'hashed_pw_khadgar_mr', '2024-12-24 08:20:00', TRUE, 5),
('Anduin', 'Lothar', '1978-02-14', 'anduin@lionofazeroth.com', '555-7890', 'anduin_l', 'hashed_pw_anduin_l', '2024-12-25 12:30:00', TRUE, 6),
('Grommash', 'Hellscream', '1968-09-09', 'grommash@warsong.com', '555-3210', 'grommash_h', 'hashed_pw_grommash_h', '2024-12-26 16:00:00', TRUE, 7),
('Sylvanas', 'Windrunner', '1981-04-27', 'sylvanas@forsaken.com', '555-2134', 'sylvanas_w', 'hashed_pw_sylvanas_w', '2024-12-27 09:45:00', TRUE, 8),
('Medivh', 'Gardien', '1960-06-18', 'medivh@guardian.com', '555-3412', 'medivh_g', 'hashed_pw_medivh_g', '2024-12-28 11:15:00', TRUE, 9),
('Arthas', 'Menethil', '1969-12-05', 'arthas@frostmourne.com', '555-4321', 'arthas_m', 'hashed_pw_arthas_m', '2024-12-29 13:30:00', TRUE, 10),
('Genn', 'Greymane', '1977-08-08', 'genn@gilneas.com', '555-5678', 'genn_g', 'hashed_pw_genn_g', '2024-12-30 15:45:00', TRUE, 11),
('Uther', 'the Lightbringer', '1955-01-01', 'uther@lightbringer.com', '555-6789', 'uther_lb', 'hashed_pw_uther_lb', '2024-12-31 17:00:00', TRUE, 12),
('Rexxar', 'Champion', '1985-03-12', 'rexxar@beastmaster.com', '555-7890', 'rexxar_c', 'hashed_pw_rexxar_c', '2025-01-01 10:30:00', TRUE, 13),
('Cairne', 'Bloodhoof', '1962-04-04', 'cairne@tauren.com', '555-8901', 'cairne_b', 'hashed_pw_cairne_b', '2025-01-02 09:00:00', TRUE, 14),
('Taretha', 'Foxton', '1970-05-25', 'taretha@stormwind.com', '555-9012', 'taretha_f', 'hashed_pw_taretha_f', '2025-01-03 14:10:00', TRUE, 15),
('Lor\'themar', 'Theron', '1976-07-19', 'lorthemar@qualthalas.com', '555-0123', 'lorthemar_t', 'hashed_pw_lorthemar_t', '2025-01-04 11:20:00', TRUE, 16),
('Brann', 'Bronzebeard', '1969-10-10', 'brann@bronze.com', '555-2345', 'brann_b', 'hashed_pw_brann_b', '2025-01-05 13:35:00', TRUE, 17),
('Alexandros', 'Mograine', '1974-02-28', 'alexandros@silverhand.com', '555-3456', 'alexandros_m', 'hashed_pw_alexandros_m', '2025-01-06 16:50:00', TRUE, 18),
('Baelgun', 'Librarian', '1958-09-15', 'baelgun@kirintor.com', '555-4567', 'baelgun_l', 'hashed_pw_baelgun_l', '2025-01-07 08:25:00', TRUE, 19),
('Elandra', 'Moonwhisper', '1983-11-22', 'elandra@moonwhisper.com', '555-5678', 'elandra_m', 'hashed_pw_elandra_m', '2025-01-08 12:40:00', TRUE, 20),
('Valeera', 'Sanguinar', '1988-10-10', 'valeera@bloodelf.com', '555-6789', 'valeera_s', 'hashed_pw_valeera_s', '2025-01-09 14:50:00', TRUE, 1),
('Turalyon', 'Lightbringer', '1960-11-11', 'turalyon@alliance.com', '555-9876', 'turalyon_lb', 'hashed_pw_turalyon_lb', '2025-01-10 16:10:00', TRUE, 2),
('Alleria', 'Windrunner', '1965-02-14', 'alleria@silvermoon.com', '555-3459', 'alleria_w', 'hashed_pw_alleria_w', '2025-01-11 09:30:00', TRUE, 3),
('Bolvar', 'Fordragon', '1972-09-15', 'bolvar@dragon.com', '555-1289', 'bolvar_f', 'hashed_pw_bolvar_f', '2025-01-12 18:20:00', TRUE, 4),
('Magni', 'Bronzebeard', '1955-05-05', 'magni@dwarves.com', '555-6780', 'magni_b', 'hashed_pw_magni_b', '2025-01-13 12:45:00', TRUE, 5),
('Kael\'thas', 'Sunstrider', '1978-07-23', 'kaelthas@qualthalas.com', '555-4568', 'kaelthas_s', 'hashed_pw_kaelthas_s', '2025-01-14 11:35:00', TRUE, 6),
('Illidan', 'Stormrage', '1965-12-12', 'illidan@stormrage.com', '555-6781', 'illidan_s', 'hashed_pw_illidan_s', '2025-01-15 15:25:00', TRUE, 7),
('Maiev', 'Shadowsong', '1973-03-21', 'maiev@warden.com', '555-4569', 'maiev_s', 'hashed_pw_maiev_s', '2025-01-16 10:15:00', TRUE, 8),
('Malfurion', 'Stormrage', '1960-06-06', 'malfurion@stormrage.com', '555-7891', 'malfurion_s', 'hashed_pw_malfurion_s', '2025-01-17 13:50:00', TRUE, 9),
('Anub', 'Arak', '1950-10-10', 'anubarak@nerubian.com', '555-3450', 'anubarak_n', 'hashed_pw_anubarak_n', '2025-01-18 08:30:00', TRUE, 10);

#------------------------------------------------------------
# Table: role
#------------------------------------------------------------

INSERT INTO role (description, role_name) VALUES
('Superadmins have access to all permissions and can also manage roles', 'superadmin'),
('Admins can manage all information apart from roles', 'admin'),
('Users can view, borrow and reserve books', 'user');


#------------------------------------------------------------
# Table: user_role
#------------------------------------------------------------

INSERT INTO user_role (id_user, id_role) VALUES
(1, 1),  
(1, 2),  
(2, 1), 
(3, 1),  
(4, 1), 
(5, 2),  
(6, 1),  
(7, 1),  
(8, 1),  
(9, 2);

#------------------------------------------------------------
# Table: book
#------------------------------------------------------------

INSERT INTO book (
    title, 
    publication_date, 
    status, 
    aspect, 
    isbn, 
    page_number, 
    editor, 
    resume, 
    created_at, 
    deleted_at, 
    id_collection, 
    id_language
) VALUES

('Arcane Mastery: A Guide for Aspiring Mages', '2024-01-01', 'available', 'new', '9781234567001', 300, 'Kirin Tor Press', 'A comprehensive guide for mastering arcane spells and rituals.', NOW(), NULL, 1, 1),
('The Secrets of Fel Magic', '2024-02-15', 'available', 'good', '9781234567002', 250, 'Shadow Council', 'A dark exploration of forbidden Fel magic techniques.', NOW(), NULL, 1, 13),
('Runes and Glyphs: Ancient Dwarvish Magic', '2024-03-10', 'available', 'new', '9781234567003', 280, 'Ironforge Publications', 'A study of ancient dwarven magical runes and their applications.', NOW(), NULL, 1, 4),

('The Art of War: A Horde Perspective', '2024-04-20', 'borrowed', 'good', '9781234567004', 400, 'Warsong Clan Archives', 'An in-depth analysis of Horde battle strategies.', NOW(), NULL, 2, 2),
('Alliance Tactics: Winning the Unwinnable', '2024-05-25', 'reserved', 'new', '9781234567005', 320, 'Stormwind Military Press', 'A treatise on advanced Alliance military strategies.', NOW(), NULL, 2, 1),

('Azeroth: A Complete History', '2024-06-30', 'available', 'new', '9781234567006', 500, 'Historian\'s Guild', 'A detailed account of the history of Azeroth, from its creation to the present day.', NOW(), NULL, 3, 1),
('The Fall of Lordaeron', '2024-07-15', 'available', 'damaged', '9781234567007', 350, 'Silvermoon Press', 'A tragic recounting of the fall of the kingdom of Lordaeron.', NOW(), NULL, 3, 6),
('The War of the Ancients Chronicles', '2024-08-12', 'available', 'good', '9781234567008', 450, 'Darnassus Archives', 'A historical account of the War of the Ancients.', NOW(), NULL, 3, 3),

('The Alchemist\'s Handbook', '2024-09-01', 'available', 'new', '9781234567009', 200, 'Gadgetzan Laboratory Press', 'A guide to creating potions and elixirs.', NOW(), NULL, 4, 9),
('Engineering Marvels of Azeroth', '2024-10-10', 'available', 'good', '9781234567010', 320, 'Tinker\'s Guild', 'An overview of groundbreaking engineering inventions.', NOW(), NULL, 4, 8),
('Mastering Blacksmithing: From Ore to Weapon', '2024-11-05', 'borrowed', 'good', '9781234567011', 280, 'Ironforge Smithy', 'Step-by-step guide to blacksmithing techniques.', NOW(), NULL, 4, 4),

('Journeys Beyond the Dark Portal', '2024-12-20', 'available', 'new', '9781234567012', 340, 'Explorer\'s League', 'An adventurer\'s guide to Outland.', NOW(), NULL, 5, 1),
('Secrets of the Emerald Dream', '2025-01-15', 'available', 'good', '9781234567013', 290, 'Druidic Lore', 'Explorations and revelations within the Emerald Dream.', NOW(), NULL, 5, 3),

('Training the Wild Beasts of Azeroth', '2025-02-05', 'available', 'new', '9781234567014', 310, 'Horde Beastmasters', 'A guide for taming and training Azeroth\'s wildlife.', NOW(), NULL, 6, 2),
('The Hunter\'s Companion', '2025-03-10', 'available', 'good', '9781234567015', 220, 'Hunter\'s Guild', 'Tips and tricks for hunting in the wilderness.', NOW(), NULL, 6, 1),

('The Titan Pantheon: Creators of Azeroth', '2025-04-01', 'reserved', 'new', '9781234567016', 350, 'Archivist\'s Guild', 'An exploration of the Titans and their influence on Azeroth.', NOW(), NULL, 7, 14),
('The Burning Legion Compendium', '2025-05-20', 'available', 'new', '9781234567017', 420, 'Dalaran Library', 'A detailed history of the Burning Legion.', NOW(), NULL, 7, 13),

('The Art of Negotiation: Horde and Alliance Diplomacy', '2025-06-10', 'available', 'good', '9781234567018', 310, 'Shattrath Peacekeepers', 'A comprehensive guide to effective diplomacy.', NOW(), NULL, 10, 1),
('Peace Through Strength: The Tauren Way', '2025-07-25', 'borrowed', 'good', '9781234567019', 300, 'Thunder Bluff Elders', 'A philosophical guide to peaceful coexistence.', NOW(), NULL, 10, 5);

#------------------------------------------------------------
# Table: writes
#------------------------------------------------------------

INSERT INTO writes (id_author, id_book) VALUES
(1, 1),  
(9, 2), 
(17, 3), 
(4, 4),
(6, 5),
(18, 6),
(10, 7),
(3, 8),
(5, 9),  
(19, 10), 
(2, 11), 
(17, 12),
(3, 13),
(13, 14), 
(13, 15), 
(16, 16), 
(5, 17),  
(8, 18),  
(14, 19); 

#------------------------------------------------------------
# Table: genre_book
#------------------------------------------------------------

INSERT INTO genre_book (id_genre, id_book) VALUES
(1, 1), 
(1, 2),  
(1, 3), 
(2, 4), 
(2, 5), 
(3, 6), 
(3, 7),  
(3, 8),  
(4, 9), 
(4, 10), 
(4, 11), 
(5, 12), 
(5, 13), 
(6, 14), 
(6, 15), 
(7, 16), 
(7, 17), 
(10, 18), 
(10, 19);


#------------------------------------------------------------
# Table: loan
#------------------------------------------------------------

INSERT INTO loan (date_loan, return_date, id_user, id_book) VALUES
('2024-12-01 10:00:00', '2024-12-15 10:00:00', 1, 1),  
('2024-12-02 11:00:00', '2024-12-16 11:00:00', 2, 4),  
('2024-12-03 12:00:00', '2024-12-17 12:00:00', 3, 6),  
('2024-12-04 13:00:00', '2024-12-18 13:00:00', 4, 8),  
('2024-12-05 14:00:00', '2024-12-19 14:00:00', 5, 12); 

#------------------------------------------------------------
# Table: reservation
#------------------------------------------------------------

INSERT INTO reservation (reservation_date, is_confirmed, id_user, id_book) VALUES
('2024-12-06 15:00:00', TRUE, 6, 5), 
('2024-12-07 16:00:00', FALSE, 7, 11), 
('2024-12-08 17:00:00', TRUE, 8, 18),
('2024-12-09 18:00:00', FALSE, 9, 17), 
('2024-12-10 19:00:00', TRUE, 10, 19); 

#------------------------------------------------------------
# Table: modification
#------------------------------------------------------------

INSERT INTO modification (date_modification, id_book, id_user) VALUES
('2024-12-11 10:00:00', 1, 1),  
('2024-12-12 11:00:00', 4, 2),  
('2024-12-13 12:00:00', 6, 3), 
('2024-12-14 13:00:00', 8, 4),  
('2024-12-15 14:00:00', 12, 5); 
