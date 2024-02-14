-- 1-create_database_if_missing.sql

-- ----------------------------------------------------------
-- SQL Script: 1-create_database_if_missing.sql
-- Description: This script creates the database hbtn_0c_0 if it
--              does not already exist on the MySQL server.
-- Author: [Your Name]
-- Date: [Current Date]
-- ----------------------------------------------------------

-- Attempt to create the database hbtn_0c_0
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Output a message indicating the operation is complete
SELECT 'Database hbtn_0c_0 created or already exists.' AS 'Status';
