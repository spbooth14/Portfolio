<!doctype html>
<html>
<body>
<h2>Album Table</h2>
<h3>Insert a new Album</h3>
<form action="albuminsert.php" method="POST">
Title: <input type="text" name="title" maxlength=500 size=50 required><br><br>
Band: <select name='bid'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct BID, Name FROM band ORDER BY Name");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['BID'];
                  $name = $row['Name']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
<br />
</br>
Published Year: <input type="number" name="pyear" min="1900" max="2016" required><br><br>
Publisher: <input type="text" name="pub" maxlength=500 size=50 required><br><br>
Format: <select name="format">
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct Format_ FROM album");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['Format_'];
                  $name = $row['Format_']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
</select>
<br />
<br />
Price: $<input type="number" name="price" min="0" max="99999.99" step="0.01" required> Between $0 and $99,999.99<br><br>
<input type="submit" value="Insert Album">
</form>
<h3>Select all Albums</h3>
<form action="albumselect.php" method="post">
<input type="submit" name="submit" value="Select Album table">
</form>
</body>
</html>

