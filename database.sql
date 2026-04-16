-- ==============================================
-- Nautilus — Script de création de la base de données
-- ==============================================

CREATE DATABASE IF NOT EXISTS nautilus;
USE nautilus;

-- ==============================================
-- Tables
-- ==============================================

CREATE TABLE fonds (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    isin VARCHAR(20) NOT NULL,
    date_creation DATE,
    aum DECIMAL(15, 2),
    devise VARCHAR(10)
);

CREATE TABLE actions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    ticker VARCHAR(10),
    pays VARCHAR(50),
    secteur VARCHAR(50),
    prix DECIMAL(10, 2)
);

CREATE TABLE composition (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fund_id INT NOT NULL,
    action_id INT NOT NULL,
    poids DECIMAL(5, 2),
    FOREIGN KEY (fund_id) REFERENCES fonds(id),
    FOREIGN KEY (action_id) REFERENCES actions(id)
);

CREATE TABLE performances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fund_id INT NOT NULL,
    date DATE NOT NULL,
    nav DECIMAL(10, 2),
    FOREIGN KEY (fund_id) REFERENCES fonds(id)
);

-- ==============================================
-- Données de test
-- ==============================================

INSERT INTO fonds (nom, isin, date_creation, aum, devise) VALUES
('Amundi World', 'FR0010315770', '2005-01-15', 15000000, 'EUR'),
('BNP Paribas Equity', 'FR0007022025', '2010-03-20', 8000000, 'EUR'),
('Lyxor CAC40', 'FR0007052782', '2001-06-10', 3500000, 'EUR'),
('Lazard Europe Equity', 'FR0010057612', '2003-06-15', 12000000, 'EUR'),
('Carmignac Patrimoine', 'FR0010135103', '1989-11-01', 25000000, 'EUR');

INSERT INTO actions (nom, ticker, pays, secteur, prix) VALUES
('Apple Inc.', 'AAPL', 'États-Unis', 'Tech', 189.50),
('BNP Paribas', 'BNP', 'France', 'Finance', 67.20),
('TotalEnergies', 'TTE', 'France', 'Énergie', 58.90),
('LVMH', 'MC', 'France', 'Luxe', 812.50),
('Microsoft', 'MSFT', 'États-Unis', 'Tech', 415.20),
('Amazon', 'AMZN', 'États-Unis', 'Tech', 198.90),
('ASML Holding', 'ASML', 'Pays-Bas', 'Tech', 782.30),
('Airbus', 'AIR', 'France', 'Industrie', 168.50),
('Sanofi', 'SAN', 'France', 'Santé', 92.40),
('L\'Oréal', 'OR', 'France', 'Consommation', 432.10),
('Nestlé', 'NESN', 'Suisse', 'Consommation', 94.80),
('SAP', 'SAP', 'Allemagne', 'Tech', 198.60),
('Hermès', 'RMS', 'France', 'Luxe', 2145.00),
('Stellantis', 'STLA', 'France', 'Automobile', 18.90);

INSERT INTO composition (fund_id, action_id, poids) VALUES
(1, 1, 40.00), (1, 2, 35.00), (1, 3, 25.00),
(2, 2, 50.00), (2, 4, 30.00), (2, 3, 20.00),
(3, 4, 60.00), (3, 1, 40.00),
(4, 3, 20.00), (4, 4, 15.00), (4, 6, 20.00), (4, 8, 15.00), (4, 9, 30.00),
(5, 1, 15.00), (5, 2, 15.00), (5, 5, 20.00), (5, 7, 20.00), (5, 10, 15.00), (5, 3, 15.00);

INSERT INTO performances (fund_id, date, nav) VALUES
(1, '2023-05-01', 95.20), (1, '2023-06-01', 96.80),
(1, '2023-07-01', 98.50), (1, '2023-08-01', 97.20),
(1, '2023-09-01', 99.10), (1, '2023-10-01', 100.00),
(1, '2023-11-01', 103.50),(1, '2023-12-01', 101.20),
(1, '2024-01-01', 104.80),(1, '2024-02-01', 106.30),
(1, '2024-03-01', 105.90),(1, '2024-04-01', 107.80),

(2, '2023-05-01', 93.10), (2, '2023-06-01', 94.50),
(2, '2023-07-01', 96.20), (2, '2023-08-01', 95.80),
(2, '2023-09-01', 97.30), (2, '2023-10-01', 100.00),
(2, '2023-11-01', 98.50), (2, '2023-12-01', 102.30),
(2, '2024-01-01', 101.50),(2, '2024-02-01', 103.80),
(2, '2024-03-01', 104.20),(2, '2024-04-01', 105.10),

(3, '2023-05-01', 96.50), (3, '2023-06-01', 98.20),
(3, '2023-07-01', 97.80), (3, '2023-08-01', 99.40),
(3, '2023-09-01', 101.20),(3, '2023-10-01', 100.00),
(3, '2023-11-01', 104.20),(3, '2023-12-01', 106.80),
(3, '2024-01-01', 105.30),(3, '2024-02-01', 107.50),
(3, '2024-03-01', 108.90),(3, '2024-04-01', 109.30),

(4, '2023-05-01', 98.20), (4, '2023-06-01', 99.50),
(4, '2023-07-01', 101.30),(4, '2023-08-01', 100.80),
(4, '2023-09-01', 102.50),(4, '2023-10-01', 100.00),
(4, '2023-11-01', 103.20),(4, '2023-12-01', 105.60),
(4, '2024-01-01', 107.20),(4, '2024-02-01', 108.90),
(4, '2024-03-01', 110.30),(4, '2024-04-01', 112.40),

(5, '2023-05-01', 97.80), (5, '2023-06-01', 96.50),
(5, '2023-07-01', 98.20), (5, '2023-08-01', 99.80),
(5, '2023-09-01', 98.60), (5, '2023-10-01', 100.00),
(5, '2023-11-01', 101.50),(5, '2023-12-01', 102.80),
(5, '2024-01-01', 104.20),(5, '2024-02-01', 103.60),
(5, '2024-03-01', 105.90),(5, '2024-04-01', 106.80);
