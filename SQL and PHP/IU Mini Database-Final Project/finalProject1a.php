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
$sectionid= mysqli_real_escape_string($conn, test_input($_POST['sectionid']));
$sql = "SELECT CONCAT(s.Lastname, ', ', s.FirstName) as Student_Name
FROM Student_Takes_Section as sts, Student as s
WHERE sts.StudentID = s.StudentID
AND sectionID = '" . $sectionid . "' 
ORDER BY s.Lastname, s.FirstName";

$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Students in Section " . $sectionid . "</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td align='center'>".$row["Student_Name"]."</td></tr>";
    }
	echo "</table>";
} else {
    echo "This section is empty";
}

mysqli_close($conn);
?>