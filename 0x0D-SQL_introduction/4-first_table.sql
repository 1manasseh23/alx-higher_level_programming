-- 4-first_table.sql

-- ----------------------------------------------------------
-- SQL Script: 4-first_table.sql
-- Description: This script creates a table named first_table
--              in the specified database on the MySQL server.
-- Author: [Your Name]
-- Date: [Current Date]
-- ----------------------------------------------------------

-- Parameter: The database name will be passed as an argument
-- Example Usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Check if the table exists before creating
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
