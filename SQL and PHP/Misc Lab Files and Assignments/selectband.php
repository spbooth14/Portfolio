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

$sql = "SELECT BID, Name, Year_Formed 
FROM band
ORDER BY Year_Formed DESC";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'>
<tr>
<th>Band Name</th>
	<th>Year Formed</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td>". $row["Name"]. "</td><td>" . $row["Year_Formed"]. "</td></tr>";
    }
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>