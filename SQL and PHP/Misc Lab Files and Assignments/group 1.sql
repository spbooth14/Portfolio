SELECT m.item_name, SUM(OD.qty) as quantity, SUM(m.price * OD.qty) as total_price
FROM menu as m, order_detail as OD, order_main as OM
WHERE OM.order_date = "2003-11-08"
	AND m.menuid = OD.menuid
	AND OD.orderid = OM.orderid
GROUP BY m.item_name;


SELECT concat(e.fname, ' ', e.lname) as full_name, ws.role
from employee as e, works_shift as ws, order_main as om
WHERE e.empid = ws.empid
	AND om.orderid = 3902
	AND om.order_date = ws.wdate
	AND om.time_in between ws.time_in and ws.time_out;
	
