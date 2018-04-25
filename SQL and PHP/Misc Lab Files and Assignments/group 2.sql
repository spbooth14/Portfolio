SELECT c.name, sum(b.price)
FROM trans as t, customer as c, book as b
WHERE c.id = t.id
AND b.bookid = t.bookid
GROUP BY c.name HAVING sum(b.price) > 50;

select concat(e.fname, ' ', e.lname), DATE_FORMAT(e.dob, "%b %D %Y"), (DATEDIFF(CURDATE(), e.DOB))/365
from employee as e
