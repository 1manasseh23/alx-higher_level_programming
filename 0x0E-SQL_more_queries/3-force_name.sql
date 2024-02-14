-- 3-force_name.sql

-- Connect to MySQL as root (you may need to use sudo)
-- Example: sudo mysql -u root -p hbtn_0d_2


-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
