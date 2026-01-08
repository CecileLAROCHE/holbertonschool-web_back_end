import { readDatabase } from '../utils.js';

export default class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2]; // récupère le fichier au lancement
    readDatabase(database)
      .then((studentsObj) => {
        let text = 'This is the list of our students\n';
        const sortedFields = Object.keys(studentsObj).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
        for (const field of sortedFields) {
          text += `Number of students in ${field}: ${studentsObj[field].length}. List: ${studentsObj[field].join(', ')}\n`;
        }
        res.status(200).type('text/plain').send(text.trim());
      })
      .catch(() => {
        res.status(500).type('text/plain').send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const major = req.params.major;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).type('text/plain').send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((studentsObj) => {
        if (!studentsObj[major]) studentsObj[major] = [];
        res.status(200).type('text/plain').send(`List: ${studentsObj[major].join(', ')}`);
      })
      .catch(() => {
        res.status(500).type('text/plain').send('Cannot load the database');
      });
  }
}
