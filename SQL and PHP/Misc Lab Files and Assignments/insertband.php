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


//escape variables for security sql injection
$sanbname = mysqli_real_escape_string($conn, $_POST['bandname']);
$sanyearf = mysqli_real_escape_string($conn, $_POST['yearformed']);

//Insert query to insert form data into the band table
$sql="INSERT INTO band(Name, Year_Formed)
VALUES('$sanbname','$sanyearf')";
//check for error on insert
if (!mysqli_query($conn,$sql))
{ die('Error: ' . mysqli_error($conn)); }

echo "1 record added";
mysqli_close($conn);

?>
 