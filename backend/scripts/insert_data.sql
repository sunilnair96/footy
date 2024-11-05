-- Insert seasons
INSERT INTO seasons (year) VALUES
(2022),
(2023),
(2024),
(2025);

-- Insert teams
INSERT INTO teams (name, full_name) VALUES
('ADE', 'Adelaide Crows'),  
('BRL', 'Brisbane Lions'),
('CAR', 'Carlton Blues'),
('COL', 'Collingwood Magpies'),
('ESS', 'Essendon Bombers'),
('FRE', 'Fremantle Dockers'),
('GCS', 'Gold Coast Suns'),
('GEE', 'Geelong Cats'),
('GWS', 'Greater Western Sydney'),
('HAW', 'Hawthorn Hawks'),
('MEL', 'Melbourne Demons'),
('NTH', 'North Melbourne'),
('PTA', 'Port Adelaide'),
('RIC', 'Richmond Tigers'),
('STK', 'St Kilda Saints'),
('SYD', 'Sydney Swans'),
('WBD', 'Western Bulldogs'),
('WCE', 'West Coast Eagles');

-- Insert game types
INSERT INTO games (code, name) VALUES
('AF', 'AFL Fantasy'),
('SC', 'SuperCoach'),
('DS', 'DraftStars');

