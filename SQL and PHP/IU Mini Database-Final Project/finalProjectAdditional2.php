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
$departmentid = mysqli_real_escape_string($conn, test_input($_POST['department']));
$sql = "SELECT COUNT(MajorID) 
FROM Major
Where DepartmentID = '" . $departmentid . "'";


$professors = "SELECT COUNT(FacultyID)
FROM Faculty
Where DepartmentID = '" . $departmentid . "'";


$result = mysqli_query($conn, $sql);
$profResult = mysqli_query($conn, $professors);
$majorNumber = mysqli_fetch_assoc($result)["COUNT(MajorID)"];
$profNumber = mysqli_fetch_assoc($profResult)["COUNT(FacultyID)"];

if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Number of Majors Offered</th><th>Number of Faculty Members</th></tr>";
    echo "<tr><td align='center'>". $majorNumber ."</td><td align='center'>". $profNumber ."</td></tr>";
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>