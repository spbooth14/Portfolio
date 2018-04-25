SELECT b.name as "Band's without females"
FROM band as b
WHERE b.name NOT IN
(SELECT b.name
FROM in_band as IB, artist as a
WHERE b.bid = IB.bid
AND a.aid = IB.aid
AND a.gender = 'F');



SELECT CONCAT(a.fname, ' ', a.lname) as 'Artist Name', timestampdiff(YEAR, a.dob, CURRENT_DATE()) as 'Age', b.name as 'Band Name'
FROM band as b, artist AS a, in_band AS IB
WHERE a.aid = IB.aid
AND b.bid = IB.bid
AND a.fname NOT IN
(SELECT a.fname
FROM artist
WHERE a.gender = 'M') 
ORDER BY b.name, CONCAT(a.fname, ' ', a.lname);



(SELECT CONCAT(a.fname, ' ', a.lname) as 'Artist Name', b.name as 'Band Name', timestampdiff(YEAR, IB.date_in, CURRENT_DATE()) as 'Time in Band'
FROM band as b, artist AS a, in_band AS IB
WHERE IB.date_out IS NULL
AND a.aid = IB.aid
AND b.bid = IB.bid
GROUP BY a.fname, b.name)
UNION ALL
(SELECT CONCAT(a.fname, ' ', a.lname) as 'Artist Name', b.name as 'Band Name', timestampdiff(YEAR, IB.date_in, IB.date_out) as 'Time in Band'
FROM band as b, artist AS a, in_band AS IB
WHERE IB.date_out IS NOT NULL
AND a.aid = IB.aid
AND b.bid = IB.bid
GROUP BY a.fname, b.name);