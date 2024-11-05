const express = require("express");
const cors = require("cors");
const multer = require("multer");
const path = require("path");
const { exec } = require("child_process");

const fs = require("fs");
require("dotenv").config();

const app = express();
const port = process.env.PORT || 5000; // Set the port

// Middleware
// Set up CORS to allow requests from http://localhost:3000
const corsOptions = {
  origin: "http://localhost:3000",
  methods: ["GET", "POST"], // Add more methods if needed
};
app.use(cors(corsOptions));

app.use(express.json()); // Parses incoming JSON requests

// Create the uploads directory if it doesn't exist
const dir = path.join(__dirname, "uploads");
if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir);
}

// Set up multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, dir); // Define the folder to store uploaded files
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname); // Use the original file name
  },
});

const upload = multer({ storage });

// Example route
app.get("/api/hello", (req, res) => {
  res.json({ message: "Hello from Express!" });
});

// Define the upload route
app.post("/upload", upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }

  // Log paths for debugging
  console.log("req.file.path:", req.file.path);
  console.log("__dirname:", __dirname);

  // Correct file path construction
  const filePath = path.resolve(__dirname, "uploads", req.file.filename);
  const escapedFilePath = filePath.replace(/\\/g, "\\\\");
  console.log("Escaped FilePath", escapedFilePath);
  exec(
    `C:\\Users\\sunil\\Projects\\footy\\venv\\Scripts\\activate && python C:\\Users\\sunil\\Projects\\footy\\scripts\\import_players.py "${filePath}"`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing script: ${error}`);
        return res.status(500).send("Error executing script");
      }
      console.log(stdout);
      res.send("Players imported successfully");
    }
  );
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
