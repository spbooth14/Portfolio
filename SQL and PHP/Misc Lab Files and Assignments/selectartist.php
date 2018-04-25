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

$sql = "SELECT AID, CONCAT(fname, ' ', lname), DOB, GENDER 
FROM artist
ORDER BY AID";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Artist ID</th><th>Artist Name</th><th>DOB</th><th>GENDER</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td align='center'>".$row["Title"]."</td><td align='center'>".$row["Name"]."</td><td align='center'>".$row["Publish_Year"]."</td><td align='center'>".$row["Price"]."</td><td align='center'>".$row["Publisher"]."</td><td align='center'>".$row["Format_"]."</td></tr>";
    }
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>