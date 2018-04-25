DROP TABLE album;
DROP TABLE in_band;
DROP TABLE band;
DROP TABLE artist;

CREATE TABLE artist
(
AID INT AUTO_INCREMENT,
fName varchar(50) NOT NULL,
lName varchar(50), 
DOB DATE,
GENDER VARCHAR(1),
PRIMARY KEY(AID)
)
Engine=innodb;

INSERT INTO artist(fName, lName, DOB,GENDER)
VALUES("Nethery", "Laney", "1995-05-20","F"),
("Kain","Jenkins","1994-12-21","M"),
("Lizzie","Smith","1995-12-11","F"),
("Skyler","Booth","1995-06-13","M"),
("Micah","Nethery", "1990-09-13","M");

CREATE TABLE band
(
BID INT AUTO_INCREMENT, 
Name varchar(100) NOT NULL,
Year_Formed varchar(20)  NOT NULL,
PRIMARY KEY(BID)
)
Engine=innodb;
ALTER TABLE band AUTO_INCREMENT=501;
INSERT INTO band (Name, Year_Formed)
VALUES ("The Beatles","1960"),
("The Rolling Stones","1962"),
("Led Zeppelin","1968"),
("Pink Floyd","1965"),
("Nirvana","1987");


CREATE TABLE in_band
(
AID INT NOT NULL, 
BID INT NOT NULL,
date_in Date NOT NULL,
date_out Date NULL,
FOREIGN KEY(AID) REFERENCES artist(AID),
FOREIGN KEY(BID) REFERENCES band(BID)
)
Engine=innodb;

INSERT INTO in_band (AID,BID, date_in, date_out)
VALUES ("1","502","2001-06-25", NULL),
("2","502","2001-06-25","2013-08-12"),
("4","505","2000-03-15","2012-08-14"),
("3","503","2001-06-25","2004-06-25"),
("1","504","1999-07-23","2006-05-03"),
("3","501","2000-05-30", NULL),
("1","502","1990-01-01","1994-06-24"),
("3","502","2007-06-25",NULL),
("4","503","2010-03-15", NULL);

CREATE TABLE album
(
AlbumID INT AUTO_INCREMENT NOT NULL,
BID INT,
Publish_Year INT, 
Title varchar(25),
Price varchar(25),
Publisher varchar(25),
Format_ varchar(25),
FOREIGN KEY(BID) REFERENCES band(BID),
PRIMARY KEY(AlbumID)
)
Engine=innodb;
ALTER TABLE album AUTO_INCREMENT=1000;

INSERT INTO album(BID, Publish_Year,Title,Price,Publisher,Format_)
VALUES("501","2000","White Blood Cells","9.99","Sympathy Records","CD"),
("501","2000","White Blood Cells","19.99","Lands Records","MP3"),
("501","2003","Alice","12.99","Red Records","CD"),
("501","1999","Barbie Girl","3.99","Sympathy Records","CD"),
("502","2007","A Letter To Elise","19.99","Red Records","CD"),
("502","2005","One","12.99","Sympathy Records","MP3"),
("502","2004","Civil Wars","4.99","Red Records","CD"),
("502","2013","Im Losing You","3.99","Lands Records","CD"),
("503","1999","Eva Braun","13.99","Dot Records","CD"),
("504","2005","Angie","8.99","Lands Records","MP3"),
("505","2006","What does the Fox say","6.99","Sympathy Records","CD");




SELECT CONCAT(a.fname, ' ', a.lname) as "Names of Rolling Stones Members in 2001"
FROM artist as a, in_band as IB, band as b
WHERE b.bid = IB.bid
	AND a.aid = IB.aid
	AND b.name = "The Rolling Stones"
	AND (DATE_FORMAT(IB.date_in, '%Y') = '2001' or DATE_FORMAT(IB.date_out, '%Y') = '2001');

SELECT DISTINCT b.name AS "Band Name", CONCAT(a.fname, ' ', a.lname) AS "Full Name"
FROM artist as a, album as al, in_band as IB, band as b
WHERE al.bid = b.bid
	AND b.bid = IB.bid
	AND a.aid = IB.aid
	AND al.title = "A Letter To Elise"
	AND IB.date_in <= al.publish_year <= al.publish_year;

SELECT DISTINCT CONCAT(a.fname, ' ', a.lname) AS "Full Name", a.GENDER, DATE_FORMAT(a.DOB, '%b' ' ' '%d' ' ' '%Y') as DOB, b.name as "Band Name"
FROM artist as a, in_band as IB, band as b
WHERE b.bid = IB.bid
	AND a.aid = IB.aid
	AND IB.date_out IS NULL
	AND (a.GENDER = 'F' OR ((DATEDIFF(CURDATE(), a.DOB) >= '7665') AND a.GENDER != 'F'))
GROUP BY b.name;

	