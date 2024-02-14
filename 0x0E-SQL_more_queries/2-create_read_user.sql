-- 2-create_read_user.sql

-- Connect to MySQL as root (you may need to use sudo)
-- Example: sudo mysql -u root -p

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;


-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user on the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Fush privileges to apply changes
FLUSH PRIVILEGES;
