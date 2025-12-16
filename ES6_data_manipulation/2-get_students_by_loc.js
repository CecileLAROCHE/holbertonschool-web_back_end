export default function getStudentsByLocation(studentList, location) {
  if (Array.isArray(studentList)) {
    const mapped = studentList.filter((element) => element.location === location);
    return mapped;
  } else {
    return [];
  }
}