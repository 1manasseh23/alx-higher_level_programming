-- 2-remove_database.sql

-- ----------------------------------------------------------
-- SQL Script: 2-remove_database.sql
-- Description: This script deletes the database hbtn_0c_0 if it
--              exists on the MySQL server.
-- Author: [Your Name]
-- Date: [Current Date]
-- ----------------------------------------------------------

-- Attempt to drop the database hbtn_0c_0
DROP DATABASE IF EXISTS hbtn_0c_0;

-- Output a message indicating the operation is complete
SELECT 'Database hbtn_0c_0 deleted or not found.' AS 'Status';
