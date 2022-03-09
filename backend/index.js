const express = require('express')
const bodyParser = require('body-parser');
const cors = require('cors')
const { exec } = require("child_process");

const app = express()
const port = 5667
const path = process.platform === 'win32' ? "python3 .\\python_scripts\\qa.py " : "python3 ./python_scripts/qa.py "

app.use(cors({
  origin: 'http://localhost:8080'
}))

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies

app.get('/', (req, res) => {
  res.send('Nothing here !')
})

app.post('/question', (req, res) => {
  let question = '"' + req.body.question + '"'
  console.log('Request for : ' + question)
  exec(path + question, (error, stdout, stderr) => {
    if (error) {
      console.log(`error: ${error.message}`);
      res.sendStatus(500)
      return;
    }
    else if (stderr) {
      console.log(`stderr: ${stderr}`);
      res.sendStatus(500)
      return;
    } else {
      res.send(stdout)
    }
  })
})

app.listen(port, () => {
  console.log(`Backend app listening at http://localhost:${port}`)
})
