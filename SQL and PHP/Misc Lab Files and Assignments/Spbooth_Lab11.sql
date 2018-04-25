SELECT m.item_name, m.price, sum(od.qty) as quantity
FROM menu as m, order_detail as od
WHERE m.menuid = od.menuid
GROUP BY m.item_name
ORDER BY quantity DESC, m.menuid LIMIT 10;

SELECT m.item_name, m.price, sum(od.qty) as quantity, sum(od.qty)*m.price as tsales
FROM menu as m, order_detail as od
WHERE m.menuid = od.menuid
GROUP BY m.item_name
ORDER BY quantity DESC, m.menuid LIMIT 10;

SELECT m.item_name, m.price, sum(od.qty) as quantity, sum(od.qty)*m.price as tsales
FROM menu as m, order_detail as od
WHERE m.menuid = od.menuid
GROUP BY m.item_name
ORDER BY tsales DESC LIMIT 10;

SELECT DATE_FORMAT(o.order_date, "%a") as day, sum(od.qty) as quantity
FROM order_main as o, order_detail as od, menu as m
WHERE o.orderid = od.orderid
AND od.menuid = m.menuid
AND m.item_name = 'menuitem7'
GROUP BY day
ORDER BY quantity DESC;

SELECT DATE_FORMAT(o.order_date, "%Y") as year, sum(od.qty) as quantity, sum(od.qty * m.price) as tsales
FROM order_main as o, order_detail as od, menu as m
WHERE o.orderid = od.orderid
AND od.menuid = m.menuid
AND m.item_name = 'menuitem7'
AND DATE_FORMAT(o.order_date, "%a") = "Sun"
GROUP BY year
ORDER BY year DESC;