<!doctype html>
<html>
<body>
<h1 align='center'>Group 29 Final Project</h1>

<h3>1a. Produce a roster for a *specified section* sorted by student’s last name, first name</h3>
<form action="finalProject1a.php" method="POST">
Please select a section to get its roster: <select name='sectionid'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct SectionID FROM Section ORDER BY SectionID");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['SectionID'];
                  $name = $row['SectionID']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="1a">
	</form>

<h3>2a. Produce a list of rooms that are equipped with *some feature*.</h3>
<form action="finalProject2a.php" method="POST">
Please select a feature: <select name='feature'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct Feature FROM Room_Features ORDER BY Feature");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['Feature'];
                  $name = $row['Feature']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="2a">
	</form>
<h3>3b. Produce a list of faculty who have never taught a specified course.</h3>
<form action="finalProject3b.php" method="POST">
Please select a course to get a list of faculty who haven't taught it: <select name='course'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct Title, CourseNumber FROM Course ORDER BY Title");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['CourseNumber'];
                  $name = $row['Title']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="3b">
	</form>
	
<h3>5b. Produce a chronological list of all courses taken by a *specified student*. Show grades earned. Include overall hours taken and GPA at the end.</h3>

<form action="finalProject5b.php" method="POST">
Please select a student: <select name='student'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct StudentID, CONCAT(FirstName, ' ', LastName) as Name FROM Student ORDER BY Name");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['StudentID'];
                  $name = $row['Name']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="5b">
	</form>
	
<h3>6c. Produce a list of students and faculty who were in a *particular building* at a *particular time*, during a *particular semester*. Also include in the list faculty and advisors who have offices in that building.</h3>
<form action="finalProject6c.php" method="POST">
Please select a bulding: <select name='building'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct Name, BuildingID FROM Building ORDER BY Name");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['BuildingID'];
                  $name = $row['Name']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
Please select a time: <select name ='time'>
<option value = "08:00:00">8:00 AM</option>
<option value = "08:15:00">8:15 AM</option>
<option value = "08:30:00">8:30 AM</option>
<option value = "08:45:00">8:45 AM</option>
<option value = "09:00:00">9:00 AM</option>
<option value = "09:15:00">9:15 AM</option>
<option value = "09:30:00">9:30 AM</option>
<option value = "09:45:00">9:45 AM</option>
<option value = "10:00:00">10:00 AM</option>
<option value = "10:15:00">10:15 AM</option>
<option value = "10:30:00">10:30 AM</option>
<option value = "10:45:00">10:45 AM</option>
<option value = "11:00:00">11:00 AM</option>
<option value = "11:15:00">11:15 AM</option>
<option value = "11:30:00">11:30 AM</option>
<option value = "11:45:00">11:45 AM</option>
<option value = "12:00:00">12:00 PM</option>
<option value = "12:15:00">12:15 PM</option>
<option value = "12:30:00">12:30 PM</option>
<option value = "12:45:00">12:45 PM</option>
<option value = "13:00:00">1:00 PM</option>
<option value = "13:15:00">1:15 PM</option>
<option value = "13:30:00">1:30 PM</option>
<option value = "13:45:00">1:45 PM</option>
<option value = "14:00:00">2:00 PM</option>
<option value = "14:15:00">2:15 PM</option>
<option value = "14:30:00">2:30 PM</option>
<option value = "14:45:00">2:45 PM</option>
<option value = "15:00:00">3:00 PM</option>
<option value = "15:15:00">3:15 PM</option>
<option value = "15:30:00">3:30 PM</option>
<option value = "15:45:00">3:45 PM</option>
<option value = "16:00:00">4:00 PM</option>
<option value = "16:15:00">4:15 PM</option>
<option value = "16:30:00">4:30 PM</option>
<option value = "16:45:00">4:45 PM</option>
<option value = "17:00:00">5:00 PM</option>
<option value = "17:15:00">5:15 PM</option>
<option value = "17:30:00">5:30 PM</option>
<option value = "17:45:00">5:45 PM</option>
<option value = "18:00:00">6:00 PM</option>
<option value = "18:15:00">6:15 PM</option>
<option value = "18:30:00">6:30 PM</option>
<option value = "18:45:00">6:45 PM</option>
<option value = "19:00:00">7:00 PM</option>
<option value = "19:15:00">7:15 PM</option>
<option value = "19:30:00">7:30 PM</option>
<option value = "19:45:00">7:45 PM</option>
<option value = "20:00:00">8:00 PM</option>
<option value = "20:15:00">8:15 PM</option>
<option value = "20:30:00">8:30 PM</option>
<option value = "20:45:00">8:45 PM</option>
<option value = "21:00:00">9:00 PM</option>
<option value = "21:15:00">9:15 PM</option>
<option value = "21:30:00">9:30 PM</option>
<option value = "21:45:00">9:45 PM</option>
<option value = "22:00:00">10:00 PM</option>
<option value = "22:15:00">10:15 PM</option>
<option value = "22:30:00">10:30 PM</option>
<option value = "22:45:00">10:45 PM</option>
</select>
<br />
Please select a semester: <select name='semester'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct SemesterCode FROM Semester ORDER BY SemesterCode");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['SemesterCode'];
                  $name = $row['SemesterCode']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="6c">
	</form>


<h3>7a. Produce an alphabetical list of students with their majors who are advised by a *specified advisor*</h3>

<form action="finalProject7a.php" method="POST">
Please select an advisor: <select name='advisor'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct AdvisorID, CONCAT(FirstName, ' ', LastName) as Name FROM Advisor ORDER BY Name");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['AdvisorID'];
                  $name = $row['Name']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="7a">
	</form>
<h3>Additional Query 1: Select a *Building* to get its address and how many classrooms it has as well as how many offices.</h3>
<form action="finalProjectAdditional1.php" method="POST">
Please select a Building: <select name='building'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct BuildingID, Name FROM Building ORDER BY Name");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['BuildingID'];
                  $name = $row['Name']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="Additional Query 1">
	</form>
<h3>Additional Query 2: Select a *Department* to how many majors it offers and how many faculty work for it.</h3>
<form action="finalProjectAdditional2.php" method="POST">
Please select a Department: <select name='department'>
<?php
$conn = mysqli_connect("db.soic.indiana.edu","i308f16_team29","my+sql=i308f16_team29","i308f16_team29");
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
    $result = mysqli_query($conn,"SELECT distinct DepartmentID, Name FROM Department ORDER BY Name");
    while ($row = mysqli_fetch_assoc($result)) {
                  unset($id, $name);
                  $id = $row['DepartmentID'];
                  $name = $row['Name']; 
                  echo '<option value="'.$id.'">'.$name.'</option>';
}
?> 
    </select>
	<br />
	<input type="submit" value="Additional Query 2">
	</form>
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
</body>
</html>