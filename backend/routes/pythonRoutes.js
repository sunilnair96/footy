// routes/pythonRoutes.js
const express = require("express");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const { executePythonScript } = require("../utils/pythonExecutor");

const router = express.Router();
const dir = path.join(__dirname, "../uploads");

console.log("Directory name ", dir);
// Create the uploads directory if it doesn't exist
if (!fs.existsSync(dir)) {
  console.log("Creating directory", dir);
  fs.mkdirSync(dir);
}

// Set up multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    console.log("Uploading to directory:", dir);

    cb(null, dir);
  },
  filename: (req, file, cb) => {
    console.log("Original file name:", file.originalname);
    cb(null, file.originalname);
  },
});

const upload = multer({ storage });

// Define the upload route for importing players
router.post("/upload", upload.single("file"), (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }

  const filePath = path.resolve(dir, req.file.filename);
  console.log("File uploaded to:", filePath);

  // Call the function to execute the import script
  executePythonScript(
    "C:\\Users\\sunil\\Projects\\footy\\scripts\\import_players.py",
    filePath,
    res
  );
});

module.exports = router;
