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
$advisor = mysqli_real_escape_string($conn, test_input($_POST['advisor']));
$sql = "SELECT distinct CONCAT(s.FirstName, ' ', s.LastName) as sName, m.Name
FROM Student as s, Studies as st, Major as m, Advises as a, Advisor as ad
WHERE s.StudentID = st.StudentID
AND a.StudentID = s.StudentID
AND st.MajorID = m.MajorID
AND a.AdvisorID = '" . $advisor . "'
AND a.AdvisorID = ad.AdvisorID
AND ad.Specialty = m.Name
ORDER BY s.LastName, s.FirstName";

$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
    // output data of each row
	echo "<table border='1'><tr><th>Student Name</th><th>Major</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr><td align='center'>".$row["sName"]."</td><td align='center'>".$row["Name"]."</td></tr>";
    }
	echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);
?>