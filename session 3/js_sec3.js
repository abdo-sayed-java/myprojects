alert("Task: Revision the code");

let studentName = "Abdo";
let studentScore = 75;

if (studentScore >= 90) {
    studentGrade = "A";
}else if (studentScore >= 80 && studentScore <= 89) {
    studentGrade = "B";
}
else if (studentScore >= 70 && studentScore <= 79) {
    studentGrade = "C";
}
else if (studentScore >= 60 && studentScore <= 69) {
    studentGrade = "D";
}
else {
    studentGrade = "Fail";
}

console.log("studentName: " + studentName + ",\n" + "studentScore: " + studentScore + ",\n" + "studentGrade: " + studentGrade);

// Bonus1
function checkPass(score) {
    if (score >= 60) {
        return "Pass";
    } else {
        return "Fail";
    }
}
console.log("checkPass for "+ studentName +" : " + checkPass(studentScore));

// Bonus2
let students = [
    { name: "Abdo", score: 75 },
    { name: "Ahmed", score: 90 },
    { name: "Ali", score: 60 }
];

for (let i = 0; i < students.length; i++) {
    console.log(students[i].name + " scored " + students[i].score + " and received a grade of " + checkPass(students[i].score));
}
