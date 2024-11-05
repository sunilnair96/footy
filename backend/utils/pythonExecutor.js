// utils/pythonExecutor.js
const { exec } = require("child_process");

const executePythonScript = (scriptPath, filePath, res) => {
  exec(
    `C:\\Users\\sunil\\Projects\\footy\\venv\\Scripts\\activate && python "${scriptPath}" "${filePath}"`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing script: ${error}`);
        return res.status(500).send("Error executing script");
      }
      console.log(stdout);
      res.send("Script executed successfully");
    }
  );
};

module.exports = { executePythonScript };
