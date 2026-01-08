import fs from 'fs';

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) reject(err);

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1); // ignore header
      const result = {};
      for (const line of students) {
        const parts = line.split(',');
        const firstname = parts[0].trim();
        const field = parts[3].trim();
        if (!result[field]) result[field] = [];
        result[field].push(firstname);
      }
      resolve(result);
    });
  });
}

export default readDatabase;
