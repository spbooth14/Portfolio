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
$buildingid = mysqli_real_escape_string($conn, test_input($_POST['building']));
$atime = mysqli_real_escape_string($conn, test_input($_POST['time']));
$semestercode = mysqli_real_escape_string($conn, test_input($_POST['semester']));
$student = "SELECT CONCAT(s.LastName, ', ', s.FirstName)
FROM Student as s, Semester as sem, Building as b, Student_Takes_Section as sts, Section as sec, Room as r
WHERE s.StudentID = sts.StudentID
AND sts.SectionID = sec.SectionID
AND sec.SemesterCode = sem.SemesterCode
AND sec.RoomID = r.RoomID
AND r.BuildingID = b.BuildingID
AND b.BuildingID = '" . $buildingid . "'
AND sem.SemesterCode = '" . $semestercode . "'
AND sec.StartTime <= '" . $atime . "'
AND sec.EndTime >= '" . $atime . "'
ORDER BY s.LastName";

$faculty = "SELECT CONCAT(f.LastName, ', ', f.FirstName)
FROM Faculty as f, Semester as sem, Building as b, Section as sec, Room as r
WHERE f.FacultyID = sec.FacultyID
AND sec.SemesterCode = sem.SemesterCode
AND sec.RoomID = r.RoomID
AND r.BuildingID = b.BuildingID
AND b.BuildingID = '" . $buildingid . "'
AND sem.SemesterCode = '" . $semestercode . "'
AND sec.StartTime <= '" . $atime . "'
AND sec.EndTime >= '" . $atime . "'
ORDER BY f.LastName";

$facoffices = "SELECT CONCAT(f.LastName, ', ', f.FirstName)
FROM Faculty as f, Building as b, Room as r
WHERE f.RoomID = r.RoomID
AND b.BuildingID = r.BuildingID
AND r.Type = 'Office'
AND b.BuildingID = '" . $buildingid . "'
ORDER BY f.LastName";

$advoffices = "Select CONCAT(a.LastName, ', ', a.FirstName)
FROM Advisor as a, Building as b, Room as r
WHERE a.RoomID = r.RoomID
AND b.BuildingID = r.BuildingID
AND r.Type = 'Office'
AND b.BuildingID = '" . $buildingid . "'
ORDER BY a.LastName";

$studentsresult = mysqli_query($conn, $student);
$facultyResult = mysqli_query($conn, $faculty);
$facofficesResult = mysqli_query($conn, $facoffices);
$advofficesResult = mysqli_query($conn, $advoffices);

if (mysqli_num_rows($studentsresult) > 0) {
    // output data of each row
	echo "<h2>Students and Faculty in this bulding<h2>";
	echo "<table border='1'><tr><th>Name</th><th>Position</th></tr>";
    while($row = mysqli_fetch_assoc($studentsresult)) {
	    echo "<tr><td align='center'>".$row["CONCAT(s.LastName, ', ', s.FirstName)"]."</td><td align='center'>Student</td></tr>";
    }
	while($row = mysqli_fetch_assoc($facultyResult)) {
	    echo "<tr><td align='center'>".$row["CONCAT(f.LastName, ', ', f.FirstName)"]."</td><td align='center'>Faculty</td></tr>";
    }
	echo "</table>";
} else {
    echo "No students or faculty were in this building at the specified time";
}
if (mysqli_num_rows($facofficesResult) > 0) {
    // output data of each row
	echo "<h2>Offices in this bulding</h2>";
	echo "<table border='1'><tr><th>Name</th><th>Type</th></tr>";
    while($row = mysqli_fetch_assoc($facofficesResult)) {
	    echo "<tr><td align='center'>".$row["CONCAT(f.LastName, ', ', f.FirstName)"]."</td><td align='center'>Faculty</td></tr>";
    }
	while($row = mysqli_fetch_assoc($advofficesResult)) {
	    echo "<tr><td align='center'>".$row["CONCAT(a.LastName, ', ', a.FirstName)"]."</td><td align='center'>Advisor</td></tr>";
    }
	echo "</table>";
} else {
    echo "No offices are in this building";
}

mysqli_close($conn);
?>