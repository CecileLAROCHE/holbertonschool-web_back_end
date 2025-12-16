export default function updateStudentGradeByCity(studentList, city, newGrades) {
  if (Array.isArray(studentList)) {
    return studentList
      .filter(student => student.location === city)
      .map(student => {
        const match = newGrades.find(
          grade => grade.studentId === student.id
        );

        return {
          ...student,
          grade: match ? match.grade : 'N/A',
        };
      });
  } else {
    return [];
  }
}
