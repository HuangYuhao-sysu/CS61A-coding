.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number FROM students AS a, students AS b WHERE a.date=b.date AND a.color=b.color AND a.pet=b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT SELECT a.seven FROM students as a, checkboxes AS b WHERE a.number=7 AND b.'7'='True' AND a.time=b.time;

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) AS count FROM fa17students GROUP BY number ORDER BY count DESC LIMIT 10;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) AS count FROM fa17students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) AS count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) AS count FROM fa17students WHERE pet='dog' GROUP BY pet LIMIT 10;


CREATE TABLE sp18alldogs AS
  SELECT pet, COUNT(*) AS count FROM fa17students WHERE pet LIKE 'dog' GROUP BY pet LIMIT 10;


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) AS count FROM students WHERE seven='7' GROUP BY denero LIMIT 5;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT SELECT smallest, COUNT(*) AS count FROM fa17students GROUP BY smallest ORDER BY smallest LIMIT 10;
