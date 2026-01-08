const express = require('express');
const fs = require('fs');
const countStudents = require('./3-read_file_async');
const database = process.argv[2];
const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  let text = 'This is the list of our students\n';

  countStudents(database)
    .then((data) => {
      text += data;
      res.send(text);
    })
    .catch(() => {
      text += 'Cannot load the database';
      res.send(text);
    });
});


app.listen(port, () => {
  console.log(`App listening on ${port}`);
});

module.exports = app;