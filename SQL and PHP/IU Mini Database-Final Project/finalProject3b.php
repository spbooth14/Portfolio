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
$course= mysqli_real_escape_string($conn, test_input($_POST['course']));
$sql = "SELECT CONCAT(f.FirstName, ' ', f.LastName)
FROM Faculty as f
WHERE f.FacultyID NOT IN
(SELECT f.FacultyID
FROM Section as s, Faculty as f, Course as c
WHERE f.FacultyID = s.FacultyID
AND s.CourseNumber = c.CourseNumber
AND c.CourseNumber = '" . $course . "') 
ORDER BY f.LastName";

$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Instructors who haven't taught " . $course . " </th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td align='center'>".$row["CONCAT(f.FirstName, ' ', f.LastName)"]."</td></tr>";
    }
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>