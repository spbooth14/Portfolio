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
$sql = "SELECT CONCAT(Address, ' ', City, ' ', State, ' ', ZIP) as Full_Address 
FROM Building
Where BuildingID = '" . $buildingid . "'";


$offices = "SELECT COUNT(RoomID)
FROM Room
Where BuildingID = '" . $buildingid . "'
AND Type = 'Office'";

$classrooms = "SELECT COUNT(RoomID)
FROM Room
Where BuildingID = '" . $buildingid . "'
AND Type = 'Classroom'";

$result = mysqli_query($conn, $sql);
$officeResult = mysqli_query($conn, $offices);
$classResult = mysqli_query($conn, $classrooms);
$fullAddress = mysqli_fetch_assoc($result)["Full_Address"];
$officeNumber = mysqli_fetch_assoc($officeResult)["COUNT(RoomID)"];
$classNumber = mysqli_fetch_assoc($classResult)["COUNT(RoomID)"];

if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Building Address</th><th>Number of Classrooms</th><th>Number of Offices</th></tr>";
    echo "<tr><td align='center'>". $fullAddress ."</td><td align='center'>". $classNumber ."</td><td align='center'>". $officeNumber ."</td></tr>";
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>
