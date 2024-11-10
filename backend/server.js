// server.js
const express = require("express");
const cors = require("cors");
require("dotenv").config();

const pythonRoutes = require("./routes/pythonRoutes"); // Import the Python routes

const app = express();
const port = process.env.PORT || 5000;

// Set up CORS
const corsOptions = {
  origin: "http://localhost:3000",
  methods: ["GET", "POST"],
};
app.use(cors(corsOptions));
app.use(express.json());

// Use pythonRoutes for all routes related to Python script handling
app.use("/api", pythonRoutes);

// Example route
app.get("/api/hello", (req, res) => {
  res.json({ message: "Hello from Express!" });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
