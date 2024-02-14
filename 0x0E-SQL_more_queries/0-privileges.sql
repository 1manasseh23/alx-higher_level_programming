-- 0-privileges.sql

-- Create the user 'user_0d_1' if not already exists
CREATE USER 'user_0d_1'@'localhost';

-- Grant all privileges to 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create the user 'user_0d_2' if not already exists
CREATE USER 'user_0d_2'@'localhost';

-- Show privileges for 'user_0d_1'
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for 'user_0d_2'
SHOW GRANTS FOR 'user_0d_2'@'localhost';
