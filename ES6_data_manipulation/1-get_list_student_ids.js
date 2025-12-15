export default function getListStudentIds(studentList) {
  if (Array.isArray(studentList)) {
    const mapped = studentList.map((element) => element.id);
    return mapped;
  } else {
    return [];
  }
}