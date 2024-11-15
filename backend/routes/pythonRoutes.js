const express = require("express");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const { executePythonScript } = require("../utils/pythonExecutor");
const { spawn } = require("child_process");

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

router.post("/run-join-player", (req, res) => {
  const season = req.body.season;
  const pythonPath = path.join(
    __dirname,
    "..",
    "..",
    "venv",
    "Scripts",
    "python.exe"
  ); // Path to the virtual environment's Python
  console.log(pythonPath);

  const scriptPath = path.join(__dirname, "..", "src", "joinPlayerData.py");
  console.log(scriptPath);

  const process = spawn(pythonPath, [scriptPath, season]);

  let output = "";
  let errorOutput = "";

  process.stdout.on("data", (data) => {
    output += data.toString();
  });

  process.stderr.on("data", (data) => {
    errorOutput += data.toString();
  });

  process.on("close", (code) => {
    if (code === 0) {
      res.json({ output });
    } else {
      console.error("Error:", errorOutput);
      res.status(500).json({ error: errorOutput });
    }
  });
});

module.exports = router;
