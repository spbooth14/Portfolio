DROP TABLE trans;
DROP TABLE book;
DROP TABLE customer;


CREATE TABLE customer
(
id INT AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
address VARCHAR(256) NOT NULL,
phone VARCHAR(15) NOT NULL,
PRIMARY KEY (id)
)
ENGINE=innodb;

CREATE TABLE book
(
bookid INT AUTO_INCREMENT,
title VARCHAR(256) NOT NULL,
price DECIMAL(4,2) NOT NULL,
PRIMARY KEY (bookid)
)
Engine=innodb;



CREATE TABLE trans
(
id INT,
bookid INT,
tdate DATE,
FOREIGN KEY (id) REFERENCES customer(id),
FOREIGN KEY (bookid) REFERENCES book(bookid)
)
Engine=innodb;

ALTER TABLE customer AUTO_INCREMENT=500;
ALTER TABLE book AUTO_INCREMENT=1001;

INSERT INTO customer (name, address,  phone)
VALUES ('Matt', '420 Baker Street', '800-555-4242'),
	   ('Jenny', '12 Tutone Ave', '555-867-5309'),
	   ('Sean', '1600 N Penn Dr', '555-555-1550');

INSERT INTO book (title, price)
VALUES ('The Code Book', '14.00'),
	   ('Core Web Programming', '49.95'),
	   ('The Hacker Ethic', '19.95');

INSERT INTO trans (id, bookid, tdate)
VALUES ('500', '1001', '2003-09-13'),
	   ('501', '1002', '2003-09-17'),
	   ('501', '1002', '2003-09-26'),
	   ('502', '1003', '2003-10-01'),
	   ('501', '1001', '2003-10-12'),
	   ('502', '1002', '2003-10-25');

Select DISTINCT c.name, b.title
From book as b, customer as c, trans as t 
Where c.id = t.id
	AND b.bookid = t.bookid
	AND t.tdate BETWEEN '2003-09-01' AND '2003-09-30';

SELECT c.name, b.title, SUM(b.price)
FROM customer AS c, trans AS t, book AS b
WHERE c.id = t.id
     AND t.bookid = b.bookid
GROUP BY c.name, b.title;
	   
UPDATE customer
SET phone =  '555-555-3333'
WHERE name = 'Sean';

ALTER TABLE book
ADD booktype VARCHAR(50);

UPDATE book
SET booktype = 'paperback'
WHERE price < '20.00';

UPDATE book
SET booktype = 'hardback'
WHERE price > '20.00';


