-- 3-list_tables.sql

-- ----------------------------------------------------------
-- SQL Script: 3-list_tables.sql
-- Description: This script lists all the tables of a given
--              database on the MySQL server.
-- Author: [Your Name]
-- Date: [Current Date]
-- ----------------------------------------------------------

-- Parameter: The database name will be passed as an argument
-- Example Usage: cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql

-- Fetch and display table names
SHOW TABLES FROM mysql;
