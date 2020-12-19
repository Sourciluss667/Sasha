const { exec } = require("child_process");

var question = '"Quand est né Vin Diesel ?"'

exec("python .\\python_scripts\\qa.py " + question, (error, stdout, stderr) => {
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