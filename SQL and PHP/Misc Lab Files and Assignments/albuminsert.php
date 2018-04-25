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
$atitle= mysqli_real_escape_string($conn, test_input($_POST['title']));
$aband = mysqli_real_escape_string($conn, test_input($_POST['bid']));
$ayear = mysqli_real_escape_string($conn, test_input($_POST['pyear']));
$apublisher = mysqli_real_escape_string($conn, test_input($_POST['pub']));
$aformat = mysqli_real_escape_string($conn, test_input($_POST['format']));
$aprice = mysqli_real_escape_string($conn, test_input($_POST['price']));

//Insert query to insert form data into the band table
$sql="INSERT INTO album(BID, Publish_Year,Title,Price,Publisher,Format_)
VALUES('$aband','$ayear','$atitle','$aprice','$apublisher','$aformat')";
//check for error on insert
if (!mysqli_query($conn,$sql))
{ die('Error: ' . mysqli_error($conn)); }

echo "1 record added";
mysqli_close($conn);

?>