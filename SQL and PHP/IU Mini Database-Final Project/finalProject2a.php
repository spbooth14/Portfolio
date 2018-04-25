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
$feature= mysqli_real_escape_string($conn, test_input($_POST['feature']));
$sql = "SELECT RoomID
FROM Room_Features
WHERE Feature = '" . $feature . "' 
ORDER BY RoomID";

$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Rooms that have a " . $feature . "</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td align='center'>".$row["RoomID"]."</td></tr>";
    }
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>