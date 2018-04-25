SELECT CONCAT(e.fname, ' ', e.lname) AS  "Full Name", COUNT(*) AS "Number of Shifts Worked in 2011"
FROM employee as e, works_shift as ws
WHERE e.empid = ws.empid
AND DATE_FORMAT(ws.wdate, '%Y') = 2011
GROUP BY e.empid
HAVING COUNT(*) > 5;

SELECT CONCAT(e.fname, ' ', e.lname) AS  "Full Name", COUNT(*) AS "Number of Shifts Worked in 2011"
FROM employee as e, works_shift as ws, shift as s
WHERE e.empid = ws.empid
AND ws.shiftid = s.shiftid
AND s.period = "L"
GROUP BY e.empid
ORDER BY COUNT(*) DESC;

SELECT CONCAT(e.fname, ' ', e.lname) AS  "Full Name", COUNT(*) AS "Number of Shifts Worked in 2011"
FROM employee as e, works_shift as ws, shift as s
WHERE e.empid = ws.empid
AND ws.shiftid = s.shiftid
AND s.period = "L"
AND (s.dayofweek = "sa" or s.dayofweek = "su")
GROUP BY e.empid
ORDER BY COUNT(*) DESC;

SELECT m.item_name as name, SUM(od.qty) as quantity, SUM(od.qty * m.price) as total
FROM order_detail as od, menu as m, order_main as om
WHERE  om.order_date = '2012-11-16'
AND od.orderid = om.orderid
AND m.menuid = od.menuid
GROUP BY m.item_name with ROLLUP;