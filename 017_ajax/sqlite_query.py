
import sqlite3


mydb = sqlite3.connect("db.sqlite3")

mydb.execute("""-- Insert Countries
INSERT INTO myapp_country (name) VALUES
('India'),
('United States'),
('Canada'),
('Australia'),
('United Kingdom');""")

mydb.execute("""-- Insert States
INSERT INTO myapp_state (name, country_id) VALUES
-- India (country_id = 1)
('Maharashtra', 1),
('Uttar Pradesh', 1),
('Karnataka', 1),
('Tamil Nadu', 1),
('Gujarat', 1),
-- United States (country_id = 2)
('California', 2),
('Texas', 2),
('New York', 2),
('Florida', 2),
('Illinois', 2),
-- Canada (country_id = 3)
('Ontario', 3),
('Quebec', 3),
('British Columbia', 3),
('Alberta', 3),
('Nova Scotia', 3),
-- Australia (country_id = 4)
('New South Wales', 4),
('Victoria', 4),
('Queensland', 4),
('Western Australia', 4),
('South Australia', 4),
-- United Kingdom (country_id = 5)
('England', 5),
('Scotland', 5),
('Wales', 5),
('Northern Ireland', 5),
('Jersey', 5);
""")

mydb.execute("""-- Insert Cities
INSERT INTO myapp_city (name, state_id) VALUES
-- Maharashtra (state_id = 1)
('Mumbai', 1),
('Pune', 1),
('Nagpur', 1),
('Nashik', 1),
('Aurangabad', 1),
-- Uttar Pradesh (2)
('Lucknow', 2),
('Kanpur', 2),
('Agra', 2),
('Varanasi', 2),
('Allahabad', 2),
-- Karnataka (3)
('Bengaluru', 3),
('Mysuru', 3),
('Mangalore', 3),
('Hubli', 3),
('Belagavi', 3),
-- Tamil Nadu (4)
('Chennai', 4),
('Coimbatore', 4),
('Madurai', 4),
('Tiruchirapalli', 4),
('Salem', 4),
-- Gujarat (5)
('Ahmedabad', 5),
('Surat', 5),
('Vadodara', 5),
('Rajkot', 5),
('Bhavnagar', 5),
-- California (6)
('Los Angeles', 6),
('San Francisco', 6),
('San Diego', 6),
('Sacramento', 6),
('Fresno', 6),
-- Texas (7)
('Houston', 7),
('Dallas', 7),
('Austin', 7),
('San Antonio', 7),
('Fort Worth', 7),
-- New York (8)
('New York City', 8),
('Buffalo', 8),
('Rochester', 8),
('Syracuse', 8),
('Albany', 8),
-- Florida (9)
('Miami', 9),
('Orlando', 9),
('Tampa', 9),
('Jacksonville', 9),
('St. Petersburg', 9),
-- Illinois (10)
('Chicago', 10),
('Aurora', 10),
('Naperville', 10),
('Joliet', 10),
('Rockford', 10),
-- Ontario (11)
('Toronto', 11),
('Ottawa', 11),
('Mississauga', 11),
('Brampton', 11),
('Hamilton', 11),
-- Quebec (12)
('Montreal', 12),
('Quebec City', 12),
('Gatineau', 12),
('Laval', 12),
('Sherbrooke', 12),
-- British Columbia (13)
('Vancouver', 13),
('Victoria', 13),
('Burnaby', 13),
('Surrey', 13),
('Kelowna', 13),
-- Alberta (14)
('Calgary', 14),
('Edmonton', 14),
('Red Deer', 14),
('Lethbridge', 14),
('St. Albert', 14),
-- Nova Scotia (15)
('Halifax', 15),
('Sydney', 15),
('Dartmouth', 15),
('Truro', 15),
('New Glasgow', 15),
-- New South Wales (16)
('Sydney', 16),
('Newcastle', 16),
('Wollongong', 16),
('Maitland', 16),
('Coffs Harbour', 16),
-- Victoria (17)
('Melbourne', 17),
('Geelong', 17),
('Ballarat', 17),
('Bendigo', 17),
('Shepparton', 17),
-- Queensland (18)
('Brisbane', 18),
('Gold Coast', 18),
('Cairns', 18),
('Townsville', 18),
('Toowoomba', 18),
-- Western Australia (19)
('Perth', 19),
('Fremantle', 19),
('Mandurah', 19),
('Bunbury', 19),
('Kalgoorlie', 19),
-- South Australia (20)
('Adelaide', 20),
('Mount Gambier', 20),
('Whyalla', 20),
('Port Augusta', 20),
('Gawler', 20),
-- England (21)
('London', 21),
('Manchester', 21),
('Birmingham', 21),
('Liverpool', 21),
('Leeds', 21),
-- Scotland (22)
('Edinburgh', 22),
('Glasgow', 22),
('Aberdeen', 22),
('Dundee', 22),
('Perth', 22),
-- Wales (23)
('Cardiff', 23),
('Swansea', 23),
('Newport', 23),
('Wrexham', 23),
('Bangor', 23),
-- Northern Ireland (24)
('Belfast', 24),
('Derry', 24),
('Lisburn', 24),
('Newtownabbey', 24),
('Carrickfergus', 24),
-- Jersey (25)
('St. Helier', 25),
('St. Ouen', 25),
('Grouville', 25),
('St. Saviour', 25),
('Trinity', 25);
""")



mydb.commit()