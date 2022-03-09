const { exec } = require("child_process");

const question = '"Quand est né Vin Diesel ?"'

const path = process.platform === 'win32' ? "python3 .\\python_scripts\\qa.py " : "python3 ./python_scripts/qa.py "
exec(path + question, (error, stdout, stderr) => {
    if (error) {
        console.log(`error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
});