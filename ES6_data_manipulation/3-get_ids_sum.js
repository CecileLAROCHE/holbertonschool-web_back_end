export default function getStudentIdsSum(studentList) {

  if (Array.isArray(studentList)) {
    return studentList.reduce((accumulateur, element ) => accumulateur + element.id, 0);
 }
  
  else {
    return [];
  }
}