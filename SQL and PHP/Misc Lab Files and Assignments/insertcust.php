<?php
$servername = "db.soic.indiana.edu";
$username = "i308f16_spbooth";
$password = "my+sql=i308f16_spbooth";
$dbname = "i308f16_spbooth";


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
Else
{ echo "Established Database Connection" ;}



$varcname = $_POST['name'];
$varaddress = $_POST['address'];
$varphone = $_POST['phone'];




$sql = "INSERT INTO customer(name, address, phone)
VALUES ('$varcname', '$varaddress', '$varphone')";


if (mysqli_query($conn, $sql)) {
    echo "<br>New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}


//mysqli_close($conn);
?>


DELETE FROM customer
WHERE name = ""