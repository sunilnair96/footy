// backend/db/db.js
const { Pool } = require("pg");
require("dotenv").config();

// Database connection configuration
const pool = new Pool({
  user: process.env.PGUSER || "sunil",
  host: process.env.PGHOST || "localhost",
  database: process.env.PGDATABASE || "runnerz",
  password: process.env.PGPASSWORD || "python.08",
  port: process.env.PGPORT || 5432,
});

// Log connection parameters
console.log("db.js - Connecting to database with the following parameters:");
console.log(
  `User: ${process.env.PGUSER}, Database: ${process.env.PGPASSWORD}, Host: ${process.env.PGHOST}`
);

// Function to execute a query
const query = (text, params) => {
  return pool.query(text, params);
};

// Export the query function for use in other modules
module.exports = { query };

console.log("Connecting to database with the following parameters:");
console.log(
  `User: ${process.env.DB_USER}, Database: ${process.env.DB_NAME}, Host: ${process.env.DB_HOST}`
);

module.exports = {
  query: (text, params) => pool.query(text, params),
};
