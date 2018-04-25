<?php
$servername = "db.soic.indiana.edu";
$username = "i308f16_team29";
$password = "my+sql=i308f16_team29";
$dbname = "i308f16_team29";


// Create connection

$conn=mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
else
{echo "Established Database Connection <br>";}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

//escape variables for security sql injection
$studentid = mysqli_real_escape_string($conn, test_input($_POST['student']));
$sql = "SELECT c.Title, sts.Letter
FROM Student_Takes_Section as sts, Section as sec, Student as s, Semester as sem, Course as c
Where sts.SectionID = sec.SectionID
AND s.StudentID = sts.StudentID
AND c.CourseNumber = sec.CourseNumber
AND sem.SemesterCode = sec.SemesterCode
AND sts.StudentID = '" . $studentid . "' 
ORDER BY sem.Start_Date, c.Title";

$hours = "SELECT SUM(c.Credit_Hours) as creditHours, SUM(c.Credit_Hours*sts.GradePoints) as Hours_Earned
FROM Student_Takes_Section as sts, Section as sec, Student as s, Semester as sem, Course as c
Where sts.SectionID = sec.SectionID
AND s.StudentID = sts.StudentID
AND c.CourseNumber = sec.CourseNumber
AND sem.SemesterCode = sec.SemesterCode
AND sts.StudentID = '" . $studentid . "' 
ORDER BY sem.Start_Date, c.Title";

$result = mysqli_query($conn, $sql);
$hoursAttempted = mysqli_query($conn, $hours);
$hoursEarned = mysqli_fetch_assoc($hoursAttempted)["Hours_Earned"];
$hoursAttempted = mysqli_query($conn, $hours);
$creditHours = mysqli_fetch_assoc($hoursAttempted)["creditHours"];
$gpa = $hoursEarned / (int)$creditHours;
if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Course Title</th><th>Letter Grade</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td align='center'>".$row["Title"]."</td><td align='center'>".$row["Letter"]."</td></tr>";
    }
	echo "</table>";
	echo "<table border='1'><tr><th>Hours Attempted</th><th>Grade Points Earned</th><th>GPA</th></tr>";
	echo "<tr><td align='center'>". $creditHours ."</td><td align='center'>". $hoursEarned."</td><td align='center'>". round($gpa, 2) ."</td></tr>";
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>
