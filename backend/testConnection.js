const { Pool } = require("pg");
require("dotenv").config();

const pool = new Pool({
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  host: "localhost",
  port: 5432,
  database: process.env.POSTGRES_DB,
});

const fetchGames = async () => {
  try {
    const res = await pool.query("SELECT * FROM games");
    console.log(res.rows);
  } catch (err) {
    console.error("Error fetching games:", err);
  } finally {
    pool.end();
  }
};

fetchGames();
