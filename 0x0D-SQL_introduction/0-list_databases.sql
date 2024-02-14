-- ----------------------------------------------------------
-- SQL Script: list_databases.sql
-- Description: This script retrieves a list of all databases 
--              available on the MySQL server.
-- Author: [Your Name]
-- Date: [Current Date]
-- ----------------------------------------------------------

-- Statement: SHOW DATABASES;
-- Purpose: Retrieves a list of all databases on the MySQL server.

-- Usage Instructions:
--   1. Save this script as list_databases.sql.
--   2. Run the script using the following command:
--      cat list_databases.sql | mysql -hlocalhost -uroot -p

-- Additional Notes:
--   - Ensure the specified MySQL user has the necessary
--     permissions to execute the SHOW DATABASES command.

-- ----------------------------------------------------------

SHOW DATABASES;
