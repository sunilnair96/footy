const express = require("express");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const { executePythonScript } = require("../utils/pythonExecutor");

const router = express.Router();
const dir = path.join(__dirname, "../uploads");
console.log("Inside pythonRoutes.js");
console.log("Directory for file uploads: ", dir);

// Create the uploads directory if it doesn't exist
if (!fs.existsSync(dir)) {
  console.log("Creating uploads directory...");
  fs.mkdirSync(dir);
}
console.log("Set up multer");
// Set up multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    console.log("Uploading file to directory:", dir);
    cb(null, dir); // Define where to store the uploaded file
  },
  filename: (req, file, cb) => {
    console.log("Original file name:", file.originalname);
    cb(null, file.originalname); // Use original file name
  },
});

const upload = multer({ storage });

// Define the upload route for importing players
router.post("/upload", upload.single("file"), (req, res) => {
  console.log("File upload route hit.");
  if (!req.file) {
    console.log("No file uploaded.");
    return res.status(400).send("No file uploaded.");
  }

  const filePath = path.resolve(dir, req.file.filename);
  console.log("File uploaded successfully. File path:", filePath);

  // Call the function to execute the Python script
  executePythonScript(
    "C:\\Users\\sunil\\Projects\\footy\\scripts\\import_players.py",
    filePath,
    res
  );
});

module.exports = router;
