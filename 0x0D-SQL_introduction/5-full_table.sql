-- 5-full_table.sql

-- This a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server
SELECT CONCAT('Table   Create Table                                                                          ', `Create Table`) AS Full_Description
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
