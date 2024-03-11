
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const port = 8080;

app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));


app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Addition API
app.post('/application/add', (req, res) => {
    console.log(req.body);
    const { num1, num2 } = req.body;
    const result = parseInt(num1) + parseInt(num2);
    res.json({ result });
});

// Subtraction API
app.post('/application/subtract', (req, res) => {
    console.log(req.body);
    const { num1, num2 } = req.body;
    const result = parseInt(num1) - parseInt(num2);
    res.json({ result });
  });