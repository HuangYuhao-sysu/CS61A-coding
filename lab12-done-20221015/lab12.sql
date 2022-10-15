.read fa17data.sql
.read sp18data.sql

-- Q2
"CREATE TABLE obedience AS
  SELECT seven, denero FROM students;

-- Q3
CREATE TABLE smallest_int AS
  SELECT smallest FROM students WHERE smallest > 15 ORDER BY smallest;

-- Q4
CREATE TABLE matchmaker AS
  SELECT SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b WHERE a.pet = b.pet AND a.song = b.song AND a.time<>b.time LIMIT 10;
