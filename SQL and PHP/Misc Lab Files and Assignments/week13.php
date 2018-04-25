<?php
// Create connection
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_teamNN","my+sql=i308f16_teamNN","i308f16_teamNN");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
$roles = mysqli_real_escape_string($conn, $_POST['roles']);
$sql = "SELECT * from works_shift where role = '$roles'";
$result = mysqli_query($conn, $sql);
$num_rows = mysqli_num_rows($result);
if ($result->num_rows > 0) {
    echo "<table><tr><th>Shift ID</th><th>Employee ID</th><th>wdate</th><th>time_in</th><th>time_out</th><th>role</th></tr>";
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>".$row["shiftid"]."</td><td>".$row["empid"]."</td><td>".$row["wdate"]."</td>
		      <td>".$row["time_in"]."</td><td>".$row["time_out"]."</td><td>".$row["role"]."</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 results";
}
echo "$num_rows Rows\n";
mysqli_close($conn);
?>
