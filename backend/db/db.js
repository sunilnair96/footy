// backend/db/db.js
const { Pool } = require("pg");
//require("dotenv").config();

// Database connection configuration
const pool = new Pool({
  user: process.env.PGUSER,
  host: process.env.PGHOST,
  database: process.env.PGDATABASE,
  password: process.env.PGPASSWORD,
  port: process.env.PGPORT,
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
