CREATE TABLE incidents
(
id INT AUTO_INCREMENT,
url VARCHAR(256),
title VARCHAR(256),
author varchar(256),
postdate varchar(256),
description varchar(1000),
PRIMARY KEY (id)
)
Engine=innodb;
