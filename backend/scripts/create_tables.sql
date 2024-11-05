-- Create the teams table
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(3) UNIQUE NOT NULL,
    full_name VARCHAR(50)  -- Optional: Store full team name
);

-- Create the seasons table
CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    year INT UNIQUE NOT NULL
);

-- Create the games table
CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    code CHAR(2) UNIQUE NOT NULL,     -- Code for game type ('AF', 'SC', 'DS')
    name VARCHAR(50) NOT NULL         -- Full name of the game
);

-- Create the season_games table to link games to specific seasons
CREATE TABLE season_games (
    id SERIAL PRIMARY KEY,
    season_id INT REFERENCES seasons(id) ON DELETE CASCADE,
    game_id INT REFERENCES games(id) ON DELETE CASCADE,
    UNIQUE(season_id, game_id)        -- Ensures each game is linked only once per season
);

--Create Player Table
-- Create the Players table
CREATE TABLE Players (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    height DECIMAL(5, 2),
    weight DECIMAL(5, 2),
    draft_rank INT,
    draft_type VARCHAR(50),
    draft_year INT,
    primary_position VARCHAR(50),
    secondary_position VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the function to update the updated_at column
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER update_players_updated_at
BEFORE UPDATE ON Players
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();


--PlayerScores Table

CREATE TABLE PlayerScores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT,
    team_code VARCHAR(10),
    season INT,
    game INT,
    avg_score DECIMAL(5, 2),
    adj_score DECIMAL(5, 2),
    ppm INT,
    round_number INT,
    round_score INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES Players(id) -- Assuming there is a Players table
);

-- Create the team_stats table
-- Links each team's stats to a specific season
CREATE TABLE team_stats (
    id SERIAL PRIMARY KEY,
    season_id INT REFERENCES seasons(id) ON DELETE CASCADE,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    draws INT DEFAULT 0,
    points INT DEFAULT 0,
    -- Add other season-specific stats as needed
    UNIQUE(season_id, team_id)  -- Ensures each team has one row per season
);
